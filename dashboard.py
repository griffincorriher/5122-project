from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/Sample - Superstore.csv')

fig = px.histogram(df, x="Category", y="Profit", color="Segment", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Superstore Dashboard'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)