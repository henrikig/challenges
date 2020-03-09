import csv
from collections import namedtuple
import itertools

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    # Extracts all movies from csv and stores them in a dictionary
    # where keys are directors, and values is a list of movies (named tuples)
    movie_data = {}

    with open(MOVIE_DATA, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            director = row['director_name']
            title = row['movie_title']
            try:
                year = int(row['title_year'])
            except ValueError:
                year = 0
            score = float(row['imdb_score'])
            if year >= MIN_YEAR:
                movie = Movie(title, year, score)
                if director in movie_data:
                    movie_data[director] += [movie]
                else:
                    movie_data[director] = [movie]

    # Remove duplicates and return
    return {k: list(set(v)) for k, v in movie_data.items()}


def get_average_scores(directors):
    # Filter directors with < MIN_MOVIES and calculate average score
    movie_data = {k: v for k, v in directors.items() if len(v) >= MIN_MOVIES}
    for k, v in movie_data.items():
        accum = 0
        for movie in v:
            accum += movie.score
        average = accum / len(v)
        movie_data[k].append(average)

    return movie_data


def print_results(directors):
    # Print directors ordered by highest average rating. For each director
    # print his/her movies also ordered by highest rated movie.
    # See http://pybit.es/codechallenge13.html for example output
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}) {title:<50} {score}'
    sep_line = '-' * 60
    directors = {k: v for k, v in sorted(directors.items(), key=lambda item: item[1][-1], reverse=True)}
    directors = dict(itertools.islice(directors.items(), 20))
    for i, director in enumerate(directors):
        movies = directors[director]
        counter = i + 1
        print(fmt_director_entry.format(counter=counter, director=director, avg=round(movies[-1], 1)))
        print(sep_line)
        for movie in sorted(movies[:len(movies)-1], key=lambda item: item.score, reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print("\n")



def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors_avg = get_average_scores(directors)
    print_results(directors_avg)


if __name__ == '__main__':
    main()
