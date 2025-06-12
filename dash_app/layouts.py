# dash_app/layouts.py

from dash import dcc, html

layout = html.Div([
    html.H1("ML Lab - MLOps Environment", style={"textAlign": "center", "margin": "20px"}),

    dcc.Tabs(id="tabs", value="tab-new-training", children=[
        dcc.Tab(label="🧪 New Training", value="tab-new-training"),
        dcc.Tab(label="📊 Experiment History", value="tab-experiment-history"),
        dcc.Tab(label="🧬 Run Details", value="tab-run-details"),
        dcc.Tab(label="📦 Registered Models", value="tab-registered-models"),
        dcc.Tab(label="⚙️ Configuration", value="tab-configuration"),
    ]),
    
    html.Div(id="tab-content", style={"padding": "20px"})
])
