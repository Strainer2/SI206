# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy
import nltk
import requests
import requests_oauthlib

consumer_key = "BNZlgxYIH8nsS9BbIoRcAYHf8"
consumer_secret = "CZBxNcz9sQ6Eo0tasASUNAt2OG0g9gHuIFiuxbjWn3luCJMdxs"
access_token = "431574690-cnNepy6dYKGGXnIGRe4FlwnlW1kWEoZI1lnD4ncY"
access_token_secret = "T9jurwWB8Y9vdTJ9lKtmggJG52gRc0DccP03t3i3AKPrx"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

newapi = tweepy.API(auth)
img = "/Users/JBone/documents/cool.jpg" 
print("Posting...")
newapi.update_with_media(img, status="#UMSI-206 #Proj3")
print("Posted")
