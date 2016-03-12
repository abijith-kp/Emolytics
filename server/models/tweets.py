from server import db

class Tweet(db.Model):
    __tablename__ = "tweet"
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(200))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    color = db.Column(db.String(10))
    flag = db.Column(db.Boolean)

    def __init__(self, tweet, lat, lon, color="Green", flag=False):
        self.tweet = tweet
        self.lat = lat
        self.lon = lon
        self.color = color
        self.flag = flag

    def __repr__(self):
        return "<Tweet {}>".format(self.tweet.encode('utf-8'))
