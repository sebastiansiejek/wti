import pandas as pd


class Lab03:

    # zad01
    def getRatedMoviesAndMovieGenres(self):
        ratedMovies = pd.read_csv(
            './user_ratedmovies.dat', nrows=100, header=0, delimiter='\t', usecols=['userID', 'movieID', 'rating'])
        movieGenres = pd.read_csv(
            './movie_genres.dat', nrows=100, header=0, delimiter='\t')

        movieGenres['dummyColumn'] = 1
        movieGenresPivoted = movieGenres.pivot_table(
            index='movieID', columns='genre', values='dummyColumn')
        movieGenresPivoted = movieGenresPivoted.fillna(0)

        ratedMoviesAndMovieGenres = pd.merge(
            ratedMovies, movieGenresPivoted, on='movieID')

        return ratedMoviesAndMovieGenres


if __name__ == '__main__':
    lab03 = Lab03()
    lab03.getratedMoviesAndMovieGenres()
