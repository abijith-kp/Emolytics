from server import db, emolytics
from server.models import Tweet, WorkerJob
from twitter import start_streaming, classify

from flask import jsonify, render_template, request, flash, redirect, url_for
from flask.ext.rq import get_queue, job

import os
import random

@emolytics.route("/login", methods=["GET", "POST"])
def login():
    return "Please login to Emolytics"

@emolytics.route("/", methods=["GET"])
def index():
    return "Welcome to Flask-Emolytics"

@emolytics.route("/analytics", methods=["POST", "GET"])
def analytics():
    try:
        wj = WorkerJob.query.first()
        if isinstance(wj, WorkerJob):
            S_job = get_queue('emolytics').fetch_job(wj.stream_job)
            C_job = get_queue('emolytics').fetch_job(wj.classify_job)
            if S_job:
                S_job.cancel()
            if C_job:
                C_job.cancel()
            WorkerJob.query.filter(WorkerJob.stream_job==wj.stream_job).delete(synchronize_session='fetch')
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            except Exception, e:
                pass
        track = request.get_json(force=True)
        track = map(unicode.strip, track["text"].split(","))
        S_job = start_streaming.delay(track=track)
        C_job = classify.delay()
        wj = WorkerJob(S_job.id, C_job.id)
        db.session.add(wj)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
    except Exception, e:
        pass
    return str(track)

@emolytics.route("/maps", methods=["GET"])
def maps():
    return render_template("emolytics.html")

@emolytics.route("/point", methods=["GET"])
def point():
    lat = 0.0
    lon = 0.0
    color = "Green"
    result = Tweet.query.filter((Tweet.flag==False)).first()
    if not isinstance(result, Tweet):
        return jsonify({"lat": lat, "lon": lon, "color": color})
    lat = 0.0
    lon = 0.0
    color = "Green"
    try:
        lat = result.lat
        lon = result.lon
        color = result.color
    except:
        pass
    result.flag = True
    try:
        db.session.commit()
    except IntegrityError, ie:
        pass
    return jsonify({"lat": lat, "lon": lon, "color": color})
