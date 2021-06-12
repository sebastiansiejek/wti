import requests
import time


class wtiproj03_API_CLIENT:

    def __init__(self):
        self.enpoint = "http://127.0.0.1:5000/"

    def getAll(self):
        r = requests.get(self.enpoint + "ratings")
        print('ratings/', r.json(), r.status_code)

    def add(self):
        r = requests.post(self.enpoint + "rating", data={
            "genre-Action": 0,
            "genre-Adventure": 0,
            "genre-Animation": 0,
            "genre-Children": 0,
            "genre-Comedy": 1,
            "genre-Crime": 0,
            "genre-Documentary": 0,
            "genre-Drama": 0,
            "genre-Fantasy": 0,
            "genre-Horror": 0,
            "genre-IMAX": 0,
            "genre-Mystery": 0,
            "genre-Romance": 1,
            "genre-Sci-Fi": 0,
            "genre-Thriller": 0,
            "genre-War": 0,
            "genre-movieID": 3,
            "rating": 1,
            "userID": 999
        })
        print('add rating/', r.json(), r.status_code)

    def delete(self):
        r = requests.delete(self.enpoint + "ratings")
        print('delete ratings/', r.json(), r.status_code)

    def getAvgRatings(self):
        r = requests.get(self.enpoint + "avg-genre-ratings/all-users")
        print('avg-genre-ratings/all-users/', r.json(), r.status_code)

    def getAvgRating(self, id):
        r = requests.get(self.enpoint + "avg-genre-ratings/user/" + str(id))
        print('avg-genre-ratings/user/' + str(id), r.json(), r.status_code)


if __name__ == '__main__':
    client = wtiproj03_API_CLIENT()
    print("\nGet all ------")
    client.getAll()
    time.sleep(0.01)
    print("\nAdd ------")
    client.add()
    time.sleep(0.01)
    print("\nDelete ------")
    client.delete()
    time.sleep(0.01)
    print("\nGet avg ratings ------")
    client.getAvgRatings()
    time.sleep(0.01)
    print("\nGet avg rating ------")
    client.getAvgRating(78)
