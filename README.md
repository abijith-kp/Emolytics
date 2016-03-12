**Emolytics**
=============

Knowing what is the current trend with respect to what people this about a
specific topic is actually a great factor to determine the popularirity what it
gets. Emolytics gives you a platform to for the same. The search keyword given
is used to filter tweets and classified using a supervised classification model
running in the background. This classification model requires an initial dataset
for the learning purpose.

In the initial prototype for Emolytics, it was made as a simple multi-threading
application along with flask, tweepy, sklearn, nltk python libraries for the
back-end and Leaflet.js, Bootstrap was used in the frontend. Now I have tried to
include redis queue for running background jobs and SQLite with SQLAlchemy for
managing databases atleast for the sake of learning about it.

This is now done as a hobby project. And in the future as I get time I would
like to build on this.

Setup
-----

Copy instance/sample-config.py to instance/config.py and change the required
variables accordingly.

LOAD_FUNCTION = 'server.dataset.load_dataset'
Load the dataset using this function. Return from the function should be a two
member tuple - (X, Y).
X - List of text(in this case tweet) used for classification
Y - List of corresponding class of sentiment

To start the server, run the python script runserver.py. Before starting the
server, make it a point to start the redis-server and the redis queue worker
using rq_worker.py.

To-Do and Contribution
----------------------

There are many things yet to be completed especially the UI.
There is many changes that is needed in the NLP-classification part.
I also wanted to reduce the dependencies on external libraries.

Any types of suggestions are welcome. :)
