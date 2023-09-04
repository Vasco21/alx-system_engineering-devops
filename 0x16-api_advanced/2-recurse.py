#!/usr/bin/python3
"""
Querying the Reddit API recursively
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    # Base case: If hot_list is None, initialize it as an empty list
    if hot_list is None:
        hot_list = []

    # Define the Reddit API URL for the given subreddit and after parameter
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Extract titles from the posts and add them to the hot_list
        titles = [post['data']['title'] for post in posts]
        hot_list.extend(titles)

        # Get the 'after' parameter for pagination
        after = data.get('data', {}).get('after')

        # If there's an 'after' parameter, recursively call recurse with it
        if after:
            recurse(subreddit, hot_list, after)
        else:
            # If there's no 'after' parameter, we've fetched all pages
            return hot_list
    else:
        # If the subreddit is invalid or there was an error, return None
        return None

