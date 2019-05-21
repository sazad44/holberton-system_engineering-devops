#!/usr/bin/python3
"""top_ten function definition"""
import requests


def top_ten(subreddit):
    """top_ten method to get the top ten hot articles on a subreddit"""
    subRcheck = requests.get('https://reddit.com/api/search_reddit_names.json',
                             headers={
                                 'User-Agent': 'Safari 12.1'
                             },
                             params={
                                 'exact': True,
                                 'query': subreddit
                             })
    if 'error' in subRcheck.json().keys():
        print(None)
    else:
        response = requests.get("https://reddit.com/r/{}.json"
                                .format(subreddit),
                                headers={
                                    'User-Agent': 'Safari 12.1'
                                })
        printRange = 10
        if len(response.json().get('data').get('children')) < 10:
            printRange = len(response.json().get('data').get('children'))
        for i in range(printRange):
            print(response.json().get('data').get('children')[i].get('data')
                  .get('title'))
