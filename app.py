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
# here's the list of possible columns to choose from.
list_of_columns = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

########## Set up the chart

df = pd.read_csv('sources/us-house-117.csv')

########## US States to Code
us_state_to_abbrev = {
    "Alaska": "AK",
    "Alabama": "AL",
    "Arkansas": "AR",
    "Arizona": "AZ",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Iowa": "IA",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Virginia": "VA",
    "Vermont": "VT",
    "Washington": "WA",
    "Wisconsin": "WI",
    "West Virginia": "WV",
    "Wyoming": "WY",
}
df['Code'] = df['clean_state'].map(us_state_to_abbrev)
#df=df[df['Age Group']!='25 and older']

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Age Range Breakdown of 117th US House Reps, by State'),
    html.Div([
        html.Div([
                html.H6('Select a state for analysis:'),
                dcc.Dropdown(
                    id='options-drop1',
                    options=[{'label': i, 'value': i} for i in list_of_columns],
                    value='Arizona'
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-1'),
            ], className='five columns'),
        html.Div([dcc.Graph(id='figure-2'),
            ], className='five columns'),
    ], className='twelve columns'),
    '''html.Div([
        html.Div([
                html.H6('Select a major for analysis:'),
                dcc.Dropdown(
                    id='options-drop2',
                    options=[{'label': i, 'value': i} for i in list_of_columns],
                    value='Arts, Humanities and Others'
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-3'),
            ], className='five columns'),
        html.Div([dcc.Graph(id='figure-4'),
            ], className='five columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),'''
    ]
)


# make a function that can intake any varname and produce a map.

def make_figure(varname):
    mycolorbartitle = "117th US House Reps"
    mygraphtitle = f'Age Range of 117th US House Reps of {varname}'
    #mycolorscale = 'Sunset' # Note: The error message will list possible color scales.
    
    '''major = pd.DataFrame(df,columns = ['Code','Sex',varname])
    major[varname] = major[varname].replace(",","", regex=True).astype(float)
    total = major[major['Sex']=='Total'].groupby(['Code'],as_index = False).sum().rename(columns={varname:"Total"})
    female = major[major['Sex']=='Female'].groupby(['Code'],as_index = False).sum().rename(columns={varname:"Female"})
    male = major[major['Sex']=='Female'].groupby(['Code'],as_index = False).sum().rename(columns={varname:"Male"})
    female_rate = pd.DataFrame()
    female_rate['Code']  = df['State'].map(us_state_to_abbrev)
    female_rate = pd.merge(female,male,on=['Code']).merge(total,on=['Code'])
    female_rate['Female Rate'] = female_rate['Female']/female_rate['Total']'''
    
    data2 = df[df['clean_state'] == varname].groupby(['age_range', 'party'])['name'].count()
    data2 = data2.unstack(level=-1)
    data2.reset_index(level=0, inplace=True)
    color_discrete_sequence = ['#009ACD','#FFB6C1']
    fig2 = px.bar(data2, x="Code", y=varname, 
                 color="party", barmode="group",color_discrete_sequence=color_discrete_sequence)
    fig2.update_layout(
        width=1200,
        height=500,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig2

@app.callback(Output('figure-2', 'figure'),
             Input('options-drop1', 'value'))

def figure_callback1(varname):
    return make_figure(varname)

'''@app.callback(Output('figure-3', 'figure'),
             Output('figure-4', 'figure'),
             Input('options-drop2', 'value'))

def figure_callback2(varname):
    return make_figure(varname)'''

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)

'''import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go
import pandas as pd

########### Define your variables
tabtitle='US House'
myheading='117th US House of Representatives'
githublink='https://github.com/astever31/data-science-project-8'
sourceurl='https://www.kaggle.com/datasets/surajjha101/us-117th-house-of-representatives'
color1='darkblue'
color2='darkred'
mytitle='Age Range of 117th House of Representatives'
label1='Democrats'
label2='Republicans'

########### Set up the chart
df2 = pd.read_csv('sources/us-house-117-ages.csv')

democrats = go.Bar(
    x=df2["age_range"],
    y=df2["Democratic"],
    name=label1,
    marker={'color':color1}
)
republicans = go.Bar(
    x=df2["age_range"],
    y=df2["Republican"],
    name=label2,
    marker={'color':color2}
)

data = [democrats, republicans]
layout = go.Layout(
    barmode='group',
    title = mytitle
)

fig = go.Figure(data=data, layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='ushouse',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
'''