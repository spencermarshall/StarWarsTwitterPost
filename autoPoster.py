import os
import random
import time
import tweepy
from dotenv import load_dotenv

from subpackage.CloneWarsQuotes import getCloneWarsQuote


class TwitterPoster:
    def __init__(self):
        load_dotenv()
        bearer_token = os.getenv('bearer_token')
        API_KEY = os.getenv('API_KEY')
        API_SECRET_KEY = os.getenv('API_SECRET_KEY')
        access_token = os.getenv('access_token')
        access_token_secret = os.getenv('access_token_secret')

        self.client = tweepy.Client(bearer_token = bearer_token,
                                        consumer_key = API_KEY, consumer_secret = API_SECRET_KEY,
                                        access_token = access_token, access_token_secret = access_token_secret)
    def randomAddSpace(self, text):
        if random.random() < 0.5:
            return " " + text
        else:
            return text

    def postCWQuote(self):
        finalTweet = getCloneWarsQuote(self) + " #StarWars #TheCloneWars #TheAcolyte #StarWarsQuotes #swtwt"
        finalTweet = self.randomAddSpace(finalTweet)
        try:
            # Post the tweet usin g the Client
            # response = self.client.create_tweet(text=finalTweet)
            ok = 3
        except Exception as e:
            print(f"An error occurred: {e}")



# Example usage
if __name__ == "__main__":
    # random wait time, 0-24 minutes
    time.sleep(random.randint(0, 60 * 24))
    poster = TwitterPoster()
    poster.postCWQuote()