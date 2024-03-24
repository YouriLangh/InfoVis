from dash import Dash, dcc, html, Input, Output, callback
from . import ids
import pandas as pd
import plotly.express as px
from ..data.source import DataSource




def render(app:Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.MONTHLY_LINEPLOT, "children"),
        Input(ids.YEAR_SLIDER, "value")
    )
    def update_lineplot(year: int) -> html.Div:
        filtered_source = source.filter(years=[year])

        # Creating a custom color map
        #custom_colors = px.colors.qualitative.Vivid

        if not filtered_source.row_count:
            return html.Div("No data selected.")
        # Plot the line chart using Plotly Express
        df_plotly = filtered_source.monthly_crime_counts('ME')
        fig = px.line(df_plotly, x='Month', y='Number of Crimes', title=f'Number of Crimes Committed in {year}')
        # Update layout properties
        fig.update_layout(xaxis=dict(tickmode='array', tickvals=df_plotly['Month']))
        return html.Div(dcc.Graph(figure=fig), id=ids.MONTHLY_LINEPLOT)
    return html.Div(id=ids.MONTHLY_LINEPLOT)