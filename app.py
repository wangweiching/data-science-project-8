import dash
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
