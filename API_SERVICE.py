import json
from flask import Flask
from wtiproj03 import RatedMoviesAndMovieGenresDataFrame
import random

app = Flask(__name__)
app.config["DEBUG"] = True


class API_SERVICE:

    def __init__(self):
        self.rawRatingData = self.getAll()

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

        for rawRatingDataItem in self.rawRatingData:
            rawRatingDataItemKeys = list(rawRatingDataItem)
            for rawRatingDataItemKey in rawRatingDataItemKeys:
                if rawRatingDataItemKey[:6] == "genre-":
                    dummy_avg_genre_ratings[rawRatingDataItemKey] = random.random(
                    )

        return dummy_avg_genre_ratings

    def getAvgRating(self, user_id):
        response = {}

        dummy_avg_genre_ratings_for_user = {}

        for rawRatingDataItem in self.rawRatingData:
            if rawRatingDataItem["userID"] == int(user_id):
                rawRatingDataItemKeys = list(rawRatingDataItem)
                for rawRatingDataItemKey in rawRatingDataItemKeys:
                    if rawRatingDataItemKey[:6] == "genre-":
                        dummy_avg_genre_ratings_for_user[rawRatingDataItemKey] = random.random(
                        )

        response["data"] = {
            "user_id": user_id,
            "ratings": dummy_avg_genre_ratings_for_user,
            "message": "User not exists" if not dummy_avg_genre_ratings_for_user.keys() else ""
        }

        return response


if __name__ == '__main__':
    api_service = API_SERVICE()
