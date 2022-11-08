import dash
from dash.dependencies import Input, Output
from dash import dcc, html
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Hello World')

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'BRI', 'value': 'BBRI.JK'},
            {'label': 'BCA', 'value': 'BBCA.JK'},
            {'label': 'TELKOM', 'value': 'TLKM.JK'},
            {'label': 'FILM', 'value': 'FILM.JK'},
            {'label': 'KOTA', 'value': 'KOTA.JK'}
        ],
        value='BBRI.JK'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2019, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close, 
            
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

dash.Dash('Hello World')


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=true)
