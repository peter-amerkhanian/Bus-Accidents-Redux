fatal_keywords = ['muert', 'fallec', 'murier', 'muri', 'sega']


def get_first_match(match1, match2):
    if match1.start() < match2.start():
        return match1
    else:
        return match2

