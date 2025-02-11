# import random
import plotly.graph_objects as go
import urllib, json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataexp = pd.read_csv('./Model_summary_DWDS.csv')
dataexp
#
# Create dimensions
dim1 = go.parcats.Dimension(values=dataexp['Topics'], label="Topics")
dim2 = go.parcats.Dimension(values=dataexp['Subtopics'], label="Subtopics")
dim3 = go.parcats.Dimension(values=dataexp['Models'], label="Models")

color = dataexp['Topics']

color = color.replace(['Machine learning to assess <br>and supoort safe drinking <br>water supply from the<br>physical aspect','Machine learning to assess <br>and supoort safe drinking <br>water supply from the<br>chemical aspect',\
                      'Machine learning to assess <br>and supoort safe drinking <br>water supply from the<br>microbiological aspect','Machine learning to assess <br>and supoort safe drinking <br>water supply from the<br>temporal aspect'],
                      ['#7955fa','#4F9DA6','#FFAD5A','#FF5959'])  


fig = go.Figure(data=[go.Parcats(dimensions=[dim1, dim2, dim3],
        line={'color': color,
              #'colorscale': colorscale,
              'shape': 'hspline'},
        #hoveron='color',
        hoverinfo='none',
        labelfont={'size': 40},  #30
        tickfont={'size': 25},   #16
        arrangement='freeform')])

fig.update_layout(width=2500, height=1800, margin=dict(l=520, r=200, t=50, b=50))
fig.update_layout(font=dict(family="Times New Roman Bold, serif"))
fig.write_image("./Sankey_diagram_DWDS.pdf")
fig.show()

