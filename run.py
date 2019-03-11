import pickle
from filters import get_time, get_date, get_route, get_deaths

# TO DO:
with open("filters/articles.pickle", "rb") as f:
    temp_data = pickle.load(f)

for story in temp_data:
    # story.accident_date = get_date(story)
    # story.accident_time = get_time(story)
    # story.route = get_route(story)
    # story.deaths = get_deaths(story)
    print(f"Story title: {story.title}\nStory Summary: {story.summary}\nStory url:{story.url}")
    print(f"Story pub date: {story.date}")
    print(f"Accident date: {get_date(story)}")
    print(f"Accident time: {get_time(story)}")
    print(f"Accident route: {get_route(story)}")
    print(f"Deaths: {get_deaths(story)}")
    print("\n")