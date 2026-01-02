"""This module is designed for storing user settings such as theme, language and notifications."""

from typing import Callable


def create_user_settings() -> tuple[
    Callable[[str, str, bool], None], Callable[[], dict[str, str | bool]]
]:
    """Function to create the user settings."""
    user_settings: dict[str, str | bool] = {
        "theme": "",
        "language": "",
        "notifications": False
    }

    def store_user_settings(theme: str, language: str, notifications: bool) -> None:
        """Function to store the user settings."""
        user_settings["theme"] = theme
        user_settings["language"] = language
        user_settings["notifications"] = notifications

    def get_user_settings() -> dict[str, str | bool]:
        """Function to get the user settings."""
        return user_settings

    return store_user_settings, get_user_settings


store_settings, get_settings = create_user_settings()
store_settings("dark", "english", True)
actual_theme, actual_language, actual_notifications = get_settings()

print(f"Theme: {actual_theme}\nLanguage: {actual_language}\nNotifications: {actual_notifications}")
