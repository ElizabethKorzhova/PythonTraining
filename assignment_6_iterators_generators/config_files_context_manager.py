"""This script is designed to implement custom context manager ConfigFilesContextManager
that read the configuration when entering the context and write the changes to a file
after exiting."""
from __future__ import annotations
import os
import configparser
import json
import copy
from typing import Any, Literal, Optional, Dict


class ConfigFilesContextManager:
    """Context manager for working with configuration files, namely making changes to it."""

    def __init__(self, file_path: str) -> None:
        """Initialize context manager with file_path parameter to set data to config file
        (ini or json)."""
        self._file_path = file_path
        self._file_extension = os.path.splitext(file_path)[1].lower()[1:]
        self._config_dict: Dict[str, Any] = {}
        self._origin_dict: Dict[str, Any] = {}

    def __enter__(self) -> ConfigFilesContextManager:
        """Opens given file, saves the data to separate protected attributes
        and returns the object."""
        if not self._file_extension == "ini" and not self._file_extension == "json":
            raise ValueError(
                f"Invalid file extension, got {os.path.splitext(self._file_path)[1]} "
                f"instead of .ini or .json")

        if not os.path.exists(self._file_path):
            self._config_dict = {}

        if os.path.exists(self._file_path):
            if self._file_extension == "json":
                with open(self._file_path, "r", encoding="utf-8") as config_file:
                    self._config_dict = json.load(config_file)

            elif self._file_extension == "ini":
                parser = configparser.ConfigParser()

                parser.read(self._file_path)
                self._config_dict = {
                    section: dict(parser.items(section)) for section in parser.sections()
                }
        else:
            self._config_dict = {}

        self._origin_dict = copy.deepcopy(self._config_dict)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> Literal[False]:
        """Saves the changes to the file if changes were made."""
        if self._config_dict != self._origin_dict:
            self._write_config_to_file()
        return False

    def _write_config_to_file(self) -> None:
        """Writes the changes to the config file (ini or json) from protected
        attribute _config_dict."""
        with open(self._file_path, "w", encoding="utf-8") as config_file:
            if self._file_extension == "json":
                json.dump(self._config_dict, config_file, ensure_ascii=False, indent=4)
            elif self._file_extension == "ini":
                parser = configparser.ConfigParser()
                for section, values in self._config_dict.items():
                    parser[section] = values
                parser.write(config_file)

    def set(self, key: str, value: Any, section: Optional[str] = None) -> None:
        """Sets values in the config file (ini or json). Parameter section is required
        for .ini files and optional for .json files."""
        if not section and self._file_extension == "ini":
            raise KeyError("Parameter section is required at .ini files")

        if not section:
            self._config_dict[key] = value
            return

        if section not in self._config_dict:
            self._config_dict[section] = {}
        self._config_dict[section][key] = value


if __name__ == '__main__':
    with ConfigFilesContextManager("test.ini") as config:
        config.set("dark", "#000", "Themes")
        config.set("light", "#fff", "Themes")

    with ConfigFilesContextManager("test.json") as config:
        config.set("dark", "#000")
        config.set("light", "#fff")
        config.set("session_key", "key", "settings")
        config.set("port", 80, "settings")
