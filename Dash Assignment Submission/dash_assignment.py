#!/usr/bin/env python
# coding: utf-8

# In[50]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Uses an External Stylesheet
# Use a css file from your GitHub Pages site 
external_stylesheets = ['https://sourabhreddy369.github.io/sourabh.github.io/StyleSheet.css']

# Creates the app to instantiate the content for the Dashboard and use the external_stylesheets
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Use a csv dataset from a repository in your GitHub account. Use the Raw URL to expose the data to the Python dataframe
df = pd.read_csv('https://raw.githubusercontent.com/sourabhreddy369/dash_data/master/cereal.csv')
df2 = df
df2 = df2.sort_values(by=['rating'], ascending = False)
df2 = df2.head(10)
df3 = df2.sort_values(by=['calories'], ascending = False)
df3 = df3.head(10)
df4 = df2.sort_values(by=['protein'], ascending = False)
df4 = df4.head(10)
  

fig3 = px.pie(df4.head(10), values='protein', names='name',
             title='Cereals with high protein content and their rating',
             hover_data=['rating'], labels={'rating':'rating'})
# Custom function used to generate a data table from a dataframe
def generate_table(dataframe, max_rows=16):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Add content to the app layout
# Begin all content DIV
app.layout=html.Div([
    # Add your HTML tags to the content - notice a comma is added between HTML elements
    html.H1('Data Visualization for Story Telling - Python Dash Assignment'),
    html.Div([
        html.P('Nutrition data of 80 cereal products ...'),
    ]),
    # Begin of DIV surrounding both Tables
    html.Div([
    # Begin of First Table
    html.Table(style={'width':'100%'},
               # Begin of Table children
               children=[
                   #######################################################################
                   # Begin of First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         
                         html.Th(style={'width':'30%'},
                             # Begin Th children
                             children=[
                                 html.H3('Cereals to consider for purchase based on rating level ')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Th
                         html.Th(style={'width':'70%'},
                             # Begin of Th children
                             children=[
                                 html.H3('All Details of Cereals')
                             # End of Th children    
                             ]
                         
                         # End of Th
                         )
                         
                     # End of Tr children    
                     ]
                 # End of First Tr - Notice a comma is placed here to separate the next Tr
                 ),
                 #########################################################################
                 # Begin of Second Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Td
                         html.Td(
                             # Begin Td children
                             children=[
                                 # Display plot graph use data from dataframe df
                                 dcc.Graph(
                                    id='life-exp-vs-gdp',
                                figure={
                                    'data': [
                                        dict(
                                            x = df2['name'],
                                            y = df2['rating'],
                                            type ='bar',
                                        )
                                    ], 'layout': {
                                            'title': 'Rating of different Cereals'}
                                    # End of 2nd Inner DIV
                                    })
                           
                             # End of Td children    
                             ]
                         
                         # End of Td - Notice a comma is placed here to separate the next Th
                         ),
                         html.Td(
                             # Begin of Td children
                             children=[
                                    # Execute custom generate_table function and display data
                                    # Use data from dataframe df2
                                    generate_table(df)
                             # End of Td children    
                             ]
                         # End of Td
                         )
                     # End of Tr children    
                     ]
                 # End of Tr
                 )     
                #########################################################################                   
               #End of Table Children    
               ]
              # End of First Table - Notice a comma is placed here to separate the next Table
              ),
        #############################################################################################################
       
     # Begin of Second Table
        
    html.Table(style={'width':'100%'},
               children=[
                 #######################################################################
                 # Begin First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         html.Th(style={'width':'30%'},
                             # Begin Th children
                             children=[
                                 html.H3('Cereals which has more calorie content')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Th
                         html.Th(style={'width':'70%'},
                             # Begin of Th children
                             children=[        
                                    html.H3('Top 10 cereals with high protein content')
                                                               
                             # End of Th children    
                             ]
                         # End of Th
                         )
                     # End of Tr children    
                     ]
                 # End of First Tr
                 ),
                   
                ######################################################################
                # Begin of Second Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Td
                         html.Td(
                             # Begin Td children
                             children=[
                                 # Display plot graph use data from dataframe df
                                 dcc.Graph(
                                    id='life-exp-vs-gdp2',
                                figure={
                                    'data': [
                                        dict(
                                            x=df3['name'],
                                            y=df3['calories'],
                                            type = 'line'
                                        )
                                    ], 'layout': {
                                            'title': 'Top 10 cereals which has more calories'}
                                    # End of 2nd Inner DIV
                                    })
                           
                             # End of Td children    
                             ]
                         
                         # End of Td - Notice a comma is placed here to separate the next Th
                         ),
                         
                         # Begin of Td
                         html.Td(
                             # Begin of Td children
                             children=[
                               
                                 dcc.Graph(figure=fig3)
#                                      dcc.Graph(
#                                     id='life-exp-vs-gdp3',
#                                 figure={
#                                     'data': [
#                                         dict(
#                                             x=df4['name'],
#                                             y=df4['protein'],
#                                             mode = 'markers'
#                                         )
#                                     ], 'layout': {
#                                             'title': 'Top 10 cereals which has more protein content'}
#                                     # End of 2nd Inner DIV
#                                     })
                             # End of Td children    
                             ]
                         # End of Td
                         )
                     # End of Tr children    
                     ]
                 # End of Second Tr
                 )     
               
               #######################################################################
               #End of Table Children    
               ]
              #########################################################################################
              # End of Second Table - Notice a comma is placed here to separate the next Content
              ),
    # End of DIV surrounding both Tables
    ]),
               
# End of all content DIV
])

# Run the app on the web server
if __name__ == '__main__':
    # Set debug to False. Some configurations are not setup for Debug
    app.run_server(debug=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




