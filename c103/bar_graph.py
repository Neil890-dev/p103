import csv
import pandas as pd
import plotly.express as px
bardata=pd.read_csv("data.csv")
bargraph=px.bar(bardata, x = "Country", y = "InternetUsers")
bargraph.show()