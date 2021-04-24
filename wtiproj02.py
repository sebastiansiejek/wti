from wtiproj01_queue import Queue
import time
import pandas as pd
import json


class Producer:
    def __init__(self):
        self.que = Queue()

    def push(self, message):
        message_to_write_to_queue_as_dict = message
        self.que.push(message_to_write_to_queue_as_dict)


class Consumer:
    def __init__(self):
        self.que = Queue()

    def list(self):
        self.que.list()


def zad3():
    producer = Producer()
    consumer = Consumer()

    que = Queue()
    que.pull()

    producer.push("message1")
    time.sleep(0.10)
    producer.push("message2")
    consumer.list()


def zad4():
    producer = Producer()
    consumer = Consumer()

    que = Queue()
    que.pull()

    data = pd.read_csv('./user_ratedmovies.dat', nrows=100)
    for index, row in data.iterrows():
        producer.push(row[0])

    consumer.list()


zad4()
