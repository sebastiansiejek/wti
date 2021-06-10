import json
from flask import Flask
from wtiproj03 import RatedMoviesAndMovieGenresDataFrame
import random

app = Flask(__name__)
app.config["DEBUG"] = True


class API_SERVICE:

    def __init__(self):
        self.rawRatingData = []

    def get(self, id):
        response = {}
        response["message"] = ""
        response["data"] = {
            "rating_id": id
        }

        return response

    def getAll(self):
        data = RatedMoviesAndMovieGenresDataFrame().getRatedMoviesAndMovieGenres()

        return data.to_dict('records')

    def delete(self):
        self.rawRatingData = []
        return self.rawRatingData

    def create(self, json_data):
        response = {}
        response["message"] = "Rating has been added"
        response["data"] = json_data

        return response

    def getAvgRatings(self):
        dummy_avg_genre_ratings = {}

        for rawRatingDataItem in self.getAll():
            rawRatingDataItemKeys = list(rawRatingDataItem)
            for rawRatingDataItemKey in rawRatingDataItemKeys:
                if rawRatingDataItemKey[:6] == "genre-":
                    dummy_avg_genre_ratings[rawRatingDataItemKey] = random.random(
                    )

        return dummy_avg_genre_ratings

    def getAvgRating(self, user_id):
        response = {}
        response["data"] = {
            "user_id": user_id
        }

        return response


if __name__ == '__main__':
    api_service = API_SERVICE()
    print(api_service.getAvgRatings())
