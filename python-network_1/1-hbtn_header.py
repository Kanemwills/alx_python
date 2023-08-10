#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""

import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id is not None:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
