import csv
import pandas as pd
import plotly.express as px
scatterdata = pd.read_csv("data.csv")
scatterplot = px.scatter(scatterdata, x = "Population", y = "Per capita", size = "Percentage", color = "Country")
scatterplot.show()
