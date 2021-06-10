import pandas as pd


class RatedMoviesAndMovieGenresDataFrame:

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
    lab03 = RatedMoviesAndMovieGenresDataFrame()
    data = lab03.getRatedMoviesAndMovieGenres()

    row_iterator = data.iterrows()

    for row in row_iterator:
        print(row)
