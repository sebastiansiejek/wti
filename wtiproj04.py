import pandas as pd


class wtiproj04:

    # ex.1
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

  # ex.2
    def convertDataFrameToDict(self):
        return self.getRatedMoviesAndMovieGenres().to_dict('records')

  # ex.3
    def convertDictToDataFrame(self):
        return pd.DataFrame.from_dict(self.convertDataFrameToDict())


if __name__ == '__main__':
    wtiproj04 = wtiproj04()
    print(wtiproj04.getRatedMoviesAndMovieGenres())
    print(wtiproj04.convertDataFrameToDict())
    print(wtiproj04.convertDictToDataFrame())
