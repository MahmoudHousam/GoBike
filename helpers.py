import pandas as pd
import numpy as np
import plotly.graph_objects as go


def explore_nans(df, title):
    """a function that takes a dataframe and inspect the Null vs
    Not-null values to visualize a groupped bar chart that will help take
    decisions to deal with missing data.

    Args:
        df: pandas dataframe
        title: (string): x label title

    Returns:
        bar chart: Null vs Not-null values
    """
    df_null = df.isnull().sum()
    df_not_null = df.notnull().sum()
    labels = df.columns.tolist()
    null_values = df_null.values.tolist()
    not_null_values = df_not_null.values.tolist()
    data = [
        go.Bar(
            name="Not Null",
            x=not_null_values,
            y=labels,
            orientation="h",
            marker=dict(
                color="rgb(128,128,128)",
            ),
        ),
        go.Bar(
            name="Null",
            x=null_values,
            y=labels,
            orientation="h",
            marker=dict(
                color="rgb(192,192,192)",
            ),
        ),
    ]
    layout = go.Layout(title=title, barmode="stack", yaxis={"dtick": 1})
    fig = go.Figure(data, layout)
    return fig.show(renderer="svg", width=1200, height=500)