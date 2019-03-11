from bs4 import BeautifulSoup
import requests
from filters import get_stories
import pickle


def get_soup(last_page):
    for x in range(1, last_page+1):
        page = requests.get(f"https://www.elcomercio.com/search/bus%20accidente%20ecuador/{x}")
        page_soup = BeautifulSoup(page.content, "html.parser")
        yield page_soup


# list_of_articles = []
# for soup in get_soup(10):
#     list_of_articles.extend(get_stories(soup))
list_of_articles = [get_stories(soup) for soup in get_soup(10)]
with open('articles.pickle', 'wb') as f:
    pickle.dump(list_of_articles, f)