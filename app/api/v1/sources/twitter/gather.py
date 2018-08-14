import tweepy

from app import app, consumer_key, consumer_secret, api_key, api_secret
from ...assets.error_handlers import custom_response
from ...assets.response import CODES, MIME_TYPES


class TwitterClass:

    # twitter API credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(api_key, api_secret)
    twitter = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def __init__(self, topic):
        self.topic = topic

    def search(self):
        try:
            cursor = tweepy.Cursor(self.twitter.search, q=self.topic, lang='en').items()
            for item in cursor:
                tweet = item._json
                print(tweet)
        except Exception as error:
            app.logger.info("Error occurred while gathering data from twitter.")
            app.logger.exception(error)
            return custom_response("Database connection error.", CODES.get('INTERNAL_SERVER_ERROR'),
                                   MIME_TYPES.get('APPLICATION_JSON'))


TwitterClass("pakistan").search()
