import pandas as pd
import csv
import plotly.express as px

#to read the csv file using pandas
data = pd.read_csv("line_chart.csv")

line_chart = px.line(data, x = "Year", y = "Per capita income", color = "Country", title = "line chart")
line_chart.show()