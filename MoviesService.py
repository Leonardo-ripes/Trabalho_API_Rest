import pandas as pd

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
    
    def addMovie(self, data):
        type = data['type']
        title = data['title']	
        director = data['director']
        cast = data['cast']
        country	= data['country']
        date_added = data['date_added']
        release_year = data['release_year']
        rating = data['rating']
        duration = data['duration']
        listed_in = data['listed_in']
        description = data['description']
        id = 's' + str(int(self.df_filmes['show_id'].tail(1).to_string().split('s')[1]) + 1)

        newMovie = {'show_id': id, 'type': type, 'title': title, 'director': director, 'cast': cast, 'country': country, 'date_added': date_added, 'release_year': release_year, 'rating': rating, 'duration': duration, 'listed_in': listed_in, 'description': description}
        self.df_filmes = self.df_filmes.append(newMovie, ignore_index=True)
        return f'New Movie Added: {newMovie}'

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