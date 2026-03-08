"""Module provides Adaptee classes for reading from and writing data to different formats
(json, csv, xml)."""
import abc
import json
import csv
import xmltodict
from typing import List, Dict


class Adaptee(abc.ABC):
    """Abstract class for Adaptee classes."""

    def __init__(self, file_path: str) -> None:
        """Initializes Adaptee with file path."""
        self._file_path = file_path

    @abc.abstractmethod
    def read(self) -> List[Dict]:
        """Read data from the file."""
        pass

    @abc.abstractmethod
    def write(self, data: List[Dict]) -> None:
        """Write data to the file."""
        pass


class JSONAdaptee(Adaptee):
    """Adapter for reading data from and writing data to json file."""

    def read(self) -> List[Dict]:
        """Reads data from json file and return the list of dictionaries."""
        with open(self._file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data

    def write(self, data: List[Dict]) -> None:
        """Writes data to json file."""
        with open(self._file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


class CSVAdaptee(Adaptee):
    """Adapter for reading data from and writing data to csv file."""

    def read(self) -> List[Dict]:
        """Reads data from csv file and return the list of dictionaries."""
        with open(self._file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            data = list(reader)
        return data

    def write(self, data: List[Dict]) -> None:
        """Writes data to csv file."""
        with open(self._file_path, "w", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys(), delimiter=",")
            writer.writeheader()
            writer.writerows(data)


class XMLAdaptee(Adaptee):
    """Adapter for reading data from and writing data to xml file."""

    def read(self) -> List[Dict]:
        """Reads data from xml file and return the list of dictionaries."""
        with open(self._file_path, "r", encoding="utf-8") as xml_file:
            data = [xmltodict.parse(xml_file.read())]
        return data

    # TODO: Add the logic if writing data (list) to xml
    def write(self, data: List[Dict]) -> None:
        """Writes data to xml file."""
        pass
