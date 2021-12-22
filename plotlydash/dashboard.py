"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from .data import create_dataframe
from .layout import html_layout
import plotly.express as px
import json 

from dash.dependencies import Input, Output, State
import string
import random
  
from flask import Flask, render_template, redirect, url_for, session, request
import urllib.parse
import flask



def dashboard(server,  messages,dash_app):
    """Create a Plotly Dash dashboard."""    

    
    with server.test_request_context('/dashboard/'):
       df = create_dataframe(json.loads(messages)["dataFrame"], server)

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[

        dcc.Tab(label='DataFrame View', value='tab-1' , children = [    
            create_data_table(df)]
        
        ),
        dcc.Tab(label='ScatterPlot', value='tab-2', children = [

            html.Div( id='input-1', children = [          
            dcc.Input(id='input-x-scatter', type='text', placeholder='Enter X axis Value'),
            dcc.Input(id='input-y-scatter', type='text', placeholder='Enter Y axis Value'),
                ]
            ),

            html.Div( id='input-2', children = [
                    
            dcc.Input(id='input-color-scatter', type='text', placeholder='Enter Color axis Value'),
            dcc.Input(id='input-size-scatter', type='text', placeholder='Enter Size axis Value'),
                ]
            ),
           

            html.Button(id='submit-button-state', n_clicks=0, children='Submit'),

            html.Div(id='output-state', children = []),
            ]
        ),

        
    ]),
    html.Div(id='tabs-content')
    ])  


    @dash_app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-x-scatter', 'value'),
              State('input-y-scatter', 'value'),
              State('input-color-scatter', 'value'),
              State('input-size-scatter', 'value'))
    def update_scatterplot(n_clicks, input1, input2, input3, input4): 
        print("3 "+str(input3 is None))
        print(input3)
        print("4 "+str(input4 is None))
        print(input4)
        fig = px.scatter_matrix(df)
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input4 is None) and (input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2))
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), color=str(input3))
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input4 is None) and (input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), size=str(input4))
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input4 is None) and not(input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), color=str(input3), size=str(input4))
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  dcc.Graph(
                id='graph-1-tabs',
                figure=fig
              ) 

    return dash_app.server





def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode='native',
        page_size=300
    )
    return table