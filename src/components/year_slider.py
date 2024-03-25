from dash import Dash, dcc, html, Input, Output, callback
from . import ids
import pandas as pd
from ..data.source import DataSource

mark_dictionary = {
    2010: '2010',
    2011: '2011',
    2012: '2012',
    2013: '2013',
    2014: '2014',
    2015: '2015',
    2016: '2016',
    2017: '2017',
    2018: '2018',
    2019: '2019',
    2020: '2020',
    2021: '2021',
    2022: '2022',
    2023: '2023',
    2024: '2024'  # Added entry for 2024
}

@callback(
    Output('slider-output-container', 'children'),
    Input(ids.YEAR_SLIDER, 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)

def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Slider(
                id = ids.YEAR_SLIDER,
                min = int(min(source.unique_years)),
                max = int(max(source.unique_years)),
                step = 1,
                value=2023,
                marks= mark_dictionary,
                
            ),
            html.Div(id='slider-output-container')
        ]
    )