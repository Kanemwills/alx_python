#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""

import requests

def main():
    url = "https://intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        response_data = response.json()

        print("Body response:")
        print(f"\t- type: {response_data['__class__']}")
        print(f"\t- content: {response_data['content']}")
        print(f"\t- utf8 content: {response_data['utf8content']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


