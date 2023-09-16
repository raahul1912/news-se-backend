import os
import requests

# news api: https://gnews.io/user

def fetch_news(search_term, number_of_results):
  apikey = os.getenv('NEWS_API_KEY')
  url = f"https://gnews.io/api/v4/search?q={search_term}&lang=en&country=us&max={number_of_results}&apikey={apikey}"
  response = requests.get(url)
  if response.status_code == 200:
			data = response.json()
			articles = data.get('articles')
			articles = [
					{'content': article.get('content'), 'title': article.get('title'), 'url': article.get('url'), 'image': article.get('image')} for article in articles
			]
			return articles
