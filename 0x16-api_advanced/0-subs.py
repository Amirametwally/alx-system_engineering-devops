#!/usr/bin/python3
"""function that queries the Reddit API and returns
the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if (not response.ok):
        return 0
    count = response.json().get('data').get('subscribers')
    return count
