#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API
    """
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if not response.ok:
        return 0
    subscriber_count = response.json().get("data").get("subscribers")
    return subscriber_count
