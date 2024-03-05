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

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0
