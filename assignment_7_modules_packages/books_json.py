"""This module provides BooksJSONManager class to manage books data in json format."""
from typing import List, Dict
import json
import datetime


class BooksJSONManager:
    """Class to manage book data in json format.

    Public methods:
        load_json():
            reads a json file;
        get_available_books():
            returns all available books from the store;
        add_new_book():
            adds a data of a new book to json file.
    """

    _REQUIRED_FIELDS = ['Name', 'Author', 'Year', 'Availability']
    _CURRENT_YEAR = datetime.datetime.now().year

    def __init__(self) -> None:
        """Initializes BooksJSONManager instance. There are no public arguments."""
        self._file_path = ""
        self._data: List[Dict[str, str | int | bool]] = []

    def load_json(self, file_path: str) -> List[Dict[str, str | int | bool]]:
        """Reads a json file and returns a list of books."""
        self._file_path = file_path

        with open(self._file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            self._data = data
        return self._data

    def get_available_books(self) -> List[Dict[str, str | int | bool]] | str:
        """Returns a list of all available books from the store."""
        available_books = []
        for book in self._data:
            if book["Availability"] is True:
                available_books.append(book)

        if not available_books:
            return "There are no available books in the store."
        return available_books

    def add_new_book(self, book_data: Dict[str, str | int | bool]) -> None:
        """Adds a new book to json file."""
        self._check_book(book_data)
        self._data.append(book_data)

        with open(self._file_path, "w", encoding="utf-8") as json_file:
            json.dump(self._data, json_file, ensure_ascii=False, indent=4)

    def _check_book(self, book_data: Dict[str, str | int | bool]) -> None:
        """Check the required keys and the correctness of the format of the data provided."""
        if list(book_data.keys()) != self._REQUIRED_FIELDS:
            raise KeyError("Key do not match with required fields")
        if not book_data["Name"] or not book_data["Author"] or not book_data["Year"]:
            raise ValueError("All fields are required")
        if not isinstance(book_data["Availability"], bool):
            raise TypeError("Availability must be a boolean")
        if not isinstance(book_data["Year"], int) or book_data["Year"] > self._CURRENT_YEAR:
            raise Exception("Year must be an integer and cannot be greater than current year")


if __name__ == '__main__':
    books = BooksJSONManager()
    print(books.load_json("books.json"))
    print(books.get_available_books())
    books.add_new_book({"Name": "Book", "Author": "Author", "Year": 2026, "Availability": False})
    print(books.get_available_books())
