import io
import pickle
from IPython.display import HTML
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_colwidth', -1)

# TO DO:
with open("filters/articles.pickle", "rb") as f:
    temp_data = pickle.load(f)


data = []
for story in temp_data:
    story.process()
    story_dict = story.to_dict()
    missing_values = [val for val in story_dict.values() if not val]
    if len(missing_values) < 2:
        data.append(story_dict)

df = pd.DataFrame.from_dict(data, orient='columns')
str_io = io.StringIO()
HTML(df.to_html(buf=str_io, classes='table table-striped table-dark', escape=False))
HTML(df.to_html('text.html', classes='table table-striped table-dark'))
html_str = str_io.getvalue()

