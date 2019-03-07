import re

dateRegex = re.compile(r'\b\d{1,2}\sde\s[a-z]{5,11}\b(\sde\s20\d\d)?')
timeRegex = re.compile(r'\d{1,2}:\d{1,2}', re.IGNORECASE)
timeRegexDetailed = re.compile(r'\bmad(r)?ugada\b|\bmedianoche\b|\btarde\b|\bmediodía\b|\bmañana\b|\bnoche\b',
                               re.IGNORECASE)
