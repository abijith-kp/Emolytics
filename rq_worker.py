#!/usr/bin/python2.7

import os
from redis import from_url
from redis.exceptions import ConnectionError

from rq import Worker, Queue, Connection

listen = ['emolytics']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0')

conn = from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        try:
            worker.work()
        except ConnectionError:
            print "Please start the redis-server and try again.."
