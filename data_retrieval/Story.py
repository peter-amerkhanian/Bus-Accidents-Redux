from data_retrieval import get_date, get_time, get_deaths, get_route
from data_retrieval.helpers import make_clickable, translate_time
from datetime import datetime


class Story:
    def __init__(self, url, date, title, summary, article, keywords):
        self.url = url
        self.date = date
        self.title = title
        self.summary = summary
        self.article = article
        self.keywords = keywords
        self.accident_date = None
        self.accident_time = None
        self.route = None
        self.deaths = None
        self.review_status = None

    def __repr__(self):
        return f"Story title: {self.title}\nStory Summary: {self.summary}" \
            f"\nStory url:{self.url}\nStory pub date: {self.date}" \
            f"\nAccident date: {self.accident_date}\nAccident time: {self.accident_time}" \
            f"\nAccident route: {self.route}\nDeaths: {self.deaths}\n"

    def process(self):
        self.accident_date = get_date(self)
        if not self.accident_date:
            self.accident_date = self.date
        self.accident_time, self.review_status = get_time(self)
        if self.accident_time:
            try:
                self.accident_time = datetime.strptime(self.accident_time, '%H:%M').time()
            except ValueError:
                self.accident_time = translate_time(self.accident_time)
        self.route = get_route(self)
        self.deaths = get_deaths(self)

    def to_dict(self):
        return {"url": make_clickable(self.url, self.title),
                "epi": self.summary,
                "date": self.accident_date,
                "time": self.accident_time,
                "deaths": self.deaths,
                "route": self.route}

