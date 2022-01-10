
from flask import Flask, render_template, redirect, url_for, session, request
import json
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from plotlydash.dashboard import dashboard
import flask
import dash_bootstrap_components as dbc
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import string
import os
import random


server = flask.Flask(__name__) 

dash_app = dash.Dash(
    server=server,
    routes_pathname_prefix='/',
    external_stylesheets=[
        'https://fonts.googleapis.com/css?family=Lato',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
        'styles.css',
        dbc.themes.BOOTSTRAP
    ],
    name='CSV Visualizer',
    title='CSV Visualizer'
)
dash_app.config.suppress_callback_exceptions = True

dash_app.validation_layout = html.Div()

dash_app.layout = html.Div()

dash_app = dashboard(dash_app)


if __name__ == '__main__':  
    server.run()