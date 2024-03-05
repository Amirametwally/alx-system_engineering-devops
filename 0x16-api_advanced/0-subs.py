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
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
