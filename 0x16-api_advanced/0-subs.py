#!/usr/bin/python3
"""
        Uses the reddit api to return the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    else:
        data = response.json().get("data")
        num_subs = data.get("subsrcibers")
        return num_subs
