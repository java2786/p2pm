import pandas as pd

# sales_data = pd.DataFrame(python_list)
sales_data = pd.read_csv('sales.csv')

# first 5 rows
# print(sales_data.head())

# Date,Salesperson,Customer_Name
# print(sales_data[["Date","Salesperson","Customer_Name"]])

# select first row by index
# print(sales_data.iloc[0])

# select first three row by index
# print(sales_data.iloc[0:3])


# Convert the 'Cost_Per_KG' column to numeric, coercing any errors to NaN
# sales_data['Cost_Per_KG'] = pd.to_numeric(sales_data['Cost_Per_KG'].str.strip(), errors='coerce')
# print(sales_data[sales_data['Cost_Per_KG'] > 200])

# select by condition
# print(sales_data[
#     (sales_data['Quantity_KG'] > 20) 
# ])

print(sales_data[
    (sales_data['Quantity_KG'] > 20) &
    (sales_data['Salesperson'] == 'Priya Patel')
])


