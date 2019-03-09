from newspaper import Article
from bs4 import BeautifulSoup
from collections import namedtuple
from dateparser import parse
from text_filtering import get_time, get_date, get_route, get_deaths
from misc_helpers import fatal_keywords
import pickle


Story = namedtuple('Story', 'url date title summary article keywords')


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


# TO DO: Get the deaths to cross reference with numbers
if __name__ == '__main__':
    with open("articles.pickle", "rb") as f:
        temp_data = pickle.load(f)

    for story in temp_data:
        print(f"Story title: {story.title}\nStory Summary: {story.summary}")
        print(f"Story pub date: {story.date}")
        print(f"Accident date: {get_date(story)}")
        print(f"Accident time: {get_time(story)}")
        print(f"Accident route: {get_route(story)}")
        print(f"Deaths: {get_deaths(story)}")
        print("\n")
