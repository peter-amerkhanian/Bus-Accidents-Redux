import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
import pandas as pd
from data_processing.data_cleaning import make_html_table
from data_processing.run_retrieval import final_data

df = pd.DataFrame.from_dict(final_data, orient='columns')
df.to_csv("for_exploration.csv")

html_str = make_html_table(df)
