from IPython.display import HTML
import io


def make_html_table(dataframe, status):
    str_io = io.StringIO()
    HTML(dataframe.to_html(buf=str_io, classes='table table-striped table-dark', escape=False))
    # This creates an HTML file too:
    # HTML(dataframe.to_html('data_processing/{}_table_text.html'.format(status)))
    return str_io.getvalue()