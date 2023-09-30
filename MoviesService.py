import pandas as pd
from flask import jsonify

class MoviesService():
    
    def __init__(self):
        self.df_filmes = pd.read_csv("netflix_titles.csv")

    def movieList(self):
        return  self.df_filmes.to_json()
    
    def movieDirectorList(self):
        return  self.df_filmes['director'].unique().tolist()
    
    def moviesByDirector(self, name):
        return self.df_filmes[self.df_filmes['director'].fillna('').str.contains(name, case=False)].to_json()
    
    def moviesByReleaseYear(self, year):
        return self.df_filmes[self.df_filmes['release_year'] == int(year)].to_json()
    
    def addMovie(self, movie_data):
        try:
            movie_schema = MovieSchema()
            validated_movie = movie_schema.load(movie_data)
            id = 's' + str(int(self.df_filmes['show_id'].tail(1).to_string().split('s')[1]) + 1)
            validated_movie['show_id'] = id
            self.df_filmes = self.df_filmes.append(newMovie, ignore_index=True)
            return jsonify({"message": "Movie created successfully", "movie_id": movie_id}), 201
        except ValidationError as err:
            return jsonify({"error": err.messages}), 400
    
    def movieById(self, id):
        return self.df_filmes[self.df_filmes['show_id'] == id].to_json()
        
    def updateMovie(self, id, data):
        updated_data_keys = ['type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']
        updated_data_values = [data['type'], data['title'], data['director'], data['cast'], data['country'], data['date_added'], data['release_year'], data['rating'], data['duration'], data['listed_in'], data['description']]
        self.df_filmes.loc[self.df_filmes['show_id'] == id, updated_data_keys] = updated_data_values
        return f'Movie Updated: {updated_data}'

    def deleteMovieById(self, id):
        self.df_filmes = self.df_filmes[self.df_filmes['show_id'] != id]
        return f'Movie Deleted: {id}'