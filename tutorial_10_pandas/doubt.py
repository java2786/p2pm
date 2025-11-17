import pandas as pd

sales_data = pd.read_csv('sales2.csv')

# Convert the 'Cost_Per_KG' column to numeric, coercing any errors to NaN
# sales_data['Demo'] = pd.to_numeric(sales_data['Demo'].str.strip(), errors='coerce')
print(sales_data[sales_data['Demo'] > 200])