import pickle
from flask import Flask, render_template, Markup


app = Flask(__name__)

with open('data_processing/processed_data.pickle', 'rb') as f:
    html_table = pickle.load(f)


@app.route('/')
def hello_world(table=Markup(html_table)):
    return render_template('table.html', table=table)

