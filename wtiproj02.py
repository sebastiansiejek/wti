import time
import pandas as pd
import json
from wtiproj01_queue import Queue
from wtiproj02_consumer import Consumer
from wtiproj02_producer import Producer


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
        producer.push(row.to_json())

    consumer.list()


def zad5():
    consumer = Consumer()
    consumer.async_list()


zad4()
zad5()
