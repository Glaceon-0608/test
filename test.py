import plotly.graph_objects as go
import pandas as pd
import time

df = pd.read_csv('https://raw.githubusercontent.com/Glaceon-0608/test/master/New_HIV2.csv') 

#year1990 = df[df["Year"] == 1990]

for i in range(28):
    a = df[df["Year"] == 1990+i]
    fig = go.Figure(data=go.Choropleth(
        locations = a['Code'],
        z = a['Incidence'],
        text = a['Entity'],
        colorscale = 'electric',
        reversescale=True,
        marker_line_color='gray',
        marker_line_width=0.5,
        colorbar_title = 'HIV Incidence',))
    fig.update_layout(title_text=str(1990+i)+' '+'HIV Incidence',)
    fig.show()
    time.sleep(1)
