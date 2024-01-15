import pandas as pd
import plotly.express as px
import os

getdf = pd.read_csv('financials.csv', squeeze=True)

color_list = []
getdf_to_arr = pd.array(getdf['Share'])
for num in getdf_to_arr:
    if num > 0:
        color_list.append(int(1))
    elif num == 0:
        color_list.append(int(0))
    elif num < 0:
        color_list.append(int(-1))

#Adding the array to the main DataFrame
getdf['colorgrading'] = color_list


fig = px.treemap(getdf, path=[px.Constant("Market"), 'Sector', 'Symbol'], values='Price', color= 'colorgrading', color_continuous_scale= [[0, 'red'], [0.5, 'rgb(255, 255, 255)'], [1.0, 'rgb(0, 255, 0)']])
fig.update_traces(root_color= 'lightgreen')
fig.update_layout(margin = dict(t = 50, l = 25, r = 25, b = 25))
fig.show()
