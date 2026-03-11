"""Module provides WebService class to obtain data from the given website."""
import requests
from typing import Dict


class WebService:
    """Class that represents WebService to obtain data from the given website.

    Public methods:
        get_data(): returns data from website
    """

    @staticmethod
    def get_data(url: str) -> Dict:
        """Returns data from the given website in json format."""
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()
        raise Exception(f"Request failed with status code: {req.status_code}")
