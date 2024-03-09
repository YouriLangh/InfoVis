from dash import Dash, html
from data.preprocess import load_and_preprocess_data
from pathlib import Path

def main() -> None:
    project_root = Path(__file__).parent.parent
    filepath = project_root / 'data' / 'Crime_Data_from_2010_to_2019.csv'
    data = load_and_preprocess_data(filepath)
    app = Dash()
    app.title = "Crime Dashboard"
    app.layout = html.Div(children="Hello World!")
    app.run(debug=True)

if __name__ == "__main__":
    main()