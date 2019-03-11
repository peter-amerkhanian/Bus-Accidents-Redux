import pickle
import pandas as pd

# TO DO:
with open("filters/articles.pickle", "rb") as f:
    temp_data = pickle.load(f)

data = []
for story in temp_data:
    story.process()
    print(story)
    data.append(story.to_dict())

df = pd.DataFrame(data)
df.to_html('html/table.html')


