import argparse
from data_processing import pickle_soup, str2bool
import pickle
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_colwidth', -1)


def load_data(_reload=False):
    if _reload:
        pickle_soup(10)
    with open("data_processing/data_retrieval/articles.pickle", "rb") as f:
        temp_data = pickle.load(f)
    return temp_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', type=str2bool)
    args = parser.parse_args()
try:
    reload = args.arg1
except NameError:
    reload = False
final_data = []
all_data = load_data(reload)[::-1]
for index, story in enumerate(all_data):
    story.process()
    missing_values = [val for val in story.__dict__.values() if not val]
    if len(missing_values) < 2:
        final_data.append(story.to_dict())

print("data successfully initialized.")
