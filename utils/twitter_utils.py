import pandas as pd
import requests


tweets_to_collecct = 2500
scraper_api = 'dfdd0aad1c1fd832761a65f63059733e'
query = 'data science, artificial inteligence'


twitter_data = []
payload  ={
    'api_key':f'{scraper_api}',
    'query': f'{query}',
    'num': f'{tweets_to_collecct}'
}
response = requests.get(
    'https://api.scraperapi.com/structured/twitter/search', params= payload
)
data = response.json()

all_tweets = data['organic_results']
for tweet in all_tweets:
    twitter_data.append(tweet)

df = pd.DataFrame(twitter_data)
df.to_csv('tweets.csv')