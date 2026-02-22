from newsapi import NewsApiClient
import os

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def get_news(query):
    return newsapi.get_everything(q=query, language="en", page_size=5)
