import argparse
from data_retrieval import pickle_soup
from datetime import datetime, timedelta
import io
import pickle
from IPython.display import HTML
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_colwidth', -1)
from pprint import pprint


# TO DO:
def load_data(reload=False):
    if reload:
        pickle_soup(10)
    with open("data_retrieval/articles.pickle", "rb") as f:
        temp_data = pickle.load(f)
    return temp_data


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


def within_two_days(_current_story, _story):
    today = _story.date == _current_story.date
    tomorrow = _story.date == _current_story.date + timedelta(days=1)
    yesterday = _story.date == _current_story.date - timedelta(days=1)
    return today or tomorrow or yesterday


def other_info_matches(_current_story, _story):
    same_route = _story.route == _current_story.route
    same_deaths = _story.deaths == _current_story.deaths
    return same_deaths or same_route


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', type=str2bool)
    args = parser.parse_args()
try:
    reload = args.arg1
except NameError:
    reload = False
final_data = []
all_data = load_data(reload)
for index, story in enumerate(all_data):
    story.process()
    missing_values = [val for val in story.__dict__.values() if not val]
    if len(missing_values) < 2:
        final_data.append(story.to_dict())

print("data successfully initialized.")
df = pd.DataFrame.from_dict(final_data, orient='columns')
df.to_csv("for_exploration.csv")
str_io = io.StringIO()
HTML(df.to_html(buf=str_io, classes='table table-striped table-dark', escape=False))
HTML(df.to_html('table_text.html'))
html_str = str_io.getvalue()
