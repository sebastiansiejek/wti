
import json
from wtiproj03 import RatedMoviesAndMovieGenresDataFrame


if __name__ == '__main__':
    mergedTables = RatedMoviesAndMovieGenresDataFrame()
    data = mergedTables.getMergedTables()

    row_iterator = data.iterrows()

    for row in row_iterator:
        row_as_dict = row[1].to_dict()
        row_as_json = json.dumps(row_as_dict)
        print(row_as_json)
