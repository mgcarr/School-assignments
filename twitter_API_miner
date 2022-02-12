import tweepy
import json

consumer_key = 'HnYOmXHqLD4rOr7ivwzsJOKU2'
consumer_secret = 'OTWt7BXGmojafwRum4FLXFdOYr3CPVnmE2MFpdeenD3WWedQ09'
access_token = '1334961701247193088-zErNWYJM9hqPRh7pz6wkrbcfaEy6s7'
access_token_secret = 'LCiLZQMZ9XxkmMPHM4781OUuEYgmw2YTkt3CFsZ3nIRCJ'

search_terms_file_name = 'search-terms.txt'

search_terms_file = open(search_terms_file_name, 'r')

search_terms = [line.lower().strip() for line in search_terms_file.readlines()]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class SearchResultStreamListener(tweepy.StreamListener):
    file_name = 'twitter-data2.txt'

    def __init__(self):
        """Constructor"""
        self._file = open(self.file_name, 'w')

    def on_data(self, raw_data):
        self._file.write(raw_data)
        print(raw_data)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False

search_result_listener = SearchResultStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=search_result_listener)
stream.filter(track=search_terms)
