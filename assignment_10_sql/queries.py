"""This module provides functions with database queries to retrieve for data. """
import sqlite3
from typing import Tuple, List


def create_tables(cursor: sqlite3.Cursor) -> None:
    """
    Creates database tables movies, actors and movie_cast

    Args:
        cursor (sqlite3.Cursor): cursor object
    """
    cursor.execute("""CREATE TABLE IF NOT EXISTS movies (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        release_year INTEGER NOT NULL,
                        genre TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS actors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        birth_year INTEGER NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS movie_cast (
                        movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
                        actor_id INTEGER REFERENCES actors(id) ON DELETE CASCADE,
                        PRIMARY KEY (movie_id, actor_id))""")


def add_actor(cursor: sqlite3.Cursor, data: Tuple[str, int]) -> None:
    """
    Adds actor data to database

    Args:
        cursor (sqlite3.Cursor): cursor object
        data (Tuple[str, int]): actor data such as name, birth_year
    """
    cursor.execute("""INSERT INTO actors (name, birth_year) VALUES (?, ?)""", data)
    cursor.connection.commit()


def add_movie(cursor: sqlite3.Cursor, data: Tuple[str, int, str]) -> None:
    """
    Adds movie data to database

    Args:
        cursor (sqlite3.Cursor): cursor object
        data (Tuple[str, int, str]): movie data such as title, release_year, genre
    """
    cursor.execute("""INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)""", data)
    cursor.connection.commit()


def add_movie_cast(cursor: sqlite3.Cursor, movie_title: str, actor_name: str) -> None:
    """
    Search movie_id and actor_id by title and name. And ids to movie_cast table

    Args:
        cursor (sqlite3.Cursor): cursor object
        movie_title (str): movie title
        actor_name (str): actor name
    """
    try:
        cursor.execute(f"""INSERT INTO movie_cast (movie_id, actor_id)
                            SELECT movies.id, actors.id
                            FROM movies, actors
                            WHERE movies.title = '{movie_title}' AND actors.name = '{actor_name}'""")
        cursor.connection.commit()
    except sqlite3.IntegrityError as ex:
        print(ex)


def get_data(cursor: sqlite3.Cursor) -> List[Tuple]:
    """
    Returns movie title and actor name from movie_cast table

    Args:
        cursor (sqlite3.Cursor): cursor object
    Returns:
        List[Tuple]: list of tuples that contains movie title and actor name
    """
    return cursor.execute("""SELECT movies.title, actors.name
                            FROM movie_cast
                            INNER JOIN movies ON movies.id = movie_cast.movie_id
                            INNER JOIN actors ON actors.id = movie_cast.actor_id
                            """).fetchall()


def select_unique(cursor: sqlite3.Cursor, table: str, column: str) -> List[Tuple]:
    """
    Returns unique data from given table and column name

    Args:
        cursor (sqlite3.Cursor): cursor object
        table (str): table name
        column (str): column name
    Returns:
        List[Tuple]: list of tuples that contains unique of column
    """
    return cursor.execute(f"""SELECT DISTINCT {column} FROM {table}""").fetchall()


def count_values(cursor: sqlite3.Cursor, table: str, column: str) -> List[Tuple]:
    """
    Counts unique values of given column

    Args:
        cursor (sqlite3.Cursor): cursor object
        table (str): table name
        column (str): column name
    Returns:
        List[Tuple]: list of tuples that contains unique item and its count
    """
    return cursor.execute(f"""SELECT {column}, COUNT(*) FROM {table} GROUP BY {column}""").fetchall()


def select_by_value(cursor: sqlite3.Cursor, table: str, column: str, value:str) -> Tuple:
    """
    Returns data where column has specific value

    Args:
        cursor (sqlite3.Cursor): cursor object
        table (str): table name
        column (str): column name
        value (str): search value
    Returns:
        Tuple: tuple that contain specific value in column
    """
    return cursor.execute(f"""SELECT * FROM {table} WHERE {column} = '{value}'""").fetchone()


def get_year_average(cursor: sqlite3.Cursor) -> List[Tuple]:
    """
    Counts average birth year of actors by specific movie genre

    Args:
        cursor (sqlite3.Cursor): cursor object
    Returns:
        List[Tuple]: list of tuples that contains average birth year and movie genre
    """
    return cursor.execute(f"""SELECT movies.genre, AVG(actors.birth_year) AS average_birth_year
                                FROM movie_cast m
                                INNER JOIN movies ON m.movie_id = movies.id
                                INNER JOIN actors ON m.actor_id = actors.id
                                GROUP BY movies.genre
                            """).fetchall()


def search_film_by_title(cursor: sqlite3.Cursor, search_param: str) -> List[Tuple]:
    """
    Search movies by title

    Args:
         cursor (sqlite3.Cursor): cursor object
         search_param (str): search data
    Returns:
        List[Tuple]: list of tuples that contains the result of searching
    """
    return cursor.execute(f"""SELECT title FROM movies
                                WHERE title LIKE '%{search_param}%';
                            """).fetchall()


def show_with_pagination(cursor: sqlite3.Cursor, page: int, per_page: int) -> List[Tuple]:
    """
    Returns movie title with given limit (per_page) and calculated offset

    Args:
        cursor (sqlite3.Cursor): cursor object
        page (int): page number
        per_page (int): number data per page
    Returns:
        List[Tuple]: list of tuples that contains title movie
    """
    offset = (page * per_page) - per_page
    return cursor.execute(f"""SELECT title FROM movies LIMIT {per_page} OFFSET {offset}""").fetchall()


def union_actors_movies(cursor: sqlite3.Cursor) -> List[Tuple]:
    """
    Unions actors and movies to one column

    Args:
        cursor (sqlite3.Cursor): cursor object
    Returns:
        List[Tuple]: list of tuples that contains actors and movies in one column
    """
    return cursor.execute(f"""SELECT name AS actors_and_movies FROM actors
                                UNION
                                SELECT title AS actors_and_movies FROM movies""").fetchall()


def movie_age(cursor: sqlite3.Cursor) -> List[Tuple]:
    """
    Calculates age of movies

    Args:
        cursor (sqlite3.Cursor): cursor object
    Returns:
        List[Tuple]: list of tuples that contains movie title and its age
    """
    return cursor.execute("""SELECT title, STRFTIME('%Y', 'now') - release_year FROM movies""").fetchall()
