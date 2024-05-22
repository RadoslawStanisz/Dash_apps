from dash import Input, Output
import plotly.express as px
import pandas as pd
from app import app

# Load data
df_dash_2 = pd.read_csv("../../data/covid.csv")
df_dash_2 = df_dash_2[df_dash_2['date'] == df_dash_2['date'].max()].fillna(0)

# Metric dictionary
metric_dict = {
    'total_cases': 'Total cases',
    'total_deaths': 'Total deaths',
    'total_tests': 'Total tests',
    'total_vaccinations': 'Total vaccinations',
    'people_fully_vaccinated': 'Number of fully vaccinated people'
}

@app.callback(
    Output(component_id='map', component_property='figure'),
    [Input(component_id='continent', component_property='value'),
     Input(component_id='metric', component_property='value')]
)
def generate_covid_map(continent, metric):
    df = df_dash_2[df_dash_2['continent'] == continent]
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        size=metric,
        size_max=20,
        hover_name='location',
        projection="natural earth",
        title=f'COVID-19 - {metric_dict[metric]} in {continent}'
    )
    return fig
