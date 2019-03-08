import re

date_regex = re.compile(r'\b\d{1,2}\sde\s[a-z]{5,11}\b(\sde\s20\d\d)?')
time_regex = re.compile(r'\d{1,2}:\d{1,2}', re.IGNORECASE)
time_regex_detailed = re.compile(r'\bmad(r)?ugada\b|\bmedianoche\b|\btarde\b|/'
                                 r'\bmediodía\b|\bmañana\b|\bnoche\b|\bprimeras horas de la mañana\b',
                                 re.IGNORECASE)

route_regex = re.compile(r'(\s[A-Z][a-z]{0,10})?\s[A-Z]\w+\s?[-–][-]?\s?[A-Z]\w+(\s[A-Z][a-z]{0,10})?|/'
                         r'(\s[A-Z][a-z]{0,10})?\s[A-Z]\w+\sa\s[A-Z]\w+(\s[A-Z][a-z]{0,10})?')
