import re

date_regex = re.compile(r'\b\d{1,2}\sde\s[a-z]{5,11}\b(\sde\s20\d\d)?')
time_regex = re.compile(r'\d{1,2}:\d{1,2}', re.IGNORECASE)
time_regex_detailed = re.compile(r'\bmañana\b|\bmedianoche\b|\btarde\b|/'
                                 r'\bmediodía\b|\bmad(r)?ugada\b|\bnoche\b|\bprimeras horas de la mañana\b',
                                 re.IGNORECASE)

route_regex = re.compile(r'(\s[A-Z][a-z]{0,10})?\s[A-Z]\w+\s?[-–][-]?\s?[A-Z]\w+(\s[A-Z][a-z]{0,10})?|/'
                         r'(\s[A-Z][a-z]{0,10})?\s[A-Z]\w+\sa\s[A-Z]\w+(\s[A-Z][a-z]{0,10})?/'
                         r'|([A-Z][a-z]{0,10})?\s[A-Z]\w+\shacia\s[A-Z]\w+(\s[A-Z][a-z]{0,10})?')

# To do add una persona fallecio
def death_regex():
    for regex in [r'(\d{1,3})\spersona(s)?\sfallecida(s)?\b',
                  r'(\w{1,7})\spersona(s)?\sfallecida(s)?\b',
                  r'(\d{1,3})\spersona\sfalleció\b',
                  r'(\w{1,7})\spersona\sfalleció\b',
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
