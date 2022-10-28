from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Ctrl+shift+r to reload CSS if not reloading

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__,
                external_stylesheets=external_stylesheets)

df = pd.read_csv('data/Sample - Superstore.csv')

segments = df['Segment'].unique()
categories = df['Category'].unique()
categories.sort()
sub_categories = df['Sub-Category'].unique()
sub_categories.sort()
products = df['Product Name'].unique()
products.sort()

countries = df['Country'].unique()
regions = df['Region'].unique()
states = df['State'].unique()
cities = df['City'].unique()
postal_code = df['Postal Code'].unique()
area_of_interest = ['Area Code', 'City', 'State', 'Region', 'Country']
area_of_interest.sort()

ship_mode = df['Ship Mode'].unique()
metric_of_interest = ['Sales', 'Discount', 'Profit', 'Profit per Item', 'Shipping Speed']
metric_of_interest.sort()


fig = px.histogram(df, x="Category", y="Profit", color="Segment", barmode="group")

app.layout = html.Div([
    html.Div(
        className='row1',
        children=[
            html.Div(
                children=[
                html.H5('Metrics of Interest'),
                dcc.Checklist(metric_of_interest,
                        [metric_of_interest[0], metric_of_interest[2]], inline=False),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'background-color': '#245C8C', 'vertical-align': 'top', 'font-size': 20}
            ),
            
            html.Div(children=[
                html.H5('Area of Interest'),
                dcc.RadioItems(area_of_interest, 'Country'),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'background-color': '#5494B4', 'vertical-align': 'top', 'font-size': 20}
            ),

            html.Div(children=[
                html.H5('Select Area(s)'),
                dcc.Dropdown(countries,
                            countries[0],
                            multi = True)
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'background-color': '#6CA4C4', 'vertical-align': 'top', 'font-size': 20}
            ),            
        ]
    ),

    html.Div(
        className='row2',
        children=[
            html.Div(children=[
                html.H5('Segments of Interest'),
                dcc.Checklist(segments, [segments[0], segments[1], segments[2]]),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'background-color': '#6CA4C4', 'vertical-align': 'top', 'font-size': 20}
            ),   

            html.Div(
                children=[
                html.H5('Category of Interest'),
                dcc.Checklist(categories, [categories[0], categories[1], categories[2]]),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'color': 'black',  'background-color': '#84B4CC', 'vertical-align': 'top', 'font-size': 20}
            ),

            html.Div(children=[
                html.H5('Select Product(s)'),
                dcc.Dropdown(products,
                            multi = True)
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'color': 'black', 'background-color': '#E6E6E6', 'vertical-align': 'top'}
            ),            
        ]
    ),

    html.Div(
        className='row3',
        children=[
            html.Div(children=[
                html.H5('Chart Placeholder'),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 932, 'height': 500, 'color': 'black',  'background-color': 'white', 'vertical-align': 'top', 'font-size': 20}
            ),

            html.Div(children=[
                html.H5('ML Recommendation Placeholder'),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 500, 'color': 'black',  'background-color': '#C0C0C0', 'vertical-align': 'top', 'font-size': 20}
            ),            
        ],
    )


], style={"margin": 15, 'max-width' : 1458, 'color': 'white'})


if __name__ == '__main__':
    app.run_server(debug=True)

