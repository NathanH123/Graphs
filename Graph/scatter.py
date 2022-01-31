import pandas as pd
import plotly.express as px
df = pd.read_csv("line_chart.csv")
figure = px.scatter(df,x = "Year", y = "Per capita income", color = "Country")
figure.show()