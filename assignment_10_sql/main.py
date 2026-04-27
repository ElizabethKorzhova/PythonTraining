"""This module provides functionality for managing the cinema database"""
import math

from utils import connect_db
from queries import (create_tables, add_actor, add_movie, add_movie_cast, get_data,
                     select_unique, count_values, select_by_value, get_year_average,
                     search_film_by_title, show_with_pagination,
                     union_actors_movies, movie_age)

DATABASE_NAME = "cinema.db"


def main() -> None:
    """Represents console application for managing the cinema database"""
    cursor = connect_db(DATABASE_NAME)
    create_tables(cursor)
    while True:
        option = input(
            "Select an option:\n\t"
            "1. Add actor data\n\t"
            "2. Add movie data\n\t"
            "3. Show all actors and movies\n\t"
            "4. Show all unique genres\n\t"
            "5. Show count of movies by genres\n\t"
            "6. Show average birth year of actors in movies of a specific genre\n\t"
            "7. Search a movie by title\n\t"
            "8. Show movies (with pagination)\n\t"
            "9. Show the names of all actors and the titles of all movies\n\t"
            "10. Relate actor to movie\n\t"
            "11. Show title movie with their ages\n\t"
            "0. Exit\n\t").strip()

        match option:
            case "1":
                while True:
                    name = input("Enter actor name: ").strip()
                    if name.isalpha():
                        break
                    print("Enter a valid name")

                while True:
                    birth_year = input("Enter actor birth year: ").strip()
                    if birth_year.isdigit():
                        break
                    print("Birth year must be an integer")

                add_actor(cursor, (name, int(birth_year)))
                print("Actor successfully added")

            case "2":
                while True:
                    title = input("Enter movie title: ").strip()
                    if not title.isspace():
                        break
                    print("Enter a valid title")

                while True:
                    release_year = input("Enter movie release year: ").strip()
                    if release_year.isdigit():
                        break
                    print("Release year must be an integer")

                while True:
                    genre = input("Enter genre: ").strip()
                    if genre.isalpha():
                        break
                    print("Enter valid genre")

                add_movie(cursor, (title, int(release_year), genre))

                while True:
                    actor_name = input("Enter actor name that related to this movie: ").strip()
                    if actor_name.isalpha():
                        break
                    print("Enter a valid actor name")

                related_actor = select_by_value(cursor, "actors", "name", actor_name)
                if not related_actor:
                    print("Actor does not exist. Please add this to database and relate to the movie by 10 option.")
                add_movie_cast(cursor, title, related_actor[1])

            case "3":
                data = get_data(cursor)
                current_movie = ""
                actors = []
                for item in data:
                    if current_movie != item[0]:
                        print(f"- Movie title: {item[0]}")
                        for actor in actors:
                            print(f"\tActor name: {actor}")
                        actors.clear()
                        actors.append(item[1])
                        current_movie = item[0]
                    else:
                        actors.append(item[1])

            case "4":
                genres = select_unique(cursor, "movies", "genre")
                print(f"Unique genres:")
                for genre in genres:
                    print(f"\t- {genre[0]}")

            case "5":
                genres = count_values(cursor, "movies", "genre")
                print(f"Unique genres with counts:")
                for genre in genres:
                    print(f"\t- {genre[0]}: {genre[1]}")

            case "6":
                data = get_year_average(cursor)
                for item in data:
                    print(f"- Genre: {item[0]}\n\tAverage birth year of actors: {item[1]}")

            case "7":
                search_param = input("Enter movie title to search: ").strip()
                search_result = search_film_by_title(cursor, search_param)
                if not search_result:
                    print("No results found")
                else:
                    print("Search result:")
                    for movie in search_result:
                        print(f"\t- {movie[0]}")

            case "8":
                while True:
                    per_page = input("Enter number of data per page: ").strip()
                    if per_page.isdigit():
                        break
                    print("Data per page must be an integer")

                while True:
                    page = input("Enter page to show: ").strip()
                    if page.isdigit():
                        break
                    print("Data page must be an integer")

                data = show_with_pagination(cursor, int(page), int(per_page))
                if not data:
                    print("Invalid option. Please try again.")
                else:
                    total_movies = len(count_values(cursor, "movies", "title"))
                    total_pages = math.ceil(total_movies / int(per_page))
                    print(f"{page} page of {total_pages} page(s):")
                    for movie in data:
                        print(f"\t- {movie[0]}")
                    print(f"Total number of movies: {total_movies}. Shown {per_page} movies.")

            case "9":
                data = union_actors_movies(cursor)
                for item in data:
                    print(f"\t- {item[0]}")

            case "10":
                while True:
                    movie_title = input("Enter movie title: ").strip()
                    if not movie_title.isspace():
                        break
                    print("Enter a valid title")

                related_movie = select_by_value(cursor, "movies", "title", movie_title)
                if not related_movie:
                    print("Movie does not exist. Please add this movie to database and try again.")

                while True:
                    actor_name = input("Enter actor name: ").strip()
                    if not actor_name.isspace():
                        break
                    print("Enter a valid name")
                related_actor = select_by_value(cursor, "actors", "name", actor_name)

                if not related_actor:
                    print("Actor does not exist. Please add this actor to database and try again.")

                if related_actor and related_movie:
                    add_movie_cast(cursor, related_movie[1], related_actor[1])

            case "11":
                data = movie_age(cursor)
                for item in data:
                    print(f"\t- {item[0]}: {item[1]} years")

            case "0":
                print("Have a nice day!")
                break

            case _:
                print("Invalid option. Please try again.")
    cursor.close()


if __name__ == '__main__':
    main()
