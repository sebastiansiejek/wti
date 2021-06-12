from API_SERVICE import API_SERVICE
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True


class wtiproj03_API:

    @app.route('/ratings', methods=['GET'])
    def getRatings():
        return jsonify(api_service.getAll())

    @app.route('/ratings', methods=['DELETE'])
    def deleteRatings():
        return jsonify(api_service.delete())

    @app.route('/rating', methods=['POST'])
    def createRating():
        return api_service.create(request.json)

    @app.route('/avg-genre-ratings/all-users', methods=['GET'])
    def getAvgRatings():
        return api_service.getAvgRatings()

    @app.route('/avg-genre-ratings/user/<user_id>', methods=['GET'])
    def getAvgRating(user_id):
        return api_service.getAvgRating(user_id)


if __name__ == '__main__':
    wtiproj03_API()
    api_service = API_SERVICE()
    app.run()
