def get_first_non_null(series):
    series = series.tolist()
    for x in series:
        if x or type(x) != float:
            return x


def within_5(numbers_set):
    numbers = list(numbers_set)
    if len(numbers) == 1:
        return True
    baseline = numbers[0]
    for number in numbers:
        if abs(baseline - number) > 5:
            return False
    return True


def max_two_routes(strings_set):
    strings = list(strings_set)
    if len(strings) <= 2:
        return True