#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

def main():
    letter = input("Enter a letter: ")
    url = "http://0.0.0.0:5000/search_user"

    params = {'q': letter}

    try:
        response = requests.post(url, data=params)
        response_data = response.json()

        if isinstance(response_data, dict) and 'id' in response_data and 'name' in response_data:
            print(f"[{response_data['id']}] {response_data['name']}")
        elif isinstance(response_data, list) and len(response_data) > 0:
            print(f"[{response_data[0]['id']}] {response_data[0]['name']}")
        elif response_data == {}:
            print("No result")
        else:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
