#!/usr/bin/python3
"""Write a function that queries a reddit api"""

import requests


def number_of_subscribers(subreddit):
    """Total number of subscribers"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        sub_count = data["data"]["subscribers"]
        return sub_count
    else:
        return 0
