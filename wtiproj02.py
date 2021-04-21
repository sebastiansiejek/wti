from wtiproj01_queue import Queue
import time


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
