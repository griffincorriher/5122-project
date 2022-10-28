from re import S
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
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
countries.sort()
regions = df['Region'].unique()
regions.sort()
states = df['State'].unique()
states.sort()
cities = df['City'].unique()
cities.sort()
postal_code = df['Postal Code'].unique()
postal_code.sort()
area_of_interest = ['Postal Code', 'City', 'State', 'Region', 'Country']
area_of_interest.sort()
area_dict = {
    'Postal Code': postal_code,
    'City': cities,
    'State': states,
    'Region': regions,
    'Country': countries
}

ship_mode = df['Ship Mode'].unique()
metric_of_interest = ['Sales', 'Discount', 'Profit', 'Profit per Item', 'Shipping Speed']
metric_of_interest.sort()

df['Order Year'] = pd.DatetimeIndex(df['Order Date'].astype('datetime64[ns]')).year
df['Ship Year'] = pd.DatetimeIndex(df['Ship Date'].astype('datetime64[ns]')).year

fig = px.histogram(df, x="Category", y="Profit", color="Segment", barmode="group")

app.layout = html.Div([
    html.Div(children=[
        dcc.RangeSlider(
            min(df['Order Year']),
            max(df['Order Year']), 1,
            value=[max(df['Order Year'])-2, max(df['Order Year'])],
            id='my-slider',
            dots=True,
            marks={i: '{}'.format(i) for i in range(min(df['Order Year']), max(df['Order Year'])+1, 1)},
            ),
        html.Div(id='slider-output-container')
        ], style = {'color':'black'}
    ),  
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
            
            html.Div(
                children=[
                html.H5('Area of Interest'),
                dcc.RadioItems(
                    id='area-radio',
                    options=[{'label': area, 'value': area} for area in area_of_interest],
                    value = area_of_interest[1]),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'background-color': '#5494B4', 'vertical-align': 'top', 'font-size': 20}
            ),

            html.Div(
                children=[
                html.H5('Select Area(s)'),
                dcc.Dropdown(
                    id='area-dropdown',
                    style={'color': 'black'},
                    multi=True)
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'background-color': '#6CA4C4', 'vertical-align': 'top', 'font-size': 20}
            ),            
        ]
    ),

    html.Div(
        className='row2',
        children=[
            html.Div(
                children=[
                html.H5('Segments of Interest'),
                dcc.Checklist(segments, [segments[0], segments[1], segments[2]]),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'color': 'black', 'background-color': '#6CA4C4', 'vertical-align': 'top', 'font-size': 20}
            ),   

            html.Div(
                children=[
                html.H5('Category of Interest'),
                dcc.Checklist(categories, [categories[0], categories[1], categories[2]]),
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 200, 'color': 'black',  'background-color': '#84B4CC', 'vertical-align': 'top', 'font-size': 20}
            ),

            html.Div(
                children=[
                html.H5('Select Product(s)'),
                dcc.Dropdown(
                            id='product-dropdown',
                            options=[{'label': product, 'value': product} for product in products],
                            multi = True
                            ),
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
                html.Div(id='display-selected-values')
                ], style={'display': 'inline-block', 'padding': 20, 'width': 446, 'height': 500, 'color': 'black',  'background-color': '#C0C0C0', 'vertical-align': 'top', 'font-size': 20}
            ),            
        ],
    )


], style={"margin": 15, 'max-width' : 1458, 'color': 'white'})

@app.callback(
    Output(component_id='slider-output-container', component_property='children'),
    Input(component_id='my-slider', component_property='value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output(component_id='area-dropdown', component_property='options'),
    Input(component_id='area-radio', component_property='value')
)
def update_date_dropdown(area):
    return [{'label': i, 'value': i} for i in area_dict[area]]



@app.callback(
    Output(component_id='display-selected-values', component_property='children'),
    Input(component_id='area-dropdown', component_property='value')
)
def set_display_children(selected_value):
    return 'you have selected {} option'.format(selected_value)



if __name__ == '__main__':
    app.run_server(debug=True)
