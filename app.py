import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd

drinks=['Coca-Cola', 'Gatorade', 'Cranberry Juice', 'Apple Juice', 'Coconut Water']
sugar_values=[10, 5, 11, 10, 5]
calorie_values=[14, 9.7, 20.5, 15.9, 9.9]
color1='darkblue'
color2='lightblue'
mytitle='Beverage Comparison'

label1='Sugar, tsp'
label2='Calories, divided by 10'

########### Set up the chart

def make_that_cool_barchart(drinks, sugar_values, calorie_values, color1, color2, mytitle):
    sugar_content = go.Bar(
        x=drinks,
        y=sugar_values,
        name=label1,
        marker={'color':color1}
    )
    calories = go.Bar(
        x=drinks,
        y=calorie_values,
        name=label2,
        marker={'color':color2}
    )

    drink_data = [sugar_content, calories]
    drink_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    drink_fig = go.Figure(data=drink_data, layout=drink_layout)
    return drink_fig

######## Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(drinks, sugar_values, calorie_values, color1, color2, mytitle)
    fig.write_html('docs/barchart.html')
    print('Barchart update successful.')


'''########### Define your variables ######

tabtitle = '117th US House of Representatives'
charturl = 'https://plot.ly/python/choropleth-maps/'
sourceurl = 'https://www.kaggle.com/datasets/surajjha101/us-117th-house-of-representatives'
githublink = 'https://github.com/astever31/data-science-project-8'
# here's the list of possible columns to choose from.
list_of_states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

########## Set up the chart

import pandas as pd
df = pd.read_csv('sources/us-house-117.csv')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the chart
results = df.groupby(['age_range', 'party'])['name'].count()
results = results.unstack(level=-1)
results.reset_index(level=0, inplace=True)
fig = results.plot(x='age_range', y=['Democratic', 'Republican'], kind='bar');

#beer_fig = go.Figure(data=beer_data, layout=beer_layout)
########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)'''