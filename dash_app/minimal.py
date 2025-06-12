import dash
from dash import dcc, html
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = html.Div([
    dcc.Tabs(id="tabs", value="a", children=[
        dcc.Tab(label="A", value="a"),
        dcc.Tab(label="B", value="b"),
    ]),
    html.Div(id="out")
])
@app.callback(
    dash.Output("out", "children"),
    dash.Input("tabs", "value")
)
def cb(v):
    print("tab changed to", v)
    return f"Selected {v}"
if __name__=="__main__":
    app.run(debug=True)
