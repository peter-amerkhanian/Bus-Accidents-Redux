from IPython.display import HTML
import io


def make_html_table(dataframe):
    str_io = io.StringIO()
    HTML(dataframe.to_html(buf=str_io, classes='table table-striped table-dark', escape=False))
    HTML(dataframe.to_html('data_processing/table_text.html'))
    return str_io.getvalue()