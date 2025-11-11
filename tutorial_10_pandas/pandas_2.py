import pandas as pd

# pd.read_csv('sales.excel')
df = pd.read_csv('sales.csv')

# first 5 rows
print(df.head())

# last 5 rows
print(df.tail())

# columns
print(df.columns)

# basic info
print(df.info())

# shape (row, column)
print(df.shape)