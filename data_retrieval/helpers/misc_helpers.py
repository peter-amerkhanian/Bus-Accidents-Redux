fatal_keywords = ['muert', 'fallec', 'murier', 'muri', 'sega']

spanish_to_english = {"uno": 1,
                      "un": 1,
                      "una": 1,
                      "dos": 2,
                      "tres": 3,
                      "cuatro": 4,
                      "cinco": 5,
                      "seis": 6,
                      "siete": 7,
                      "ocho": 8,
                      "nueve": 9,
                      "diez": 10,
                      "once": 11,
                      "doce": 12,
                      "trece": 13,
                      "catorce": 14,
                      "quince": 15,}

months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
          "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def get_first_match(match1, match2):
    if match1.start() < match2.start():
        return match1
    else:
        return match2


def make_clickable(val, text):
    return '<a target="_blank" href="{}">{}</a>'.format(val, text)

