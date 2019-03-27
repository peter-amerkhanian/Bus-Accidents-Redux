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


def within_two_days(current_story, story):
    return (story.date == current_story.date or story.date == current_story.date + timedelta(days=1) or story.date == current_story.date - timedelta(days=1))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', type=str2bool)
    args = parser.parse_args()
try:
    reload = args.arg1
except NameError:
    reload = False
final_data = []
current_story = None
all_data = load_data(reload)[::-1]
for index, story in enumerate(all_data):
    story.process()
    missing_values = [val for val in story.__dict__.values() if not val]
    if len(missing_values) < 2:
        if current_story and within_two_days(current_story, story):
            combined_story = {'url': current_story.url,
                              'epi': current_story.summary,
                              'date': current_story.accident_date,
                              'time': current_story.accident_time,
                              'route': current_story.route}
            dupes = [current_story]
            for _story in all_data[index:]:
                if within_two_days(current_story, _story):
                    dupes.append(_story)
                    # all_data.remove(_story)
            combined_story["deaths"] = [story.deaths for story in dupes if story.deaths][-1]
            combined_story["time"] = min([story.accident_time for story in dupes if story.accident_time])
            combined_story["route"] = [story.route for story in dupes if story.route][0]
            print(dupes)
            print(combined_story)

            print("==========")
            # final_data.remove(current_story.to_dict())
            final_data.append(combined_story)
        else:
            final_data.append(story.to_dict())
        current_story = story

# pprint(final_data)
# df = pd.DataFrame.from_dict(data, orient='columns')
# df.to_csv("test.csv")
# str_io = io.StringIO()
# HTML(df.to_html(buf=str_io, classes='table table-striped table-dark', escape=False))
# HTML(df.to_html('text.html'))
# html_str = str_io.getvalue()