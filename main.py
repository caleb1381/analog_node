from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import re

mydata = pd.read_csv("diverse_tweets.csv")
print(mydata.head(50))


# def clean_text(text):
#     text = re.sub('@[A-Za-z0-9_]+', '', text)  # Remove @mentions
#     text = re.sub('https?://[A-Za-z0-9./]+', '', text)  # Remove URLs
#     text = re.sub('[^a-zA-Z]', ' ', text)  # Remove non-alphabetic characters
#     text = text.lower()  # Convert to lowercase
#     text = word_tokenize(text)  # Tokenization
#     text = [word for word in text if word not in set(stopwords.words('english'))]  # Remove stopwords
#     stemmer = PorterStemmer()
#     text = [stemmer.stem(word) for word in text]  # Stemming
#     return ' '.join(text)


# def get_tweet_sentiment(tweet):
#     # create TextBlob object of passed tweet text
#     analysis = TextBlob(tweet)
#     # set sentiment
#     if analysis.sentiment.polarity > 0:
#         return 'positive'
#     elif analysis.sentiment.polarity == 0:
#         return 'neutral'
#     else:
#         return 'negative'


# df = pd.read_csv("diverse_tweets.csv")
# fetched_tweets = df["source_article"].to_list()

# tweets = []
# positive = 0
# neutral = 0
# negative = 0

# for tweet in fetched_tweets:
#     sentiment = get_tweet_sentiment(clean_text(tweet))
#     if sentiment == 'positive':
#         positive += 1
#     elif sentiment == 'neutral':
#         neutral += 1
#     else:
#         negative += 1

# tweets.append(positive)
# tweets.append(neutral)
# tweets.append(negative)

# print(tweets)
# names = ["positive","neutral","negative"]

# plt.figure(figsize=(6, 6))
# plt.bar(names, tweets, color=['g','b','r'])

# plt.title("Sentiment Analysis of Twitter Data on 'End SARS'")
# plt.xlabel("x axis - types of sentiments", fontweight='bold', fontsize=15)
# plt.ylabel("y axis - twitter data", fontweight='bold', fontsize=15)

# plt.show()


# # for tweet in fetched_tweets:
# #     parsed_tweet = {}
# #     parsed_tweet['text'] = tweet
# #     parsed_tweet['sentiment'] = get_tweet_sentiment(clean_text(tweet))
# #     if parsed_tweet not in tweets:
# #         tweets.append(parsed_tweet)
