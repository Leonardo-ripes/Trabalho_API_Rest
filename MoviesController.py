import pandas as pd
from MoviesService import MoviesService
from flask import Flask, request, jsonify

moviesService = MoviesService()

app = Flask(__name__)

################################################
#                    ROUTES                    #
################################################

################################################
#                    GET                       #
################################################
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/movies', methods=['GET'])
def movieList():
    return  moviesService.movieList()

@app.route('/director', methods=['GET'])
def movieDirectorList():
    return  moviesService.movieDirectorList()

@app.route('/movies/director/<name>', methods=['GET'])
def moviesByDirector(name):
    return moviesService.moviesByDirector(name)

@app.route('/movies/id/<id>', methods=['GET'])
def movieById(id):
    return moviesService.movieById(id)

@app.route('/movies/release_year/<year>', methods=['GET'])
def moviesByReleaseYear(year):
    return moviesService.moviesByReleaseYear(year)

################################################
#                     POST                     #
################################################

@app.route('/addMovie', methods=['POST'])
def json_endpoint():
    data = request.json
    return moviesService.addMovie(data)

################################################
#                     PUT                      #
################################################

@app.route('/updateMovie/<id>', methods=['PUT'])
def updateMovie(id):
    data = request.json
    return moviesService.updateMovie(id,data)

################################################
#                    DELETE                    #
################################################

@app.route('/deleteMovie/id/<id>', methods=['DELETE'])
def deleteMovieById(id):
    return moviesService.deleteMovieById(id)

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()