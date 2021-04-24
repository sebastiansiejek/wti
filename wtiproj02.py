import time
import pandas as pd
import json
from wtiproj01_queue import Queue
from wtiproj02_consumer import Consumer
from wtiproj02_producer import Producer

data = pd.read_csv('./user_ratedmovies.dat', nrows=100, sep="  ", header=0)


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

    for index, row in data.iterrows():
        producer.push(row.to_json())

    consumer.list()


def zad5():
    consumer = Consumer()
    producer = Producer()

    row_iterator = data.iterrows()

    for row in row_iterator:
        row_as_dict = row[1].to_dict()
        producer.push(row_as_dict)
        time.sleep(0.25)
        consumer.async_list()


zad5()
