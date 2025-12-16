"""
HTTP Service for making requests to the Hogwarts API.
"""
from typing import Any
import requests
from lib.utils.EnvironmentVariables import EnvironmentVariables

env = EnvironmentVariables()

def get_spells() -> Any | None:
    """
    Makes a GET request to the Hogwarts API to retrieve spells.

    Returns:
        dict: The JSON response from the API.
    """
    endpoint = env.get_hogwarts_api_spells_path()
    if endpoint:
        return _get(endpoint)
    else:
        print(f"An error occurred: {endpoint} not valid.")
        return None


def _get(endpoint: str, language: str = env.get_hogwarts_api_lang()) -> Any | None:
    """
    Makes a GET request to the Hogwarts API.

    Args:
        endpoint (str): The endpoint to make the request to.
        language (str, optional): The language of the response. Defaults to 'en'.

    Returns:
        dict: The JSON response from the API.
    """

    # Get the base URL from the environment variables
    base_url = env.get_hogwarts_api_host()

    try:
        # Make the GET request to the API
        response = requests.get(base_url + '/' + language + '/' + endpoint)

        # Check if the response was successful
        response.raise_for_status()

        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return None
