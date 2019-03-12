from filters import date_regex, time_regex, time_regex_detailed, route_regex, death_regex
from filters import get_first_match, spanish_to_english
from filters.helpers import months
from dateparser import parse


def get_date(story):
    match_object1 = date_regex.search(f"{story.title} {story.summary}")
    if match_object1:
        if len([month for month in months if month in match_object1.group()]):
            date = parse(match_object1.group(), languages=['es'])
            return date.replace(year=story.date.year)
    match_object2 = date_regex.search(story.article)
    if match_object2:
        print("searching article")
        if len([month for month in months if month in match_object2.group()]):
            date = parse(match_object2.group(), languages=['es'])
            return date.replace(year=story.date.year)
    else:
        return None


def get_time(story):
    match_object1 = time_regex.search(f"{story.title} {story.summary}")
    match_object2 = time_regex_detailed.search(f"{story.title} {story.summary}")
    if match_object1 and match_object2:
        return get_first_match(match_object1, match_object2).group()
    elif match_object1:
        return match_object1.group()
    elif match_object2:
        return match_object2.group()
    else:
        match_object3 = time_regex.search(story.article)
        match_object4 = time_regex_detailed.search(story.article)
        if match_object3 and match_object4:
            return get_first_match(match_object3, match_object4).group()
        elif match_object3:
            return match_object3.group()
        elif match_object4:
            return match_object4.group()
        else:
            return None


def get_route(story):
    for regex in route_regex():
        match_object = [keyword.strip() for keyword in story.keywords if regex.search(keyword)]
        if len(match_object):
            return match_object[0]
        else:
            match_object1 = regex.search(f"{story.title} {story.summary}")
            if match_object1:
                return match_object1.group()


def get_deaths(story):
    for regex in death_regex():
        match_object1 = regex.search(f"{story.title} {story.summary}")
        if match_object1:
            deaths = match_object1.group(1).lower()
            if not deaths.isdigit():
                deaths = spanish_to_english.get(deaths)
            if deaths and int(deaths) < 60:
                return int(deaths)
    for regex in death_regex():
        match_object2 = regex.search(story.article)
        if match_object2:
            deaths = match_object2.group(1).lower()
            if not deaths.isdigit():
                deaths = spanish_to_english.get(deaths)
            if deaths and int(deaths) < 60:
                return int(deaths)
    return None

