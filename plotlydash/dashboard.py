"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
from dash import dash_table
from dash import dcc

from plotlydash.dashboard_layout import dashboard_layout
from .data import create_dataframe
from .layout import html_layout
import plotly.express as px
import json 
from dash import html
from dash.dependencies import Input, Output, State
from flask import Flask, render_template, redirect, url_for, session, request
import dash_bootstrap_components as dbc
import plotly.graph_objects as go



def dashboard(dash_app, df = px.data.iris()):
    """Create a Plotly Dash dashboard."""    

    print("SETTING INTI")
    dropdowns = {}
    plot_theme = "plotly_dark"
    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold',
        'backgroundColor': 'black',
        'color': 'white',
    }

    dropdown_style = {
        'fontWeight': 'bold',
        'backgroundColor': 'black',
        'color': 'white',
    }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#119DFF',
        'color': 'white',
        'padding': '6px'
    }

    searchbar_div_style = { "marginLeft": "20%", "width":"48%", " marginRight": "1%","display":"inline-grid"}
    left_indent_style = {"marginLeft": "1%",}

    

    barmode = [{"label":"stack", "value":"stack"},{"label":"group", "value":"group"}]

    regressioon_Algos = [{"label":"Ordinary least squares", "value":"ols"},
                        {"label":"Locally WEighted Scatterplot Smoothing", "value":"lowess"},
    #                    {"label":"5-Point Moving Averages", "value":"rolling"},
    #                    {"label":"5-point Exponentially Weighted Moving Average", "value":"ewm"},
                        {"label":"Expanding Mean", "value":"expanding"},]
    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div([
        dcc.Interval(
            id='interval-component',
            interval=60*1000, # in milliseconds
            n_intervals=0
        ),
        html.Div( id='search-bar-div',style = searchbar_div_style, children= [ 
            dcc.Input(id='input-search-field', placeholder='URL to CSV', value = "https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv"),
        ]),
        dbc.Button(id='submit-button-search-field',  color="primary", n_clicks=0, children='Submit Query',  className="me-1"),
        html.P(" "),
        html.Div(id='update-content', className="container", style={"marginUp": "15px"}, children = [
        dashboard_layout(dash_app)  
    ]),
    ])

    @dash_app.callback(Output('update-content', 'children'),
              Input('submit-button-search-field', 'n_clicks'),
              State('input-search-field', 'value'))
    def update_dfplot(n_clicks, input1): 
        if not(input1 is None):
            df, dropdowns = create_dataframe(input1)
            return dashboard_layout(dash_app, df,dropdowns)
        return dashboard_layout(dash_app)

    return dash_app



def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
        page_size=300
        
    )
    return table