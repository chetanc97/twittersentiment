import tweepy
from textblob import TextBlob

consumer_key = "bbIid5eJDDPBVeM30I4arMR4G"
consumer_secret = "dusmaNlRdWouDss30CZpfXNCB8BB9fs5CKW3avUcUpAz6FK6KE"

access_token = "701659684776730625-Zn3TRlEVDJJlwSo9aNwzWDkLpCAswg6"
access_token_secret = "xvq01wfyEkMcA4OcO9Hl3PfFIaRkNG1AKHhqDdsJZiqKS"

auth = tweepy.OAuthHandler(consumer_key ,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


#     analysis =  TextBlob(tweet.text)
#     print(analysis.sentiment)

api =  tweepy.API(auth)

twewets =  api.search("Mumbai")

for tweet  in twewets :
    print("\n")
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
