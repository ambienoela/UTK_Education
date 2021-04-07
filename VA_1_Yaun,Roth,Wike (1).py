from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas_datareader import data
import pandas as pd




# ___________Visualization Assignment 1 ______________________
#
#       Due by 11:59pm on April 2, 2021
#
#
#       *** Joseph Wike, Amber Roth, Marah Yuan ***
#
#
#
# Submit a file with .py extension 
#
#   To start use python script file  my_app_10.py (the code is copied below)
#
#
# A: Pick a company of your choice 
# Find out the company's ticker
# (cannot be any mentionned in class ['^DJC', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT', 'GOOGL', 'TSLA', 'AAPL'])
#
# B: Using pandas_datareader read the company's index from yahoo finance.
# C: Provide the companies name as a comment in the code
#
# D: Modify the code to plot difference between High and Low prices 
# E: Make sure that the Input box shows the correct ticker
# F: Change the header to show an appropriate text (mention the company's name...)
#
#
#######################################################################
# Grading:
#
# This assignement is worth 20 points.
# If your file throws a syntax error, max you can earn is 10 points
#
#
#        
# ___________Visualization Assignment 1 ______________________



my_app = Dash('my app')

df1 = data.DataReader('PG','yahoo')
df1=df1[df1.index>="2019-1-1"] # This line will get rid of data for earlier than Jan 1 of 2019

my_app.layout = html.Div( style={"background" : "#b0c2ff"},
                children=[    # here is the list of components/children     

                    html.H1('Difference Between High and Low Stock Values of P&G',style={"textAlign" : "center", "color": "Black", 'backgroundColor': '#b0c2ff'}),   # this is a header           html.H1('   ')            
                    html.H1('BAS 476 Visualization Project | Marah Yuan, Joseph Wike, Amber Roth',style={"textAlign" : "center", "color": "Black", 'backgroundColor': '#b0c2ff'}),
                    html.Label('Company: '),     # this is a label            html.Label(' ')

                    dcc.Input(                  # this is an input box       dcc.Input(value=   , id=   )
                               value="PG",      
                               id='my_input'
                              ),

                    html.Div(      # this is another divider that is a "child" of the main divider 
                              id = 'my_graph',   # it has an ID and will have only one child (next line)
                              
                              children = dcc.Graph(figure = {'data' : [    # here is a list that may have several dictionaries for plots
                                                                       {'x': df1.index, 'y': df1.High.values-df1.Low.values, 'name': "PG","line": dict(color="Blue",width=4)}  # x and y values to plot
                                                                      ],
                                                             'layout' : {'plot_bgcolor':"Black",
                                                                         'paper_bgcolor': "#b0c2ff",
                                                                         'font': {'color': "Black", "size": 12},
                                                                         "height": 600,
                                                                         'width': 1270
                                                                        }
                                                            }
 
                                                   )
                            )       
                   ]
                        )



if __name__ == '__main__':
    my_app.run_server(debug=True)
