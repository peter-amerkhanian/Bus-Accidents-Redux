import pickle

# TO DO:
with open("filters/articles.pickle", "rb") as f:
    temp_data = pickle.load(f)

for story in temp_data:
    story.process()
    print(story)
