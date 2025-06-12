import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback
import yaml
from dash_app import app

def load_pipeline_def(path=None, content=None):
    if content:
        return yaml.safe_load(content)
    elif path:
        with open(path) as f:
            return yaml.safe_load(f)
    return {}

# UI for loading YAML
def new_training_form():
    return dbc.Container([
        html.H2("Launch New Training", className="mb-4"),

        dbc.Row([
            dbc.Col([
                dbc.Label("YAML Content"),
                dcc.Textarea(id="yaml-content", style={"width": "100%", "height": "200px"}, placeholder="Paste pipeline YAML here...")
            ], md=6),
            dbc.Col([
                dbc.Label("YAML File Path"),
                dbc.Input(id="yaml-path", placeholder="e.g. /path/to/pipeline.yaml", type="text")
            ], md=6),
        ], className="mb-3"),

        dbc.Button("Load Pipeline", id="load-pipeline", color="secondary", className="mb-4"),

        html.Div(id="pipeline-form")
    ], fluid=True)

@callback(
    Output("pipeline-form", "children"),
    Input("load-pipeline", "n_clicks"),
    Input("yaml-path", "value"),
    Input("yaml-content", "value")
)
def render_pipeline_form(n, path, content):
    if not n:
        return html.Div()
    pipeline = load_pipeline_def(path=path, content=content)
    steps = pipeline.get("steps", [])
    if not steps:
        return html.Div("No steps defined in YAML.")

    # Step selector
    form_children = [
        dbc.Row([
            dbc.Col([
                dbc.Label("Step"),
                dcc.Dropdown(
                    id="step-selector",
                    options=[{"label": s.get("name"), "value": s.get("name")} for s in steps],
                    value=steps[0].get("name")
                )
            ], md=6)
        ], className="mb-3")
    ]

    # Container for params
    form_children.append(html.Div(id="step-params"))
    # Launch button
    form_children.append(
        dbc.Row([
            dbc.Col([
                dbc.Button("Launch Training", id="launch-training", color="primary"),
                html.Span(id="training-feedback", className="ms-3")
            ])
        ])
    )
    return html.Div(form_children)

@callback(
    Output("step-params", "children"),
    Input("step-selector", "value"),
    Input("load-pipeline", "n_clicks"),
    Input("yaml-path", "value"),
    Input("yaml-content", "value")
)
def render_step_params(step_name, n, path, content):
    if not n or not step_name:
        return html.Div()
    pipeline = load_pipeline_def(path=path, content=content)
    step = next((s for s in pipeline.get("steps", []) if s.get("name")==step_name), {})
    params = step.get("params", {})
    rows = []
    for key, meta in params.items():
        rows.append(
            dbc.Row([
                dbc.Col([
                    dbc.Label(key),
                    dbc.Input(
                        id={"type": "param-input", "index": key},
                        type=meta.get("type", "text"),
                        value=meta.get("default"),
                        step=meta.get("step")
                    )
                ], md=4)
            ], className="mb-3")
        )
    return html.Div(rows)
