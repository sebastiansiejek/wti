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
                  value_read_from_queue)

    def pull(self):
        values = self.client.lrange(self.que_name, 0, -1)
        self.client.ltrim(self.que_name, len(values), -1)

    def flush(self):
        self.client.flushdb()


if __name__ == "__main__":
    que = Queue()
    que.pull()
    message_to_write_to_queue_as_dict = {}
    message_to_write_to_queue_as_dict["pole1"] = "wartosc1"
    message_to_write_to_queue_as_dict["pole2"] = "wartosc2"
    que.push(message_to_write_to_queue_as_dict)
    que.list()
    que.pull()
    message_to_write_to_queue_as_dict2 = {}
    message_to_write_to_queue_as_dict2["nowe_pole"] = "wartosc1"
    que.push(message_to_write_to_queue_as_dict2)
    que.push(message_to_write_to_queue_as_dict2)
    que.list()
