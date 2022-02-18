import pandas as pd
import plotly.express as ps

df=pd.read_csv("data.csv")
d=df["country"].tolist()
n=df["cases"].tolist()
s=df["date"].tolist()
h=ps.scatter(color=d ,y=s ,x=n )
h.show()
