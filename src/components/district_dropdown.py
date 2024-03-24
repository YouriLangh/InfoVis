from dash import Dash, html, dcc 
from . import ids
import pandas as pd
from ..data.source import DataSource
from ..data.loader import DataSchema

def render(app: Dash, source: DataSource) -> html.Div:
    unique_districts = source.get_unique_generic(column_name=DataSchema.AREA)
    return html.Div(
        children=[
            html.H6("District"),
            dcc.Dropdown(
                id = ids.DISTRICT_DROPDOWN,
                options=[{"label": district, "value": district} for district in unique_districts],
                value=["Mission"],
                multi=True
            )
        ]
    )