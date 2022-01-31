import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
figure = px.line(df, x = "Country", y = "InternetUsers")
figure.show()