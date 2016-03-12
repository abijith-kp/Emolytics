from server import db

class WorkerJob(db.Model):
    __tablename__ = "worker_job"
    id = db.Column(db.Integer, primary_key=True)
    # user = db.Column(db.String(250))
    # TODO map this to the user table created
    stream_job = db.Column(db.String(250))
    classify_job = db.Column(db.String(250))

    def __init__(self, stream_job, classify_job):
        self.stream_job = stream_job
        self.classify_job = classify_job

    def __repr__(self):
        return "<WorkerJob {} {}>".format(self.stream_job, self.classify_job)
