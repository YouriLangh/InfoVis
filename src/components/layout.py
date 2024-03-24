from dash import Dash, html
from . import district_dropdown, bar_chart, year_slider, monthly_trend_lineplot
from ..data.source import DataSource

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    district_dropdown.render(app, source)
                ]
            ),
             bar_chart.render(app, source),
             monthly_trend_lineplot.render(app,source),
             year_slider.render(app, source)
        ]
    )