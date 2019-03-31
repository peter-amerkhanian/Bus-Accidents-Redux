from bs4 import BeautifulSoup
import requests
from data_processing.data_retrieval import get_stories
import pickle


def get_soup(last_page):
    for x in range(1, last_page+1):
        page = requests.get(f"https://www.elcomercio.com/search/bus%20accidente%20ecuador/{x}")
        page_soup = BeautifulSoup(page.content, "html.parser")
        yield page_soup


def pickle_soup(pages):
    list_of_articles = []
    for soup in get_soup(pages):
        list_of_articles.extend(get_stories(soup))
    with open('data_processing/data_retrieval/articles.pickle', 'wb') as f:
        pickle.dump(list_of_articles, f)

