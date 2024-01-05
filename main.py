from __future__ import unicode_literals

from tornado.websocket import websocket_connect
from tornado.ioloop import IOLoop
from tornado import gen

import logging
import json
import sys

from google.cloud import pubsub_v1


echo_uri = 'wss://www.seismicportal.eu/standing_order/websocket'
PING_INTERVAL = 15


def publish(message):
    project_id = 'your-project-id'
    topic_name = 'your-topic'

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    # Message to be sent
    message_data = message

    # Convert the message to bytes
    message_data = json.dumps(message_data)
    message_data_bytes = message_data.encode('utf-8')

    # Create a Pub/Sub message
    message = pubsub_v1.types.PubsubMessage(data=message_data_bytes)

    # Publish the message
    response = publisher.publish(topic_path, messages=[message])



#You can modify this function to run custom process on the message
def myprocessing(message):
    try:
        data = json.loads(message)["data"]
        msg = {"time":data["properties"]["time"],
       "lat":data["properties"]["lat"],
       "lon":data["properties"]["lon"],
       "magnitude":data["properties"]["mag"],
       "type":data["properties"]["action"]}
        
        publish(msg)
    except Exception:
        logging.exception("Unable to parse json message")

@gen.coroutine
def listen(ws):
    while True:
        msg = yield ws.read_message()
        if msg is None:
            logging.info("close")
            self.ws = None
            break
        myprocessing(msg)
        

@gen.coroutine
def launch_client():
    try:
        logging.info("Open WebSocket connection to %s", echo_uri)
        ws = yield websocket_connect(echo_uri, ping_interval=PING_INTERVAL)
    except Exception:
        logging.exception("connection error")
    else:
        logging.info("Waiting for messages...")
        listen(ws)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    ioloop = IOLoop.instance()
    launch_client()
    try:
        ioloop.start()
    except KeyboardInterrupt:
        logging.info("Close WebSocket")
        ioloop.stop()