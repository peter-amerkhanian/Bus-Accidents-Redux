import argparse

from data_retrieval import pickle_soup
import io
import pickle
from IPython.display import HTML
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_colwidth', -1)


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', type=str2bool)
    args = parser.parse_args()
    print(args)
    print(args.arg1)
try:
    reload = args.arg1
except NameError:
    reload = False
data = []
for story in load_data(reload):
    story.process()
    missing_values = [val for val in story.__dict__.values() if not val]
    if len(missing_values) < 2:
        data.append(story.to_dict())
df = pd.DataFrame.from_dict(data, orient='columns')
str_io = io.StringIO()
HTML(df.to_html(buf=str_io, classes='table table-striped table-dark', escape=False))
HTML(df.to_html('text.html'))
html_str = str_io.getvalue()
