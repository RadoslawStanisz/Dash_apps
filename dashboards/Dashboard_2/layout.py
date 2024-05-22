from dash import html, dcc
import pandas as pd

# Load data
df_dash_2 = pd.read_csv("../../data/covid.csv")
df_dash_2 = df_dash_2[df_dash_2['date'] == df_dash_2['date'].max()].fillna(0)

# Prepare dropdown options
metric_dict = {
    'total_cases': 'Total cases',
    'total_deaths': 'Total deaths',
    'total_tests': 'Total tests',
    'total_vaccinations': 'Total vaccinations',
    'people_fully_vaccinated': 'Number of fully vaccinated people'
}

continent_list = list(df_dash_2['continent'].drop_duplicates())

layout = html.Div([
    html.Div([
        html.H1('COVID-19 Tracker')
    ]),                           
    html.P("Choose continent:"),
    dcc.Dropdown(
        id='continent', 
        options=[{'value': str(continent), 'label': continent} 
                 for continent in continent_list],
        value=continent_list[0]
    ),
    html.P("Choose metric:"),
    dcc.Dropdown(
        id='metric', 
        options=[{'value': metric, 'label': metric_label} 
                 for metric, metric_label in metric_dict.items()],
        value='total_cases'
    ),       
    html.Br(),
    html.Div(children=[
        dcc.Graph(id="map", style={'height': '800px', 'width': '100%'})
    ])
])
