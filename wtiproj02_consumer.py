from wtiproj01_queue import Queue
import time
import datetime


class Consumer:
    def __init__(self):
        self.que = Queue()

    def list(self):
        self.que.list()
