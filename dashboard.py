from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/Sample - Superstore.csv')

segments = df['Segment'].unique()
categories = df['Category'].unique()
sub_categories = df['Sub-Category'].unique()
product = df['Product Name'].unique()
countries = df['Country'].unique()
regions = df['Region'].unique()
area_of_interest = [regions]
ship_mode = df['Ship Mode'].unique()
metric_of_interest = ['Sales', 'Discount', 'Profit', 'Profit per Item', 'Shipping Speed']

fig = px.histogram(df, x="Category", y="Profit", color="Segment", barmode="group")

app.layout = html.Div([
    html.Div(children=[
    html.Label('Checkboxes'),
    dcc.Checklist(metric_of_interest,
                    [metric_of_interest[0], metric_of_interest[2]]
    ),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(area_of_interest),



        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'inline-block', 'text-align':'justify'})


if __name__ == '__main__':
    app.run_server(debug=True)