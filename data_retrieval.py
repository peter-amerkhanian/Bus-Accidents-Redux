from newspaper import Article
from bs4 import BeautifulSoup
import requests
from collections import namedtuple
from dateparser import parse
from text_filtering import get_time, get_date
from misc_helpers import fatal_keywords

page = requests.get("https://www.elcomercio.com/search/?query=bus%20accidente%20ecuador")
soup = BeautifulSoup(page.content, "html.parser")


def get_stories(soup):
    """

    :param soup:
    :return:
    """
    Story = namedtuple('Story', 'url date title summary article')
    for article in soup.findAll("div", {"class": "two-cols-article"}):
        url = "https://www.elcomercio.com" + article.find("a", {"class":"title"}).get("href")
        date = parse(article.find("div", {"class": "publishDate"}).span.text, languages=["es"])
        title = article.find("a", {"class":"title"}).text.strip()
        summary = article.find("div", {"class":"epigraph"}).text.strip()
        for keyword in fatal_keywords:
            if keyword in title + " " + summary:
                article_object = Article(url=url, language='es')
                article_object.download()
                article_object.parse()
                temp_story = Story(url, date, title, summary, article_object)
                break
            else:
                temp_story = None
        if temp_story:
            yield temp_story


for story in get_stories(soup):
    print(story.title, story.summary)
    print(story.date)
    get_date(story)
    get_time(story)
    print("\n")
