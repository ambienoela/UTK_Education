#pip3 install dash==1.4.1
#pip3 install dash-daq==0.2.1
#pip3 install pandas-datareader
# ___________Visualization Assignment 2 ______________________
#
#       Due by 11:59pm on April 9, 2021
#
#
#       *** Joseph Wike, Marah Yaun, and Amber Roth ***
#
#
#
# Submit a file with .py extension 
#
#   To start use python script file  my_app_12_callback.py (the code is copied below)
#
#
# A: Pick 2 companies of your choice 
# Find out the companies' tickers
# (cannot be any mentioned in class ['^DJC', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT', 'GOOGL', 'TSLA', 'AAPL'])
# B: Using pandas_datareader read both companies data from yahoo finance (in two different dataframes).
# C: Provide the companies' names as a comment in the code
# 
#
# D: Change the header to an appropriate text (ex. Vis. hw 2, or Company One and Two __ data, etc...)
# E: Add a label and Input box for the second company.
#
#
# F: Add another label and an Input box
#    Label should display "Enter High or Low"
#    Input box should display "High" at the start
#
# G. Show/plot Both companies' "High" values on the same graph (you will have two traces on the same plot) 
#
# H: Modify the Callback:
# - For any changes in either company's ticker the plot should update accordingly
# - If an user enters "Low" in the High/Low Input box, the plot should display/plot Low values for both companies
# - If an user enters "High" in the High/Low Input box, the plot should display/plot High values for both companies
#
# - The code should work if the user enters values more than once
# (going from "High" to "Low", back to "High", and do so for several companies).  
#
#######################################################################
# Grading:
#
# This assignment is worth 20 points.
# If your file throws a syntax error, max you can earn is 10 points

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas_datareader import data
import pandas as pd


my_app = Dash('my app')


df = data.DataReader('PG','yahoo')
df2 = data.DataReader('JNJ','yahoo')
start_date="2018-1-1"



my_app.layout = html.Div(children=[
    
 html.H1('Visualization HMWK 2: Company One and Two',style={"textAlign" : "center", "color": "Black", 'backgroundColor': '#b0c2ff'}),   # this is a header           html.H1('   ')            
 html.H1('BAS 476 Visualization Project | Marah Yuan, Joseph Wike, Amber Roth',style={"textAlign" : "center", "color": "Black", 'backgroundColor': '#b0c2ff'}),
    
      html.Label('Company 1: ', style={'backgroundColor': '#b0c2ff'}),
    
 dcc.Input(
     value="PG",
     id='my_input'
 ),

 html.Div(id="NewDiv",
          children =[
              html.Label('Company 2: ', style={'backgroundColor': '#b0c2ff'}),
              dcc.Input(value="JNJ", id='my_input_2')
              ]
          ),
  html.Div(id="Div",
          children =[
              html.Label('Enter High or Low: ', style={'backgroundColor': '#b0c2ff'}),
              dcc.Input(value="High", id='my_high')
              ]
           ),
              
    
 html.Div(
     id = 'my_graph',
      children = dcc.Graph(figure = {'data' : [    # here is a list that may have several dictionaries for plots
                                                                       {'x': df.index, 'y': df.High.values, 'name': "PG","line": dict(color="Navy",width=4)},  # x and y values to plot
                                                                       {'x': df2.index, 'y': df2.High.values,'name': "JNJ","line": dict(color="Maroon",width=4)}
                                                                      ],
                                                             'layout' : {'plot_bgcolor':"White",
                                                                         'paper_bgcolor': "#b0c2ff",
                                                                         'font': {'color': "Black", "size": 10},
                                                                         "height": 600,
                                                                         'width': 1270
                                                                           }
                                                            }
 ))
 ])  


# do something before a function
# run a function
# do something after the function run


@my_app.callback(  # Output, [Input])
    Output(component_id='my_graph', component_property='children'),
   
    [Input(component_id='my_input',component_property='value'),
     Input(component_id='my_input_2',component_property='value'),
     Input(component_id='my_high',component_property='value')]
     )
                
def update_graph(ticker_1, ticker_2, high_values):
    df = data.DataReader(ticker_1,'yahoo')
    df2 =data.DataReader(ticker_2, 'yahoo')
    # if statement for high and low values, if too high, if too low...

    if high_values=='High':
        graph = dcc.Graph(figure = { 'data' : [{'x': df.index, 'y': df.High.values,"line": dict(color="blue",width=5), 'name' : ticker_1},
                                           {'x': df2.index, 'y': df2.High.values,"line": dict(color="red",width=5), 'name' : ticker_2}],
                                     'layout' : {'plot_bgcolor':"White",
                                                                         'paper_bgcolor': "#b0c2ff",
                                                                         'font': {'color': "Black", "size": 10},
                                                                         "height": 600,
                                                                         'width': 1270
                                                                           }# updated graph   
                                }
                      )
    else:
        graph = dcc.Graph(figure = { 'data' : [{'x': df.index, 'y': df.Low.values,"line": dict(color="blue",width=5), 'name' : ticker_1},
                                           {'x': df2.index, 'y': df2.Low.values,"line": dict(color="red",width=5),'name' : ticker_2}],
                                     'layout' : {'plot_bgcolor':"White",
                                                                         'paper_bgcolor': "#b0c2ff",
                                                                         'font': {'color': "Black", "size": 10},
                                                                         "height": 600,
                                                                         'width': 1270
                                                                           }# updated graph   
                                }
                      )
    return graph

if __name__ == '__main__':
    my_app.server.run(debug=True)
