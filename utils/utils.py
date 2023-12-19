import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter

num_tweets = 100

scrapper = sntwitter.TwitterSearchScraper('#python #run')
tweet_list = []
for i,tweets in enumerate(scrapper.get_items()):
    data = [tweets.date, 
            tweets.id,
            tweets.contents,
            tweets.user.username,
            tweets.likeCount,
            tweets.retweetCount]
    tweet_list.append(data)
    if i > num_tweets:
        break

tweet_df = pd.DataFrame(tweet_list, columns = ['DATE','ID','CONTENT','USERNAME','LIKECOUNT','RETWEET_COUNT'])
tweet_df