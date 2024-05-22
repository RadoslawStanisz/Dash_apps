from dash import html, dcc
import pandas as pd

# Load data
df_covid = pd.read_csv("../../data/covid.csv")

layout = html.Div([
    html.Div([
        html.H1('COVID-19 Tracker')
    ]),                           
    html.P("Choose top x countries:"),
    dcc.Slider(5, 20, 5,
        value=5,
        id='my-slider'
    ),   
    html.Br(),
    html.Div(children=[
        dcc.Graph(id='first-graph', style={'display':'inline-block', 'width': '48%'}),
        dcc.Graph(id='second-graph', style={'display':'inline-block', 'width': '48%'})
    ])
])
