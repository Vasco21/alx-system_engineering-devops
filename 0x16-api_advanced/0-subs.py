#!/usr/bin/python3
"""
the number_of_subscribers function, which takes a subreddit name as input, sends a GET request to the Reddit API to retrieve information about the subreddit, and then extracts the number of subscribers from the JSON response. If the subreddit is invalid or there is an error, it returns 0.
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
