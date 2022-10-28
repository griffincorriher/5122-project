from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = Dash(__name__, title='Superstore Dashboard', update_title=None)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('data/Sample - Superstore.csv')

segments = df['Segment'].unique()
categories = df['Category'].unique()
sub_categories = df['Sub-Category'].unique()
product = df['Product Name'].unique()
countries = df['Country'].unique()
regions = df['Region'].unique()
area_of_interest = ['Area Code', 'City', 'State', 'Region', 'Country']
ship_mode = df['Ship Mode'].unique()
metric_of_interest = ['Sales', 'Discount', 'Profit', 'Profit per Item', 'Shipping Speed']

fig = px.histogram(df, x="Category", y="Profit", color="Segment", barmode="group")

app.layout = html.Div([



    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(metric_of_interest,
                        [metric_of_interest[0], metric_of_interest[2]], inline=False),
    ], style={'display': 'flex', 'flex-direction': 'column'}),

    html.Div(children=[
        html.Br(),
        html.Label('Area of Interest'),
        dcc.RadioItems(area_of_interest, 'Country'),
    ], style={'display': 'flex', 'flex-direction': 'column', 'padding': 10}),

    html.Div(children=[
        html.Br(),
        html.Label('Segments of Interest'),
        dcc.Checklist(segments, [segments[0], segments[1], segments[2]]),
    ], style={'display': 'flex', 'flex-direction': 'column'}),

    html.Div(children=[
        html.Br(),
        html.Label('Category of Interest'),
        dcc.Checklist(categories, [categories[0], categories[1], categories[2]]),
    ], style={'padding': 10, 'flex': 1})

], style={'display': 'flex', 'flex-direction': 'column'})


if __name__ == '__main__':
    app.run_server(debug=True)