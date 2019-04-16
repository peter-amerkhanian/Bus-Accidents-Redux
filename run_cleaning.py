import pickle
from data_cleaning import make_html_table
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_colwidth', -1)

data = pd.read_csv("data/raw_data.csv")


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


for date in set(data.date):
    _data = data.loc[data.date == date]
    if len(_data) > 1:
        death_set = set((_data['deaths'].tolist()))
        route_set = set(([x.split('-')[-1].strip() if type(x) != float else x for x in _data['route']]))
        if max_two_routes(route_set) or within_5(death_set):
            combination = _data.groupby('date', as_index=False).agg({'deaths': 'last',
                                                                     'epi': 'first',
                                                                     'route': get_first_non_null,
                                                                     'time': get_first_non_null,
                                                                     'url': get_first_non_null})
            data = data[data.date != combination.date.tolist()[0]]
            data = data.append(combination, sort=False)

data = data.sort_values('date')
data.to_csv("data/processed_data.csv")
html_str = make_html_table(data, status="processed")
with open('data/processed_data.pickle', 'wb') as f:
    pickle.dump(html_str, f)