#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data'].get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None
    else:
        return None
