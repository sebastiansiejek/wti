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
        for i in range(len(queue_batch)):
            print(i, json.loads(queue_batch[i]))

    def pull(self):
        values = self.client.lrange(self.que_name, 0, -1)
        self.client.ltrim(self.que_name, len(values), -1)

    def flush(self):
        self.client.flushdb()
