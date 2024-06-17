#!/usr/bin/python3
"""
Script to query number of subscribers on a given Reddit subreddit.
"""

import requests
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return 0
    
    try:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (ValueError, KeyError) as e:
        logging.error(f"Failed to parse JSON response: {e}")
        return 0

if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    if subscribers:
        logging.info(f"The subreddit '{subreddit}' has {subscribers} subscribers.")
    else:
        logging.info(f"Could not retrieve the number of subscribers for subreddit '{subreddit}'.")

