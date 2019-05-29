#!/usr/bin/python3
"""Recurse function definition"""
import requests


def count_words(subreddit, word_list):
    """count_words function to return printed word counts"""
    countDict = word_count(subreddit, word_list)
    for key in [v[0] for v in
                sorted(countDict.items(), key=lambda kv: (-kv[1], kv[0]))]:
        if countDict[key] > 0:
            print("{}: {}".format(key, countDict[key]))


def word_count(subreddit, word_list, after=None, countDict={}):
    """
    Recurse function recursively produces a list of all hot articles
    on a subreddit
    """
    subRcheck = requests.get("https://reddit.com/api/search_reddit_names.json",
                             headers={
                                 'User-Agent': 'Safari 12.1'
                             },
                             params={
                                 'exact': True,
                                 'query': subreddit
                             })
    if 'error' in subRcheck.json().keys():
        pass
    response = requests.get("https://reddit.com/r/{}.json"
                            .format(subreddit),
                            headers={
                                'User-Agent': 'Safari 12.1'
                            },
                            params={
                                'after': after
                            })
    """Create dictionary for count record"""
    for child in response.json().get('data').get('children'):
        for word in child.get('data').get('title').split():
            for wordList in word_list:
                if wordList not in countDict.keys():
                    countDict[wordList] = 0
                if word.upper() == wordList.upper():
                    countDict[wordList] += 1
    if response.json().get('data').get('after') is None:
        return countDict
    return word_count(subreddit,
                      word_list,
                      response.json().get('data').get('after'),
                      countDict)
