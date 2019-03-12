import re

date_regex = re.compile(r'\b\d{1,2}\sde\s[a-z]{4,11}(\sde\s20\d\d)?\b')
time_regex = re.compile(r'\d{1,2}:\d{1,2}', re.IGNORECASE)
time_regex_detailed = re.compile(r'\bmañana\b|\bmedianoche\b|\btarde\b|/'
                                 r'\bmediodía\b|\bmad(r)?ugada\b|\bnoche\b|\bprimeras horas de la mañana\b',
                                 re.IGNORECASE)


def route_regex():
    for regex in [r'([A-Z]\w+\s)?[A-Z]\w+\s?[-–]-?\s?[A-Z]\w+(\s[A-Z]\w+)?',
                  r'([A-Z]\w+\s)?[A-Z]\w+\sa\s[A-Z]\w+(\s[A-Z]\w+)?',
                  r'([A-Z]\w+\s)?[A-Z]\w+\shacia\s[A-Z]\w+(\s[A-Z]\w+)?']:
        yield re.compile(regex, re.IGNORECASE)


# To do add una persona fallecio
def death_regex():
    for regex in [r'(\d{1,3})\spersona(s)?\sfallecida(s)?\b',
                  r'(\w{1,7})\spersona(s)?\sfallecida(s)?\b',
                  r'(\d{1,3})\s((\w+\s){1,3})falleció\b',
                  r'(\w{1,7})\s((\w+\s){1,3})falleció\b',
                  r'(\d{1,3})\spersonas\smuertas',
                  r'(\w{1,7})\spersonas\smuertas',
                  r'(\w{1,7})\smuerto(s)?',
                  r'(\d{1,3})\smuerto(s)?',
                  r'(\d{1,3})\spersonas\smurieron',
                  r'(\w{1,7})\spersonas\smurieron',
                  r'(\d{1,3})\sfallecid[oa](s)?',
                  r'(\w{1,7})\sfallecid[oa](s)?',  # fix 27, the un fallecido
                  r'(\d{1,3})\spersonas\s(que\s)?fallecieron',
                  r'(\w{1,7})\spersonas\s(que\s)?fallecieron',
                  r'\sla\smuerte\sde\s(\w{1,7})\s',
                  r'\smurieron\s(\w{1,7})',
                  r'\ssegado\s(\w{1,7}\svidas\b)',
                  r'\ssegado\s(\d{1,3}\svidas\b)'
                  ]:
        yield re.compile(regex, re.IGNORECASE)
