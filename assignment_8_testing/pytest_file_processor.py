"""Module is designed for test FileProcessor class"""
from pathlib import Path

import pytest

from assignment_8_testing.file_processor import FileProcessor


@pytest.fixture
def file_processor() -> FileProcessor:
    """
    Fixture to initialize FileProcessor class for further tests.
    :return: instance of FileProcessor class
    """
    return FileProcessor()


@pytest.fixture
def file_path(tmp_path: Path, file_processor: FileProcessor) -> str:
    """
    Fixture to create temporary filepath and write simple data to the file for further tests.
    :param tmp_path: fixture to create temporary file (instance of Path)
    :param file_processor: instance of FileProcessor class
    :return: path to temporary file (string)
    """
    file_path = str(tmp_path / "testfile.txt")
    file_processor.write_to_file(file_path, "Hello, World!")
    return file_path


def test_read_file_existing_file(file_processor: FileProcessor, file_path: str) -> None:
    """
    Tets read_from_file method of FileProcessor class for correct reading
    data from the existing file
    :param file_processor: instance of FileProcessor class
    :param file_path: path to file
    """
    data = file_processor.read_from_file(file_path)
    assert data == "Hello, World!"


def test_read_file_file_not_found(file_processor: FileProcessor) -> None:
    """
    Tets read_from_file method of FileProcessor class for raises exception
    with reading not existing file
    :param file_processor: instance of FileProcessor class
    """
    with pytest.raises(FileNotFoundError):
        file_processor.read_from_file("test_file.txt")


@pytest.mark.parametrize("short_data", ("",
                                        "abc def ghi jkl mno '§ $%& /() tuv wxyz ABC DEF"))
def test_write_to_file_success(file_processor: FileProcessor, file_path: str,
                               short_data: str) -> None:
    """
    Tests write_to_file method of FileProcessor class for correct writing data to the file
    :param file_processor: instance of FileProcessor class
    :param file_path: path to file (string)
    :param short_data: simple string or empty string to write to file
    """
    file_processor.write_to_file(file_path, short_data)
    data = file_processor.read_from_file(file_path)
    assert data == short_data


@pytest.mark.parametrize("large_data",
                         ("Data" * 100_000, "Data" * 1_000_000))
def test_write_and_read_large_file(file_processor: FileProcessor,
                                   file_path: str, large_data: str) -> None:
    """
    Tests write_to_file and read_from_file methods of FileProcessor class
    for correct writing and reading large data
    :param file_processor: instance of FileProcessor class
    :param file_path: path to file (string)
    :param large_data: example large string to write to file
    """
    file_processor.write_to_file(file_path, large_data)
    data = file_processor.read_from_file(file_path)
    assert data == large_data
