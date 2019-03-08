from newspaper import Article
from bs4 import BeautifulSoup
import requests
from collections import namedtuple
from dateparser import parse
from text_filtering import get_time, get_date
from misc_helpers import fatal_keywords
import pickle

page = requests.get("https://www.elcomercio.com/search/?query=bus%20accidente%20ecuador")
soup = BeautifulSoup(page.content, "html.parser")
Story = namedtuple('Story', 'url date title summary article')


def get_stories(soup):
    """
    a generator that yields each story from el commercio
    :param soup: BeautifulSoup object
    :return: named-tuple
    """
    for article in soup.findAll("div", {"class": "two-cols-article"}):
        url = "https://www.elcomercio.com" + article.find("a", {"class": "title"}).get("href")
        date = parse(article.find("div", {"class": "publishDate"}).span.text, languages=["es"])
        title = article.find("a", {"class": "title"}).text.strip()
        summary = article.find("div", {"class": "epigraph"}).text.strip()
        for keyword in fatal_keywords:
            if keyword in title + " " + summary:
                article_object = Article(url=url, language='es')
                article_object.download()
                article_object.parse()
                temp_story = Story(url, date, title, summary, article_object.text)
                break
            else:
                temp_story = None
        if temp_story:
            yield temp_story


with open("articles.pickle", "rb") as f:
    temp_data = pickle.load(f)

for story in temp_data:
    print(story.title, story.summary)
    print(story.date)
    get_date(story)
    get_time(story)
    print("\n")
