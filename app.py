from argparse import ArgumentParser
from dash import Dash, html
from pathlib import Path
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP
from src.data.loader import load_combined_data
from src.data.source import DataSource
from src.data.fetch import fetch_datasets


def main(args) -> None:
    fetch_datasets()
    project_root = Path(__file__).parent
    filepath = project_root / 'data' / 'Crime_Data_20_Year_Analysis.csv'
    data = load_combined_data(filepath)
    data = DataSource(data)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Crime Dashboard"
    app.layout = create_layout(app, data)
    app.run(debug=args.debug)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()
    main(args)
