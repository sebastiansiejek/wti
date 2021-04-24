from wtiproj01_queue import Queue


class Producer:
    def __init__(self):
        self.que = Queue()

    def push(self, message):
        message_to_write_to_queue_as_dict = message
        self.que.push(message_to_write_to_queue_as_dict)
