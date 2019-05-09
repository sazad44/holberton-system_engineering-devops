#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Get number of subreddit subscribers"""
    response = requests.get("https://reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={'User-Agent': 'Safari 12.1'})
    if response.json().get('data').get('subscribers') is None:
        return 0
    else:
        return response.json().get('data').get('subscribers')
