from wtiproj01_queue import Queue
import time
import datetime


class Consumer:
    def __init__(self):
        self.que = Queue()

    def list(self):
        self.que.list()

    def async_list(self):
        timeout = time.time() + 10

        while True:
            print(datetime.datetime.fromtimestamp(
                time.time()).strftime('%Y-%m-%d %H:%M:%S'), self.list())
            time.sleep(0.25)
            if time.time() > timeout:
                break
