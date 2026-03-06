"""This script is designed to implement custom context manager AutomaticBackupContextManager
that context manager that creates the backup of the file before processing it.

If the processing is successful, the original file is replaced with the new one.
In case of an error, the backup is automatically restored."""
import os
import shutil


class AutomaticBackupContextManager:
    """Context manager to create backup of the file and restore the original file in
    case of error."""

    def __init__(self, file_path: str) -> None:
        """Initialize context manager with file_path parameter to create backup of the file
        and restore the original file in case of error."""
        self._file_path = file_path
        self._file_object = None
        self._backup_file_path = os.getcwd() + "/" + os.path.splitext(self._file_path)[0] + \
                                 "_backup" + os.path.splitext(self._file_path)[1]

    def __enter__(self):
        """Opens given file, creates the backup of the file and returns the file object."""
        if not os.path.exists(self._file_path):
            raise FileNotFoundError(f"File {self._file_path} does not exist")

        shutil.copy(self._file_path, self._backup_file_path)
        self._file_object = open(self._file_path, "r", encoding="utf-8")
        return self._file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restores the backup of the file in case of error and closes the file object."""
        if self._file_object:
            self._file_object.close()

        if exc_type is not None:
            os.remove(self._file_path)
            shutil.copy(self._backup_file_path, self._file_path)
            os.remove(self._backup_file_path)
        else:
            os.remove(self._backup_file_path)


if __name__ == '__main__':
    with AutomaticBackupContextManager(file_path="test.txt") as file_object:
        print(file_object.read())
        raise Exception
