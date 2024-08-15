#!/usr/bin/python3
"""A recrsive function to return a list of titles"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """A list of hot titles"""
    url = "https://www.reddit.com/{}/r/hot.json".format(subreddit)
    data = {
            "after": after,
            "count": count,
            "limit": 100
    }
    response = requests.get(url, params=data, allow_redirects=False)
    if response.status_code == 404:
        return None

    data_dict = response.json().get("data")
    after = data_dict.get("after")
    count += data_dict.get("dist")
    data_list = data_dict["children"]
    for title in data_list:
        hot_list.append(title.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list=[], after="", count=0)
    """Return the results of the previous page"""
    return hot_list


