# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import dash

import dash_core_components as dcc

import dash_daq as daq

import dash_html_components as html

from dash.dependencies import Input, Output

 

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

 

df = pd.read_csv("Student_Perf_Casted.csv")
X = df[df.columns.difference(['Paper 7', 'Student_ID'])]

Y=df['Paper 7']

 

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

 

regressor = LinearRegression() 

regressor.fit(X_train, Y_train)

 

 

 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server=app.server

 

app.layout = html.Div([

       

    html.H1('Master Program Acceptance Predictor'),

       

    html.Div([  

    html.Label('Paper 1'),

    dcc.Slider(id='Paper 1-slider',

            min=0, max=100, step=1, value=10,

               marks={

        0: {'label': '0'},

        10: {'label': '10'},

        20: {'label': '20'},

        30: {'label': '30'},

        40: {'label': '40'} 
        
        50: {'label': '50'}  
        60: {'label': '60'}
        70: {'label': '70'}  
        80: {'label': '80'}
        90: {'label': '90'} 
        100: {'label': '100'}   

    }),

 

html.Br(),

  html.Label('Paper 2'),

    dcc.Slider(id='Paper 2-slider',

            min=0, max=100, step=1, value=10,

               marks={

        0: {'label': '0'},

        10: {'label': '10'},

        20: {'label': '20'},

        30: {'label': '30'},

        40: {'label': '40'} 
        
        50: {'label': '50'}  
        60: {'label': '60'}
        70: {'label': '70'}  
        80: {'label': '80'}
        90: {'label': '90'} 
        100: {'label': '100'}   

    }),

 

html.Br(),

  html.Label('Paper 3'),

    dcc.Slider(id='Paper 3-slider',

            min=0, max=100, step=1, value=10,

               marks={

        0: {'label': '0'},

        10: {'label': '10'},

        20: {'label': '20'},

        30: {'label': '30'},

        40: {'label': '40'} 
        
        50: {'label': '50'}  
        60: {'label': '60'}
        70: {'label': '70'}  
        80: {'label': '80'}
        90: {'label': '90'} 
        100: {'label': '100'}   

    }),

 

html.Br(),
  html.Label('Paper 4'),

    dcc.Slider(id='Paper 4-slider',

            min=0, max=100, step=1, value=10,

               marks={

        0: {'label': '0'},

        10: {'label': '10'},

        20: {'label': '20'},

        30: {'label': '30'},

        40: {'label': '40'} 
        
        50: {'label': '50'}  
        60: {'label': '60'}
        70: {'label': '70'}  
        80: {'label': '80'}
        90: {'label': '90'} 
        100: {'label': '100'}   

    }),

 

html.Br(),
  html.Label('Paper 5'),

    dcc.Slider(id='Paper 5-slider',

            min=0, max=100, step=1, value=10,

               marks={

        0: {'label': '0'},

        10: {'label': '10'},

        20: {'label': '20'},

        30: {'label': '30'},

        40: {'label': '40'} 
        
        50: {'label': '50'}  
        60: {'label': '60'}
        70: {'label': '70'}  
        80: {'label': '80'}
        90: {'label': '90'} 
        100: {'label': '100'}   

    }),

 

html.Br(),

  html.Label('Paper 6'),

    dcc.Slider(id='Paper 6-slider',

            min=0, max=100, step=1, value=10,

               marks={

        0: {'label': '0'},

        10: {'label': '10'},

        20: {'label': '20'},

        30: {'label': '30'},

        40: {'label': '40'} 
        
        50: {'label': '50'}  
        60: {'label': '60'}
        70: {'label': '70'}  
        80: {'label': '80'}
        90: {'label': '90'} 
        100: {'label': '100'}   

    }),
 


],className="pretty_container four columns"),

 

  html.Div([

 

    daq.Gauge(

        id='my-gauge',

        showCurrentValue=True,

        color={"gradient":True,"ranges":{"red":[0,0.4],"yellow":[0.4,0.7],"green":[0.7,1]}},

        label="Probability",

        max=1,

        min=0,

        value=1

    ),

])

    ])

 

 

@app.callback(

    Output('my-gauge', 'value'),

    [Input('Paper 1-slider', 'value'),

     Input('Paper 2-slider', 'value'),

     Input('Paper 3-slider', 'value'),

     Input('Paper 4-slider', 'value'),

     Input('Paper 5-slider', 'value'),

     Input('Paper 6-slider', 'value'),

     ])

def update_output_div(Paper 1,

                      Paper 2,

                      Paper 3,

                      Paper 4,

                      Paper 5,

                      Paper 6,):

   X_case =pd.DataFrame({'Paper 1':[Paper 1],'Paper 2':[Paper 2],'Paper 3':[Paper 3],'Paper 4':[Paper 4],'Paper 5':[Paper 5],'Paper 6':[Paper 6]})

   Y_case = regressor.predict(X_case)

 

   return Y_case[0]

 

 

if __name__ == '__main__':

    app.run_server()
