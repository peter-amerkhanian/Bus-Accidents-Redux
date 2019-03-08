from regular_expressions import dateRegex, timeRegex, timeRegexDetailed
from misc_helpers import get_first_match


def get_date(story):
    match_object1 = dateRegex.search(f"{story.title} {story.summary}")
    if match_object1:
        print(match_object1.group())
    else:
        print("first try failed")
        match_object2 = dateRegex.search(story.article)
        if match_object2:
            print(match_object2.group())
        else:
            print("second try failed")


def get_time(story):
    match_object1 = timeRegex.search(f"{story.title} {story.summary}")
    match_object2 = timeRegexDetailed.search(f"{story.title} {story.summary}")
    if match_object1 and match_object2:
        print(get_first_match(match_object1, match_object2))
    elif match_object1:
        print(match_object1)
    elif match_object2:
        print(match_object2.group())
    else:
        print("first try failed")
        match_object3 = timeRegex.search(story.article)
        match_object4 = timeRegexDetailed.search(story.article)
        if match_object3 and match_object4:
            print(get_first_match(match_object3, match_object4))
        elif match_object1:
            print(match_object1)
        elif match_object2:
            print(match_object2)
        else:
            print("second try failed")
