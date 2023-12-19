import pandas as pd
import plotly.express as px
import os

mycsvdir = 'sp500'
getcsvfile = os.path.join(mycsvdir, "financials.csv")
df = pd.read_csv(getcsvfile)

fig = px.treemap(df, path=[px.Constant("Market"), 'Sector', 'Symbol'], values='Price')
fig.update_traces(root_color= 'lightgreen')
fig.update_layout(margin = dict(t = 50, l = 25, r = 25, b = 25))
fig.show()