import pandas as pd

date_cols = ["x"]
df = pd.read_csv("sentiment.csv", parse_dates=date_cols)
df.index = df['x'] 
print(df.resample('M').mean())
