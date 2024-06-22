import requests
from sys import argv

API_KEY = ''

URL = 'https://newsapi.org/v2/top-headlines?'


def get_articles_by_category(country, category):
    query_parameters = {
        "category": category,
        "sortby": "top",
        "country": country,
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
    print(f"Getting news from {argv[1]}...\n")
    field = input("Choose category:\nbusiness\nentertainment\ngeneral\nhealth\nscience\nsports\ntechnology\n").lower()
    get_articles_by_category(argv[1], field)
    print(f"Succesfully retrieved top {argv[1]} headlines")


