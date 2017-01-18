import os

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler, StaticFileHandler, Application, url
from tornado.httpclient import AsyncHTTPClient
from tornado.httputil import url_concat
from tornado.escape import json_decode
from tornado import ioloop

from rx.subjects import Subject, BehaviorSubject, ReplaySubject, AsyncSubject
from rx.concurrency import IOLoopScheduler

scheduler = IOLoopScheduler()


def search_wikipedia(term):
    """Search Wikipedia for a given term"""
    url = 'http://en.wikipedia.org/w/api.php'

    params = {
        "action": 'opensearch',
        "search": term,
        "format": 'json'
    }
    # Must set a user agent for non-browser requests to Wikipedia
    user_agent = "RxPY/1.0 Tornado/4.0.1"

    url = url_concat(url, params)

    http_client = AsyncHTTPClient()
    return http_client.fetch(url, method='GET', user_agent=user_agent)


class WSHandler(WebSocketHandler):

    def on_close(self):
        print("WebSocket closed")

    def on_message(self, message):
        # Each time get a new message we are going to add it to our stream
        self.stream.on_next(message)

    def open(self):
        print("WebSocket opened")

        # TODO: Build a subject to use it as a stream of messages.
        # What would be the best kind? Subject, BehaviorSubject, ReplaySubject, AsyncSubject
        self.stream =

        # Get all distinct key up events from the input and only fire if long enough and distinct
        # Before getting the data you will need to do a few things.
        query = self.stream.
        # TODO: You will need to decode the message at it comes as a json string
        # TODO: You will need to extract the key "term"
        # TODO: You will need to filter only if the text is longer than 2 characters 
        # TODO: You will need to pause for 0.5s . To avoid putting a huge load over our server
        # TODO: Only if the value has changed from previous messages

        searcher = query.
        # TODO: Use search_wikipedia function to get the possible results. HINT take a look to flat_map and flat_map_latest
        # TODO: Get the response from wikipedia. HINT x.body

        def on_error(ex):
            print(ex)

        searcher.subscribe(
            #TODO add a send_response function to get the final answer
            on_error
        )


class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html")


def main():
    port = os.environ.get("PORT", 8080)
    app = Application([
        url(r"/", MainHandler),
        (r'/static/(.*)', StaticFileHandler, {'path': "."}),
        (r'/ws', WSHandler)
    ])
    print("Starting server at port: %s" % port)
    app.listen(port)
    ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
