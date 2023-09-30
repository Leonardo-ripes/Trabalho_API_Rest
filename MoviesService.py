import pandas as pd
from flask import jsonify
from marshmallow import ValidationError
from Movie import MovieSchema

class MoviesService():
    
    def __init__(self):
        self.df_filmes = pd.read_csv("netflix_titles.csv")

    def movieList(self):
        return jsonify(self.df_filmes.to_dict(orient='records'))
    
    def movieDirectorList(self):
        return jsonify(self.df_filmes['director'].unique().tolist())
    
    def moviesByDirector(self, name):
        df_rows = self.df_filmes[self.df_filmes['director'].fillna('').str.contains(name, case=False)]
        if df_rows.empty:
            return f'Movie with directors {name} not found', 404
        return jsonify(df_rows.to_dict(orient='records'))
    
    def moviesByReleaseYear(self, year):
        if isinstance(year, int) and year < 1700:
            return f'Invalid year: {year}', 400
        return jsonify(self.df_filmes[self.df_filmes['release_year'] == int(year)].to_dict(orient='records'))
    
    def addMovie(self, movie_data):
        try:
            movie_schema = MovieSchema()
            validated_movie = movie_schema.load(movie_data)
            id = 's' + str(int(self.df_filmes['show_id'].tail(1).to_string().split('s')[1]) + 1)
            validated_movie['show_id'] = id
            self.df_filmes = self.df_filmes.append(validated_movie, ignore_index=True)
            return jsonify({"message": "Movie created successfully", "show_id": id}), 201
        except ValidationError as err:
            return jsonify({"error": err.messages}), 400
    
    def movieById(self, id):
        movie_row = self.df_filmes[self.df_filmes['show_id'] == id]    
        if movie_row.empty:
            return f'Movie not found: {id}', 404
        return jsonify(movie_row.to_dict(orient='records')[0])
        
    def updateMovie(self, id, data):
        try:
            movie_schema = MovieSchema()
            validated_movie = movie_schema.load(data)
        except ValidationError as err:
            return jsonify({"error bad body structure": err.messages}), 400
        
        if(self.df_filmes.loc[self.df_filmes['show_id'] == id].empty):
            return f'Movie not found: {id}', 404    

        updated_data_keys = ['type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']
        updated_data_values = [data['type'], data['title'], data['director'], data['cast'], data['country'], data['date_added'], data['release_year'], data['rating'], data['duration'], data['listed_in'], data['description']]
        self.df_filmes.loc[self.df_filmes['show_id'] == id, updated_data_keys] = updated_data_values
        return f'Movie Updated show_id: {id}'
        
    def deleteMovieById(self, id):
        if(self.df_filmes.loc[self.df_filmes['show_id'] == id].empty):
            return f'Movie not found: {id}', 404
        self.df_filmes = self.df_filmes[self.df_filmes['show_id'] != id]
        return jsonify({"message": "Movie deleted successfully", "show_id": id}), 200 