"""
HTTP Service for making requests to the Hogwarts API.
"""
from typing import Any
import requests, json
from lib.utils.EnvironmentVariables import EnvironmentVariables

env = EnvironmentVariables()

def get_spells() -> Any | None:
    """
    Makes a GET request to the Hogwarts API to retrieve spells.

    Returns:
        dict: The JSON response from the API or local file with the same data.
    """
    spells = _get()
    if spells is None:
        with open('static/en_spells_v2.json') as json_file:
            return json.load(json_file)
    return None


def _get(base_url: str = env.get_hogwarts_api_host(), endpoint: str =env.get_hogwarts_api_spells_path(), language: str = 'en') -> Any | None:
    """
    Makes a GET request to the Hogwarts API.

    Args:
        base_url (str): The base URL of the API.
        endpoint (str): The endpoint to make the request to.
        language (str, optional): The language of the response. Defaults to 'en'.

    Returns:
        dict: The JSON response from the API.
    """

    if base_url and endpoint:
        try:
            # Make the GET request to the API
            response = requests.get(base_url + '/' + language + '/' + endpoint)

            # Check if the response was successful
            response.raise_for_status()

            # Return the JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            # print(f"An error occurred: {e}")
            return None
    return None
