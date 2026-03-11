"""Module is designed for testing the UserManager class using pytest."""
import pytest
from user_manager import UserManager

users_count = 0


@pytest.fixture
def user_manager() -> UserManager:
    """Fixture that returns UserManager with two pre-added users."""
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)

    global users_count
    users_count += 2
    return um


@pytest.mark.parametrize(("name", "age"), [("Anna", 26), ("Jack", 29)])
def test_add_user_success(user_manager: UserManager, name: str, age: int) -> None:
    """Adds еру new user and checks it appears in the users list."""
    user_manager.add_user(name, age)
    users = user_manager.get_all_users()
    assert {'name': name, 'age': age} in users


@pytest.mark.parametrize(("name", "age"), [("Anna", 26), ("Jack", 29)])
def test_add_user_in_the_end(user_manager: UserManager, name: str, age: int) -> None:
    """Adds a new user and checks it appears at the end of the users list."""
    user_manager.add_user(name, age)
    users = user_manager.get_all_users()
    index = len(users) - 1
    assert users[index]['name'] == name and users[index]['age'] == age


@pytest.mark.parametrize(("name", "age"), [("Alice", 30), ("Bob", 25)])
def test_add_existing_user_fail(user_manager: UserManager, name: str, age: int) -> None:
    """Checks that adding the existing user raises a ValueError."""
    with pytest.raises(ValueError):
        user_manager.add_user(name, age)


@pytest.mark.parametrize(("name", "age"), [("Alice", "30"), (11, 25), (1, "2")])
def test_add_user_type_fail(user_manager: UserManager, name: str | int, age: str | int) -> None:
    """Checks that adding the user with wrong type of data raises a TypeError."""
    with pytest.raises(TypeError):
        user_manager.add_user(name, age)


@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_remove_user_success(user_manager: UserManager, name: str) -> None:
    """Checks that removing the existing user removes the user from the users list."""
    user_manager.remove_user(name)
    users = user_manager.get_all_users()
    assert all(user["name"] != name for user in users)


@pytest.mark.parametrize("name", ["Anna", "Jack", ""])
def test_remove_not_existing_user_fail(user_manager: UserManager, name: str) -> None:
    """Checks that removing the non-existing user raises a ValueError."""
    with pytest.raises(ValueError):
        user_manager.remove_user(name)


@pytest.mark.parametrize("name", [30, (11, 25), []])
def test_remove_user_type_fail(user_manager: UserManager, name: int | tuple | list) -> None:
    """Checks that removing the user with wrong type of data raises a TypeError."""
    with pytest.raises(TypeError):
        user_manager.remove_user(name)


def test_get_all_users_len(user_manager: UserManager) -> None:
    """Checks that get_all_users returned the correct number of users."""
    users = user_manager.get_all_users()
    assert len(users) == 2


def test_get_all_users_success(user_manager: UserManager) -> None:
    """Checks that get_all_users returns the correct list of users."""
    users = user_manager.get_all_users()
    expected_users = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    assert users == expected_users


def test_get_all_users_empty(user_manager: UserManager) -> None:
    """Skips the test if users list is not empty; otherwise checks that the list is empty."""
    if len(user_manager.get_all_users()) != 0:
        pytest.skip("Users found")
    assert not user_manager.get_all_users()


@pytest.mark.skipif(users_count < 3, reason="Not enough users")
def test_get_all_users_skip(user_manager: UserManager) -> None:
    """Skips the test if users_count < 3; otherwise checks that the list is not empty."""
    assert user_manager.get_all_users()
