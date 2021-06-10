from API_SERVICE import API_SERVICE
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True


class wtiproj03_API:

    @app.route('/rating/<id>', methods=['GET'])
    def getRating(id):
        return jsonify(API_SERVICE().get(id))

    @app.route('/ratings', methods=['GET'])
    def getRatings():
        return jsonify(API_SERVICE().getAll())

    @app.route('/ratings', methods=['DELETE'])
    def deleteRatings():
        return jsonify(API_SERVICE().delete())

    @app.route('/rating', methods=['POST'])
    def createRating():
        return API_SERVICE().create(request.json)

    @app.route('/avg-genre-ratings/all-users', methods=['GET'])
    def getAvgRatings():
        return API_SERVICE().getAvgRatings()

    @app.route('/avg-genre-ratings/user/<user_id>', methods=['GET'])
    def getAvgRating(user_id):
        return API_SERVICE().getAvgRating(user_id)


if __name__ == '__main__':
    wtiproj03_API()
    app.run()
