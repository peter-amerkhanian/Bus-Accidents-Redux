import io
import pickle
import pandas as pd
from pandas import ExcelWriter

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
    # else:
        # print(story)
# print(len(data), "/", len(temp_data))

df = pd.DataFrame.from_dict(data, orient='columns')
writer = ExcelWriter('test.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
str_io = io.StringIO()
df.to_html(buf=str_io, classes='table table-striped')
html_str = str_io.getvalue()
print(html_str)

