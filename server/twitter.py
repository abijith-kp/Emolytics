from server import db, auth, emolytics
from server.models import Tweet
from classifier import create_classifier

from tweepy import Stream
from tweepy.streaming import StreamListener

from flask.ext.rq import job

import json
import random
from multiprocessing import Process
from sqlalchemy.exc import IntegrityError

def get_document(status):
    status = json.loads(status)
    lat = 0.0
    lon = 0.0
    try:
        lon, lat = status["place"]["bounding_box"]["coordinates"][0][0]
    except:
        pass
    return {"tweet": status["text"], "pos": [lat, lon]}

class StdOutListener(StreamListener):
    def on_data(self, status):
        with emolytics.app_context():
            try:
                doc = get_document(status)
                loc = doc["pos"]
                if loc != [0, 0]:
                    t = Tweet(doc['tweet'], loc[0], loc[1])
                    db.session.add(t)
                    db.session.commit()
            except IntegrityError, ie:
                pass
            except Exception, e:
                pass
        return True

    def on_error(self, error_code):
        pass

@job('emolytics')
def start_streaming(track=[""], locations=[-180,-90,180,90], languages=["en"]):
    print "Starting streaming"
    l = StdOutListener()
    stream = Stream(auth, l)
    while True:
        try:
            stream.disconnect()
            stream.filter(track=track, locations=locations, languages=languages)
        except Exception, e:
            pass

@job('emolytics')
def classify():
    print "Starting classification"
    with emolytics.app_context():
        CLF = create_classifier()
        c = {0: "green", 1: "red"}

        while True:
            result = Tweet.query.filter((Tweet.flag == False)).all()
            try:
                for t in result:
                    r = CLF.predict(t.tweet.encode('utf-8'))
                    t.color = c[int(r)]
                db.session.commit()
            except IntegrityError, ie:
                pass
                db.session.rollback()
            except Exception, e:
                pass

'''
def start_thread(track):
    global process
    if process != None and process.is_alive():
        process.terminate()
    process = Process(target=start_streaming, kwargs={"track": track})
    process.start()
    print "Started the thread"

def start_classification():
    global clf_process

    if clf_process != None and clf_process.is_alive():
        clf_process.terminate()
    clf_process = Process(target=classify)
    clf_process.start()
    print "Started classification"
'''
