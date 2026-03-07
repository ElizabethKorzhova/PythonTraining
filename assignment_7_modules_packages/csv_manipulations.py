"""This module manages students data in csv format."""

import csv
from typing import List, Dict, Generator


class StudentsCSVManager:
    """Class to manage students data in csv format.

    Public methods:
        create_csv():
            creates a csv file
        read_csv():
            reads a csv file
        get_mean_students_grade():
            returns the average student grade.
        add_student():
            adds a student data to the csv file.
    """

    def __init__(self, filepath: str) -> None:
        """Initializes StudentsCSVManager instance.

        Args:
            filepath (str): path to csv file
        """
        self._filepath = filepath
        self._fieldnames: List[str] = []
        self._data: List[Dict[str, str | int]] = []

    def create_csv(self, fieldnames: List[str], data: List[Dict[str, int | str]]) -> None:
        """Creates the csv file with given fields."""
        self._check_keys(fieldnames, data)
        self._fieldnames = fieldnames
        self._data = data
        with open(self._filepath, "w+", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._fieldnames)
            writer.writeheader()
            for row in self._data:
                writer.writerow(row)

    def read_csv(self) -> Generator:
        """Reads the csv file."""
        with open(self._filepath, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            self._fieldnames = list(reader.fieldnames)
            self._data = list(reader)

        yield ", ".join(self._fieldnames)

        for data in self._data:
            yield ", ".join(data.values())

    def get_mean_students_grade(self):
        """Calculates the average student grade."""
        count = 0
        total = 0
        for data in self._data:
            count += 1
            total += int(data["Rating"])
        return f"The average student grade: {(total / count):.2f}"

    def add_student(self, student_data: Dict[str, str | int]) -> None:
        """Adds a data of a new student to the csv file."""
        self._check_keys(self._fieldnames, [student_data])

        with open(self._filepath, "a", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._fieldnames)
            writer.writerow(student_data)

        self._data.append(student_data)

    @staticmethod
    def _check_keys(fieldnames, data) -> None:
        """Check the required keys and the correctness of the format of the data provided."""
        if not fieldnames and not data:
            raise ValueError("Parameters cannot be empty")

        for row in data:
            if len(row) != len(fieldnames):
                raise ValueError("Incorrect number of fields")
            if list(row.keys()) != fieldnames:
                raise KeyError("Keys do not match")
            if not isinstance(row["Rating"], int) or not isinstance(row["Age"], int):
                raise TypeError("Rating and Age should be an integer")


if __name__ == '__main__':
    students = StudentsCSVManager("students.csv")
    students.create_csv(["Name", "Age", "Rating"],
                        [{"Name": "Peter", "Age": 21, "Rating": 90},
                         {"Name": "Marina", "Age": 22, "Rating": 85},
                         {"Name": "Andrew", "Age": 20, "Rating": 88}])
    for line in students.read_csv():
        print(line)

    print(students.get_mean_students_grade())
    students.add_student({"Name": "Bob", "Age": 19, "Rating": 60})
    print(students.get_mean_students_grade())
