#!/usr/bin/python3
"""Prints the titles of the 10 hot posts"""

import requests


def top_ten(subreddit):
    """A function to print 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False).json()
    if subreddit is None:
        return None
    data_list = response["data"]["children"]
    for title in data:
        print(title.get("data").get("title"))
