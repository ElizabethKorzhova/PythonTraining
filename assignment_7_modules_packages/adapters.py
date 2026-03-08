"""Module provides Adapters to convert from one format to another."""
import abc
from typing import Dict, List

from adaptees import JSONAdaptee, CSVAdaptee, XMLAdaptee


class Adapter(abc.ABC):
    """Abstract class for Adapters."""

    def __init__(self, json_file_path: str, csv_file_path: str = "") -> None:
        """Initializes Adapter with json_file_path and csv_file_path."""
        self._json_manager = JSONAdaptee(json_file_path)
        self._csv_manager = CSVAdaptee(csv_file_path)

    @abc.abstractmethod
    def convert(self) -> None:
        """Convert data from one format to another."""
        pass


class JSONtoCSVAdapter(Adapter):
    """Adapter for converting JSON file to CSV file."""

    def convert(self) -> None:
        """Converts JSON file to CSV file."""
        data: List[Dict] = self._json_manager.read()
        self._csv_manager.write(data)


class CSVtoJSONAdapter(Adapter):
    """Adapter for converting CSV file to JSON file."""

    def convert(self) -> None:
        """Converts CSV file to JSON file."""
        data: List[Dict] = self._csv_manager.read()
        self._json_manager.write(data)


class XMLtoJSONAdapter(Adapter):
    """Adapter for converting XML file to JSON file."""

    def __init__(self, json_file_path: str, xml_file_path: str) -> None:
        """Initializes Adapter with json_file_path and xml_file_path."""
        super().__init__(json_file_path)
        self._xml_manager = XMLAdaptee(xml_file_path)

    def convert(self) -> None:
        """Converts XML file to JSON file."""
        data: List[Dict] = self._xml_manager.read()
        self._json_manager.write(data)


if __name__ == '__main__':
    from_json_adapt = JSONtoCSVAdapter("books.json", "books.csv")
    from_json_adapt.convert()

    from_csv_adapt = CSVtoJSONAdapter("students.json", "students.csv", )
    from_csv_adapt.convert()

    from_xml_adapt = XMLtoJSONAdapter("products.json", "products.xml", )
    from_xml_adapt.convert()
