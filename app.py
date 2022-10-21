# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:50:33 2022

@author: USER
"""

import pandas as pd
import plotly.express as px

data=pd.read_excel('Treatment Data.xlsx')

df=data.groupby('Treatment Reason').mean()

df=df.reset_index()

df2=data.groupby('Gender').mean()

df2=df2.reset_index()


from dash import Dash,html, dcc
app=Dash(__name__)
server = app.server
fig = px.line(df, x="Treatment Reason", y="Treatment Duration in Minutes")
fig2 = px.bar(df2, x="Gender", y="Treatment Duration in Minutes", color='Gender')

fig3 = px.scatter(data, y="Age", color='Gender')

app.layout=html.Div(children=[html.H2(children='Treatmeant Reason', style={'color':'red',
                                                                         'text-style':'Italics'}),
                             html.H4(children='This is data analytic dashboard for visualization of treatment reason'),
                              
                              dcc.Graph(figure=fig),
                              dcc.Graph(figure=fig2),
                              
                              html.H2(children='Age Analysis', style={'margin-left':'200px'}),
                               dcc.Graph(figure=fig3),
                              
                              dcc.Input(id='my-input', value='initial value', type='text')
                             ])

app.run_server()