import json
from flask import Flask
from wtiproj03 import RatedMoviesAndMovieGenresDataFrame

app = Flask(__name__)
app.config["DEBUG"] = True


class API_SERVICE:

    def get(self, id):
        response = {}
        response["message"] = "Rating has been added"
        response["data"] = {
            "rating_id": id
        }

        return response

    def getAll(self):
        data = RatedMoviesAndMovieGenresDataFrame().getMergedTables()

        return data.to_dict('records')

    def delete(self):
        return []

    def create(self, json_data):
        response = {}
        response["message"] = "Rating has been added"
        response["data"] = json_data

        return response

    def getAvgRatings(self):
        response = {}
        response["genre"] = ""

        return response

    def getAvgRating(self, user_id):
        response = {}
        response["data"] = {
            "user_id": user_id
        }

        return response


if __name__ == '__main__':
    api_service = API_SERVICE()
    print(api_service.get())
