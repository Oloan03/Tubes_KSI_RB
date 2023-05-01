import requests
from textblob import TextBlob

API_KEY = '8bfb2dc904mshee2c9a51b060205p107242jsnf9f331655b32'

url = 'https://imdb8.p.rapidapi.com/title/get-user-reviews'


parameter = {
    'tconst': 'tt1375666',  # ID film yang akan diambil sentimennya
    'limit': '200'           # Batas jumlah review yang diambil, dikarenakan RapidAPI diakses secara gratis limit maksimal 200
}

HEADERS = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': 'imdb8.p.rapidapi.com'
}

try:
    response = requests.get(url=URL, headers=HEADERS, params=PARAMS)
    response.raise_for_status()  # memicu HTTPError jika terjadi kesalahan pada response

    # Memproses hasil response menjadi teks
    data = response.json()
    reviews = [d['reviewText'] for d in data['reviews']]

    # Analisis sentimen menggunakan TextBlob
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

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
