from flask import Flask, render_template, Markup
from run import html_str

app = Flask(__name__)


@app.route('/')
def hello_world(table=Markup(html_str)):
    return render_template('table.html', table=table)