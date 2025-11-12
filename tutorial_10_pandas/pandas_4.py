import pandas as pd

employees = pd.DataFrame({
    'Name': ['Ramesh', 'Suresh'],
    'Basic_Salary': [30000, 40000],
    'Exp': [3, 5]
})

print(employees)

employees.loc[0, 'Basic_Salary'] = 35000
employees.loc[employees['Exp'] > 4, 'Basic_Salary'] *= 1.10


employees['HRA'] = employees['Basic_Salary'] * .3
employees['MA'] = employees['Basic_Salary'] * .15
employees['DA'] = employees['Basic_Salary'] * .2

employees['Total_Salary'] = employees['Basic_Salary'] + employees['HRA'] + employees['MA'] + employees['DA']
print(employees)

emp = employees.drop('MA', axis=1)
print(emp)

print(emp['Basic_Salary'].sum())