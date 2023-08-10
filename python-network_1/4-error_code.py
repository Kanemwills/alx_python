#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""

import requests
import sys

def main():
    url = input("Enter the URL: ")

    try:
        response = requests.get(url)
        response_body = response.text

        print("Response body:")
        print(response_body)

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
