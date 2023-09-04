#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    # Base case: If counts is None, initialize it as an empty dictionary
    if counts is None:
        counts = {}

    # Base case: If word_list is empty, there are no more keywords to count
    if not word_list:
        # Sort the counts first by count (descending), then alphabetically (ascending)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

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

        # Extract titles from the posts and concatenate them
        titles = [post['data']['title'] for post in posts]
        title_text = ' '.join(titles)

        # Loop through the word_list and count occurrences
        keyword = word_list[0].lower()
        keyword_count = title_text.lower().count(keyword)
        if keyword_count > 0:
            # Update the counts dictionary
            counts[keyword] = counts.get(keyword, 0) + keyword_count

        # Recursively call count_words with the rest of the word_list
        count_words(subreddit, word_list[1:], data.get('data', {}).get('after'), counts)
    else:
        # If the subreddit is invalid or there was an error, print nothing
        return
