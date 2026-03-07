"""This module is designed to implement function that stores the given webpage in separate file."""
from urllib.parse import urlparse
import requests


def store_web_page(url: str) -> None:
    """Loads the web page and stores the  content of given webpage in the separate file."""
    get_request = requests.get(url, timeout=5)
    if get_request.status_code != 200:
        raise requests.exceptions.RequestException(f"The web page at {url} is unavailable.")
    parsed_uri = urlparse(url)
    file_name = f"{parsed_uri.netloc}.txt"
    with open(file_name, "w+", encoding="utf-8") as text_file:
        text_file.write(get_request.text.strip())


if __name__ == '__main__':
    try:
        store_web_page('https://github.com')
    except requests.exceptions.RequestException as exception:
        print(f"Error: {exception}")
