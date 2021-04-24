from wtiproj01_queue import Queue
import time
import datetime


class Consumer:
    def __init__(self):
        self.que = Queue()

    def list(self):
        self.que.list()


if __name__ == "__main__":

    consumer = Consumer()

    timeout = time.time() + 10

    while True:
        print(datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        consumer.list()
        time.sleep(0.4)
        if time.time() > timeout:
            break
