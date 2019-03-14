import pickle
import pandas as pd

# TO DO:
with open("filters/articles.pickle", "rb") as f:
    temp_data = pickle.load(f)


data = []
for story in temp_data:
    story.process()
    story_dict = story.to_dict()
    missing_values = [val for val in story_dict.values() if not val]
    if len(missing_values) < 2:
        data.append(story)
    else:
        print(story)
print(len(data), "/", len(temp_data))


# df = pd.DataFrame(data)
# df.to_html('html/table.html')


