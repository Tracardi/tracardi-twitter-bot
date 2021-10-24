import asyncio
import tweepy
from tracardi_twitter_bot.model.model import TwitterCredentials


class TwitterClient:
    def __init__(self, credentials: TwitterCredentials):
        self.credentials = credentials
        auth = tweepy.OAuthHandler(
            self.credentials.consumer_key,
            self.credentials.consumer_secret
        )
        auth.set_access_token(
            self.credentials.access_token,
            self.credentials.access_token_secret
        )
        self.api = tweepy.API(auth)
        self.api.verify_credentials()

    async def auto_follow_followers(self):
        for follower in self.api.get_followers():  # type: User
            if not follower.following:
                follower.follow()
                await asyncio.sleep(0)
                # todo yield followed screen_Names

    async def like_all_mentions(self):
        tweets = self.api.mentions_timeline()
        for tweet in tweets:  # type: Status
            if not tweet.favorited:
                tweet.favorite()
                await asyncio.sleep(0)
                # todo yield list of texts and users
                print(tweet.text)