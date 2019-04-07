import pickle
from flask import Flask, render_template, Markup


app = Flask(__name__)


with open('data_processing/processed_data.pickle', 'rb') as f:
    html_table_processed = pickle.load(f)

with open('data_processing/raw_data.pickle', 'rb') as f:
    html_table_raw = pickle.load(f)


@app.route('/')
def home(table_processed=Markup(html_table_processed)):
    return render_template('processed_table.html',
                           table_processed=table_processed)


@app.route('/processed-table')
def processed(table_processed=Markup(html_table_processed)):
    return render_template('processed_table.html',
                           table_processed=table_processed)


@app.route('/raw-table')
def raw(table_raw=Markup(html_table_raw)):
    return render_template('raw_table.html',
                           table_raw=table_raw)


