import datetime

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


def translate_time(time):
    if time == 'primeras horas de la mañana':
        return datetime.time(2, 0)
    if time == 'noche':
        return datetime.time(20, 0)
    if time == 'madrugada':
        return datetime.time(2, 0)
    if time == 'mañana':
        return datetime.time(8, 0)
    if time == 'medianoche':
        return datetime.time(23, 59)
    if time == 'tarde':
        return datetime.time(15, 0)


def str2bool(v):
    """
    using function from
    https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    :param v: a string, the user's argument
    :return: a boolean, true or false
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

