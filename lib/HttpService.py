from typing import Any

import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get(endpoint: str, language: str = 'en') -> Any | None:
    """
    Makes a GET request to the Hogwarts API.

    Args:
        endpoint (str): The endpoint to make the request to.
        language (str, optional): The language of the response. Defaults to 'en'.

    Returns:
        dict: The JSON response from the API.
    """

    # Get the base URL from the environment variables
    base_url = os.getenv('HOGWARTS_API_HOST')

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
