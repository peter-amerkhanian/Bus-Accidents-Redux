import argparse
from data_processing import pickle_soup, str2bool
import pickle
import pandas as pd
from data_processing.data_cleaning import make_html_table

pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_colwidth', -1)


def load_data(_reload=False):
    if _reload:
        pickle_soup(10)
    with open("data_processing/data_retrieval/articles.pickle", "rb") as f:
        temp_data = pickle.load(f)
    return temp_data


def create_raw_data(_reload):
    all_data = load_data(_reload)[::-1]
    for index, story in enumerate(all_data):
        story.process()
        missing_values = [val for val in story.__dict__.values() if not val]
        if len(missing_values) < 2:
            yield story.to_dict()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', type=str2bool)
    args = parser.parse_args()
    try:
        reload = args.arg1
    except NameError:
        reload = False
    final_data = create_raw_data(reload)
    df = pd.DataFrame.from_dict(final_data, orient='columns')
    df.to_csv("data_processing/raw_data.csv")
    html_str = make_html_table(df, status="raw")
    with open('data_processing/raw_data.pickle', 'wb') as f:
        pickle.dump(html_str, f)
    print("data successfully initialized.")