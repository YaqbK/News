import requests

API_KEY = 'e6dd1a095f3e496fa0de39c85d2017e0'

URL = 'https://newsapi.org/v2/top-headlines?'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortby": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

#ef get_articles_by_query(query):


def _get_articles(parameters):
    response = requests.get(URL, params=parameters)

    articles = response.json("articles")

    results = []

    for article in articles:
        results.append()
