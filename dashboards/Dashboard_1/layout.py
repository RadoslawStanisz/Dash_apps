from dash import html, dcc
import pandas as pd


df_dash_1 = pd.read_csv("../../data/covid.csv")
countries_list = list(df_dash_1['location'].drop_duplicates())


layout = html.Div([
    html.Div([
        html.H1('COVID-19 Tracker')
    ]),                           
    html.P("Choose country:"),
    dcc.Dropdown(
        id='country', 
        options=[{'value': str(country), 'label': country} 
                 for country in countries_list],
        value=countries_list[0]
    ),
    html.Br(),
    html.Div(children=[
        dcc.Graph(id="graph-1", style={'display': 'inline-block', 'width': '48%'}),
        dcc.Graph(id="graph-2", style={'display': 'inline-block', 'width': '48%'})
    ])
])
