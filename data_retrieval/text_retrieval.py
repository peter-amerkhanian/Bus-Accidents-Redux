from newspaper import Article
from bs4 import BeautifulSoup
from collections import namedtuple
from dateparser import parse
from data_retrieval import fatal_keywords
from data_retrieval.Story import Story


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
        temp_story = None
        for keyword in fatal_keywords:
            if keyword in title:
                article_object = Article(url=url, language='es')
                article_object.download()
                article_soup = BeautifulSoup(article_object.html, "html.parser")
                bold_words = [bold.text for bold in article_soup.findAll("b")]
                article_object.parse()
                full_text = article_object.text
                temp_story = Story(url, date, title, summary, full_text, bold_words)
                break
        if temp_story:
            yield temp_story
