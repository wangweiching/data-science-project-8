import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = '117th US House of Representatives'
charturl = 'https://plot.ly/python/choropleth-maps/'
sourceurl = 'https://www.kaggle.com/datasets/surajjha101/us-117th-house-of-representatives'
githublink = 'https://github.com/astever31/data-science-project-8'
# here's the list of possible columns to choose from.
list_of_columns = []

########## Set up the chart

import pandas as pd
df = pd.read_csv('sources/us-house-117.csv')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('117th US House of Representatives'),
    html.Div([
        html.Div([
                html.H6('Select a variable for analysis:'),
                dcc.Dropdown(
                    id='options-drop',
                    options=[{'label': i, 'value': i} for i in df[district]],
                    value=df[district][0],
                    optionHeight=50
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-1'),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Chart Source", href=charturl),
    html.Br(),
    html.A("Data Source", href=sourceurl),
]
)


# make a function that can intake any varname and produce a map.
@app.callback(Output('figure-1', 'figure'),
             [Input('options-drop', 'value')])
def make_figure(varname):
    mygraphtitle = f'Exports of {varname} in 2022'
    mycolorscale = 'sunset' # Note: The error message will list possible color scales.
    mycolorbartitle = "Millions USD"

    data=go.Choropleth(
        locations=df['test_state'], # Spatial coordinates
        locationmode = 'USA-states', # set of locations match entries in `locations`
        z = df[varname].astype(float), # Data to be color-coded
        colorscale = mycolorscale,
        colorbar_title = mycolorbartitle,
    )
    fig = go.Figure(data)
    fig.update_layout(
        title_text = mygraphtitle,
        geo_scope='usa',
        width=1200,
        height=800
    )
    return fig


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
