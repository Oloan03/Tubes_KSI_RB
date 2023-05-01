import requests
from textblob import TextBlob

url = 'https://imdb8.p.rapidapi.com/title/get-user-reviews'
params = {
    'tconst': 'tt0944947',  # ID film yang akan diambil sentimennya
    'limit': '200'           # Batas jumlah review yang diambil, dikarenakan limit dari rapidapi gratis hanya 200
}

headers = {
    'x-rapidapi-key': '8bfb2dc904mshee2c9a51b060205p107242jsnf9f331655b32',
    'x-rapidapi-host': 'imdb8.p.rapidapi.com'
}

response = requests.get(url=url, headers=headers, params=params)

data = response.json()
reviews = [d['reviewText'] for d in data['reviews']]

positive_reviews = []
negative_reviews = []
neutral_reviews = []
for review in reviews:
    sentiment = TextBlob(review).sentiment.polarity
    if sentiment > 0:
        positive_reviews.append(review)
    elif sentiment < 0:
        negative_reviews.append(review)
    else:
        neutral_reviews.append(review)


print(f'Jumlah review positif: {len(positive_reviews)}')
print(f'Jumlah review negatif: {len(negative_reviews)}')
print(f'Jumlah review netral: {len(neutral_reviews)}')
