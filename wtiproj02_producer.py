from wtiproj01_queue import Queue
import pandas as pd
import time


class Producer:
    def __init__(self):
        self.que = Queue()

    def push(self, message):
        self.que.push(message)


if __name__ == "__main__":

    data = pd.read_csv('./user_ratedmovies.dat',
                       nrows=100, delimiter="\t")

    row_iterator = data.iterrows()
    producer = Producer()
    diagnostic_row_index = 99999

    for row in row_iterator:
        row_as_dict = row[1].to_dict()
        row_as_dict["diagnostic_index"] = diagnostic_row_index
        producer.push(row_as_dict)
        diagnostic_row_index += 1
        time.sleep(0.25)
