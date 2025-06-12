# dash_app/app.py
from dash_app import app, server
from dash_app.layouts import layout

app.layout = layout

# esto asegura que callbacks.py vea el mismo `app`
import dash_app.callbacks

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
