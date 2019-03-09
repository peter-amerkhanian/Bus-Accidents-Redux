from bs4 import BeautifulSoup
import requests


def get_soup(last_page):
    for x in range(1, last_page+1):
        page = requests.get(f"https://www.elcomercio.com/search/bus%20accidente%20ecuador/{x}")
        soup = BeautifulSoup(page.content, "html.parser")
        yield soup
