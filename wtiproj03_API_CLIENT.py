import requests
import time
from API_SERVICE import API_SERVICE


class wtiproj03_API_CLIENT:

    def __init__(self):
        self.enpoint = "http://127.0.0.1:5000/"

    def getAll(self):
        r = requests.get(self.enpoint + "ratings")
        print('ratings/', r.status_code)

    def delete(self):
        r = requests.delete(self.enpoint + "ratings")
        print('delete ratings/', r.status_code)

    def getAvgRatings(self):
        r = requests.get(self.enpoint + "avg-genre-ratings/all-users")
        print('avg-genre-ratings/all-users/', r.status_code)

    def getAvgRating(self, id):
        r = requests.get(self.enpoint + "avg-genre-ratings/user/" + str(id))
        print('avg-genre-ratings/user/' + str(id), r.status_code)


if __name__ == '__main__':
    client = wtiproj03_API_CLIENT()
    client.getAll()
    time.sleep(0.01)
    client.delete()
    time.sleep(0.01)
    client.getAvgRatings()
    time.sleep(0.01)
    client.getAvgRating(78)
