from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from . import ids
from ..data.source import DataSource
from ..data.loader import DataSchema

def render(app:Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.DISTRICT_DROPDOWN, "value")
    )
    def update_bar_chart(districts: list[str]) -> html.Div:
        filtered_source = source.filter(districts=districts)
        print(districts)

        # Creating a dictionary to map category values to colors
        #color_map = {category: custom_colors[i % len(custom_colors)] for i, category in enumerate(df_plotly['Vict Descent'])}
        if not filtered_source.row_count:
            return html.Div("No data selected.")
        
        fig = px.bar(filtered_source.create_pivot_table(column_name= DataSchema.AREA), x=DataSchema.AREA, y='Frequency',
             template="plotly_dark", color=DataSchema.AREA,
             #color_discrete_map=color_map
             )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)



