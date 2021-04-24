import redis
import json


class Queue:

    def __init__(self):
        self.client = redis.StrictRedis(port=6381)
        self.que_name = "sample_que"

    def push(self, value):
        self.client.rpush(self.que_name,  json.dumps(value))

    def list(self):
        queue_batch = self.client.lrange(self.que_name, 0, -1)
        for value_read_from_queue in queue_batch:
            print("value: ",
                  json.loads(value_read_from_queue))

    def pull(self):
        values = self.client.lrange(self.que_name, 0, -1)
        self.client.ltrim(self.que_name, len(values), -1)

    def flush(self):
        self.client.flushdb()
