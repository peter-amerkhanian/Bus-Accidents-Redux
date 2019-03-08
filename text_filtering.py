from regular_expressions import date_regex, time_regex, time_regex_detailed, route_regex, death_regex
from misc_helpers import get_first_match


def get_date(story):
    match_object1 = date_regex.search(f"{story.title} {story.summary}")
    if match_object1:
        return match_object1.group()
    else:
        print("first try failed")
        match_object2 = date_regex.search(story.article)
        if match_object2:
            return match_object2.group()
        else:
            print("second try failed")


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
        print("first try failed")
        match_object3 = time_regex.search(story.article)
        match_object4 = time_regex_detailed.search(story.article)
        if match_object3 and match_object4:
            return get_first_match(match_object3, match_object4).group()
        elif match_object1:
            return match_object1.group()
        elif match_object2:
            return match_object2.group()
        else:
            print("second try failed")


def get_route(story):
    match_object = [keyword for keyword in story.keywords if route_regex.search(keyword)]
    if len(match_object):
        return match_object


def get_deaths(story):
    for regex in death_regex():
        match_object1 = regex.search(f"{story.title} {story.summary}")
        if match_object1:
            return match_object1.group()
    print("first try failed")
    for regex in death_regex():
        match_object2 = regex.search(story.article)
        if match_object2:
            return match_object2.group()
    print("second try failed")

