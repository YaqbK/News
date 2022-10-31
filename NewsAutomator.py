import requests
from sys import argv

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

# def get_articles_by_query(query):


def _get_articles(parameters):
    response = requests.get(URL, params=parameters)

    articles = response.json()["articles"]

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result["title"])
        print(result["url"])
        print('')

# def get_sources_by_category(category):


if __name__ == "__main__":
    print(f"Getting news for {argv[1]}...\n")
    get_articles_by_category(argv[1])
    print(f"Succesfully retrieved top {argv[1]} headlines")
