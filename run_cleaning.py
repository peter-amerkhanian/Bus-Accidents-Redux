import pandas as pd
from data_processing.data_cleaning import make_html_table
import pickle


html_str = make_html_table(df, status="raw")
