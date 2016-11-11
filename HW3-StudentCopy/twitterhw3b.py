# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import nltk
import requests
import requests_oauthlib
from textblob import TextBlob
import tweepy

consumer_key = "BNZlgxYIH8nsS9BbIoRcAYHf8"
consumer_secret = "CZBxNcz9sQ6Eo0tasASUNAt2OG0g9gHuIFiuxbjWn3luCJMdxs"
access_token = "431574690-cnNepy6dYKGGXnIGRe4FlwnlW1kWEoZI1lnD4ncY"
access_token_secret = "T9jurwWB8Y9vdTJ9lKtmggJG52gRc0DccP03t3i3AKPrx"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

tweets = api.search('UMSI')

avgsubjectivity = 0
avgpolarity = 0
count = 0 

for tweet in tweets:
	print(tweet.text)
	count += 1
	analysis = TextBlob(tweet.text)
	tweetsub = analysis.subjectivity
	tweetpol = analysis.polarity
	avgsubjectivity += tweetsub
	avgpolarity += tweetpol
	print("Tweet Subjectivity Rating: ", tweetsub)
	print("Tweet Polarity Rating: ", tweetpol)


print("Average Subjectivity: ", (avgsubjectivity / count))
print("Average Polarity: ", (avgpolarity / count))
