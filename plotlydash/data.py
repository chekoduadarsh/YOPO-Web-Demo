"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd



import seaborn as sns


sns.load_dataset("titanic")

def create_dataframe(message, server):
    """Create Pandas DataFrame from local CSV."""
    print("<"+message+">")
    df = pd.read_csv(message)

    #df = sns.load_dataset("titanic")
    return df