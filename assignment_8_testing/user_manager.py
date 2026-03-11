"""Module provides UserManager class for working with user data."""


class UserManager:
    """Class for managing users data.

    Public methods:
        add_user(): adds user to users list
        remove_user(): removes user from users list
        get_all_users(): returns list of all users in users list
    """

    def __init__(self) -> None:
        """Initializes user manager."""
        self._users = []

    def add_user(self, name: str, age: int) -> None:
        """Adds user to users list."""
        if not isinstance(name, str) or not isinstance(age, int):
            raise TypeError('Name must be a string and age must be a integer')

        for user in self._users:
            if user['name'] == name and user['age'] == age:
                raise ValueError(f'User {name} already exists')
        self._users.append({'name': name, 'age': age})

    def remove_user(self, name: str) -> None:
        """Removes user from users list."""
        if not isinstance(name, str):
            raise TypeError('Name must be a string')

        for user in self._users:
            if user['name'] == name:
                self._users.remove(user)
                return

        raise ValueError(f'User {name} not found')

    def get_all_users(self) -> list[dict]:
        """Returns list of all users in users list."""
        return self._users
