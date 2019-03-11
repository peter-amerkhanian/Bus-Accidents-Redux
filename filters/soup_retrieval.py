from bs4 import BeautifulSoup
import requests
from filters import get_stories
import pickle


def get_soup(last_page):
    for x in range(1, last_page+1):
        page = requests.get(f"https://www.elcomercio.com/search/bus%20accidente%20ecuador/{x}")
        soup = BeautifulSoup(page.content, "html.parser")
        yield soup


list_of_articles = []
for soup in list(get_soup(10)):
    list_of_articles.extend(list(get_stories(soup)))
with open('articles.pickle', 'wb') as f:
    pickle.dump(list_of_articles, f)