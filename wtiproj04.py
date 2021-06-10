import pandas as pd


class wtiproj04:

    # zad1
    def getRatedMoviesAndMovieGenres(self):
        ratedMovies = pd.read_csv(
            './user_ratedmovies.dat', nrows=100, header=0, delimiter='\t', usecols=['userID', 'movieID', 'rating'])
        movieGenres = pd.read_csv(
            './movie_genres.dat', nrows=100, header=0, delimiter='\t')

        movieGenres['dummyColumn'] = 1
        movieGenresPivoted = movieGenres.pivot_table(
            index='movieID', columns='genre', values='dummyColumn')
        movieGenresPivoted = movieGenresPivoted.fillna(0)

        columnsNamesMap = {}
        for movieGenresPivotedName in movieGenresPivoted.columns:
            columnsNamesMap[movieGenresPivotedName] = "genre-" + \
                movieGenresPivotedName

        movieGenresPivoted = movieGenresPivoted.rename(
            columns=columnsNamesMap)

        ratedMoviesAndMovieGenres = pd.merge(
            ratedMovies, movieGenresPivoted, on='movieID')

        return ratedMoviesAndMovieGenres


if __name__ == '__main__':
    wtiproj04 = wtiproj04()
    print(wtiproj04.getRatedMoviesAndMovieGenres())
