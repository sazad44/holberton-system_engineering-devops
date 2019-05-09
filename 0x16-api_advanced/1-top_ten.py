#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """top_ten method to get the top ten hot articles on a subreddit"""
    respAbout = requests.get('https://reddit.com/r/{}/about.json'
                             .format(subreddit),
                             headers={'User-Agent': 'Safari 12.1'})
    response = requests.get("https://reddit.com/r/{}.json"
                            .format(subreddit),
                            headers={'User-Agent': 'Safari 12.1'})
    if respAbout.json().get('data').get('subscribers') is None:
        print (None)
    else:
        printRange = 10
        if len(response.json().get('data').get('children')) < 10:
            printRange = len(response.json().get('data').get('children'))
        for i in range(printRange):
            print(response.json().get('data').get('children')[i].get('data')
                  .get('title'))
