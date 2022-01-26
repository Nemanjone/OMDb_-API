import argparse
import requests
import json
import pandas
import sqlite3

api_url = "http://www.omdbapi.com/"
API_KEY = "7488ae42"

# initiate the parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument("--title", "-t", help="set movie title", nargs='+', default=[], required=True)
parser.add_argument("--rating", "-r", help="set lowest imbd ratings")
parser.add_argument("--genre", "-g", help="set movie genre")

# read arguments from the command line
args = parser.parse_args()


# initialize db
def init_db():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    # get the count of tables with the name MOVIE
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='MOVIE' ")
    if cursor.fetchone()[0] == 1:
        print('Table already exists.')
    else:
        # create table
        cursor.execute("CREATE TABLE MOVIE (TITLE TEXT NOT NULL,CONTENT BLOB NOT NULL)")
        print("Table created successfully")
    return con


# method for inserting data in db
def insert_in_db(data, connection):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO MOVIE VALUES(?,?)", (data["Title"], json.dumps(data)))
    connection.commit()


# check if data are in db and retrieve them
def get_movie_from_db(con, title):
    query = "SELECT CONTENT FROM MOVIE WHERE TITLE = :title"
    movie = pandas.read_sql_query(query, con, params={"title": title})
    if not movie.empty:
        return json.loads(movie['CONTENT'].iloc[0])


# rest of code is used for API calls
def get_single_response(parameters):
    response = requests.get(api_url, params=parameters)
    return response


def get_movies(connection):
    list_of_movies = []
    for title in args.title:
        title = title.strip()
        parameters = {
            "apikey": API_KEY,
            "t": title
        }
        movie = get_movie_from_db(connection, title)
        if movie:
            list_of_movies.append(movie)
        else:
            api_movie = get_single_response(parameters)
            if api_movie:
                api_movie = api_movie.json()
                # if movie is found
                if api_movie["Response"] == "True":
                    insert_in_db(api_movie, connection)
                    list_of_movies.append(api_movie)
                # if movie is not found
                else:
                    print(api_movie["Error"])

    return list_of_movies


def filter_single_movie(movie):
    if args.rating is not None:
        # filter movie by ratings
        if float(movie["imdbRating"]) < float(args.rating):
            return False
    if args.genre is not None:
        # filter genre
        genre = [x.strip() for x in movie["Genre"].split(',')]
        if args.genre not in genre:
            return False
    return True


def filter_movies(connection):
    # get the movies
    movies = get_movies(connection)
    filtered_movies = []
    for movie in movies:
        if filter_single_movie(movie) is True:
            filtered_movies.append(movie)
    return filtered_movies


def save_data_to_file(content):
    with open("movies.json", "w") as file:
        json.dump(content, file, indent=4)


if __name__ == "__main__":
    db_connection = init_db()
    filteredMovies = filter_movies(db_connection)
    if not filteredMovies:
        print("There are no movies that match your criteria.")
    else:
        print(filteredMovies)
        save_data_to_file(filteredMovies)
    db_connection.close()
