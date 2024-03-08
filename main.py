from dash import Dash, html

def main() -> None:
    app = Dash()
    app.title = "Crime Dashboard"
    app.layout = html.Div(children="Hello World!")
    app.run(debug=True)

if __name__ == "__main__":
    main()