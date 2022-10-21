
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


import plotly.express as px


# In[7]:


data1=pd.DataFrame({'Years':[2017,2016,2015,2014,2013,2012],'Percentage':[0.18,-1.62,2.65,6.31,6.67,4.23]})


# In[8]:


data2=pd.DataFrame({'Years':[2017,2016,2015,2014,2013,2012],'Percentage':[105.82,109.45,112.79,123.62,127.00,138.22]})


# In[9]:


data3=pd.DataFrame({'Years':[2017,2016,2015,2014,2013,2012],'Percentage':[2.64,2.66,2.68,2.67,2.71,2.72]})


# In[10]:


data4=pd.DataFrame({'Years':[2017,2016,2015,2014,2013,2012],'Percentage':[8.39,7.06,4.31,4.56,3.70,3.74]})


# In[ ]:


from dash import Dash,html,dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
fig1 = px.line(data1,x='Years',y='Percentage', title='GROSS DOMESTIC PRODUCT(GDP)OF Nigeria FROM 2012-2017')
fig2 = px.line(data2,x='Years',y='Percentage', title='Deaths from malaria in Nigeria FROM 2012-2017')
fig3 = px.line(data3,x='Years',y='Percentage', title='Population growth rate in Nigeria FROM 2012-2017')
fig4 = px.line(data4,x='Years',y='Percentage', title='Unemployment rate in Nigeria FROM 2012-2017')

app=Dash(__name__)
server=app.server
app.title= 'DIFFERENT INDICATORS IN NIGERIA AND THEIR PERCENTAGE FROM 2012-2017'

app.layout=html.Div(children=[html.H1(children='DIFFERENT INDICATORS IN NIGERIA',
                                      style={'color':'green','background-color':'gray'}),
                             
dcc.Input(id='num', type='number'),
            html.Button('Click here to see the content', id='show-secret'),
            html.Div(children=[dcc.Graph(figure=fig1)
                    ], style={'width':'50%','float':'left'}),
            html.Div(children=[html.H1('Death rate from malaria'),dcc.Graph(figure=fig2)
                    ], style={'width':'50%','float':'right'}), 
            html.Div(children=[dcc.Graph(figure=fig3)
                    ], style={'width':'50%','float':'left'}), 
            html.Div(children=[dcc.Graph(figure=fig4)
                    ], style={'width':'50%','float':'right'}) 
                             ])
            
app.run_server()

