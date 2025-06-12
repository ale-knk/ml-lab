# dash_app/callbacks.py

from dash import Input, Output, html
from dash_app import app
from dash_app.components.new_training_form import new_training_form

print("[DEBUG] callbacks.py loaded")

def render_tab_content(tab):
    if tab == "tab-new-training":
        return html.Div([
            new_training_form()
        ])
    elif tab == "tab-experiment-history":
        return html.Div("Experiment history table")
    elif tab == "tab-run-details":
        return html.Div("Selected run details")
    elif tab == "tab-registered-models":
        return html.Div("Registered models catalog")
    elif tab == "tab-configuration":
        return html.Div("System configuration and status")
    return html.Div("View not found")

@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "value")
)
def switch_tab(tab_value):
    print(f"[DEBUG] switch_tab triggered with value = {tab_value}")
    return render_tab_content(tab_value)
