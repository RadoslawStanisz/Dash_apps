from dash import Input, Output
import plotly.express as px
from app import app
import pandas as pd


df_dash_1 = pd.read_csv(r"../../data/covid.csv")

@app.callback(
    Output(component_id='graph-1', component_property='figure'),
    Input(component_id='country', component_property='value')
)
def generate_first_graph(country):
    df = df_dash_1[df_dash_1['location'] == country]
    fig = px.line(
        data_frame=df,
        x='date',
        y='total_cases',
        title=f'Cumulative number of positive cases in {country}',
        labels={'total_cases': 'Total cases'}
    )
    return fig

@app.callback(
    Output(component_id='graph-2', component_property='figure'),
    Input(component_id='country', component_property='value')
)
def generate_second_graph(country):
    df = df_dash_1[df_dash_1['location'] == country]
    fig = px.line(
        data_frame=df,
        x='date',
        y='total_deaths',
        title=f'Cumulative number of deaths in {country}',
        labels={'total_deaths': 'Total deaths'}
    )
    return fig
