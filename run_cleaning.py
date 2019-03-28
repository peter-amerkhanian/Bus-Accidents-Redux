import pandas as pd
from data_processing.data_cleaning import make_html_table
from run_retrieval import final_data

df = pd.DataFrame.from_dict(final_data, orient='columns')
df.to_csv("data_processing/for_exploration.csv")

html_str = make_html_table(df)
