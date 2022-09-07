import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd
import numpy as np
import os
import plotly as py
import plotly.express as px

# from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

########### Define your variables ######

tabtitle = 'US House'
sourceurl = 'https://www.kaggle.com/datasets/surajjha101/us-117th-house-of-representatives'
githublink = 'https://github.com/astever31/data-science-project-8'
myheading = 'Age Range Breakdown of 117th US House Reps, by State'
# here's the list of possible columns to choose from.
list_of_columns = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

########## Set up the chart

df = pd.read_csv('sources/us-house-117.csv')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading),
    html.Div([
        html.Div([
                html.H6('Select a state for analysis:'),
                dcc.Dropdown(
                    id='options-drop1',
                    options=[{'label': i, 'value': i} for i in list_of_columns],
                    value=list_of_columns[1]
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-2'),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


# make a function that can intake any varname and produce a map.
@app.callback(Output('figure-2', 'figure'),
             Input('options-drop1', 'value'))

def make_figure(varname):
    mycolorbartitle = "117th US House Reps"
    mygraphtitle = f'Age Range of 117th US House Reps of {varname}'
    colors = ['#3264A8','#A83232']
    #mycolorscale = 'Sunset' # Note: The error message will list possible color scales.
    
    data2 = df[df['clean_state']==varname].groupby(['age_range', 'party'])['name'].count()
    data2 = data2.unstack(level=-1)
    data2.reset_index(level=0, inplace=True)
    fig2 = px.bar(data2, x='age_range', y=['Democratic','Republican'],
              barmode='group',labels={'value':'number of reps','variable':'party'},color_discrete_sequence=colors)
    fig2.update_layout(
        width=1200,
        height=500,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig2

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)