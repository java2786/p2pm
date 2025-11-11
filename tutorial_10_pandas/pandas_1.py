import pandas as pd
"""
panda => pan da => panel + data
Pandas has two main component:
    1. Series - single column data - array
    2. DataFrame - table - row and column
"""



cities = pd.Series(["Mumbai", "Delhi", "Chennai", "Pune", "Bangalore"])

print("Cities (Series): ")
print(cities)


# emp = pd.DataFrame({
#     "name": "Ramesh",
#     "age": 32,
#     "contact": ("67485748", "demo@gmail.com")
# })

# print(emp)

employees_data = pd.DataFrame({
    'Name': ['Suresh', 'Ramesh', 'Mahesh', 'Dinesh'],
    'Age': [25,28,24,27],
    'Cities': ["Pune", "Mumbai", "Chennai", "Delhi"],
    'Salary': [35000, 42000, 38000, 45000],
    'Id': ["bm1934", "bm7863", "bm8873", "bm9234"]
})
print("Employees DataFrame: ")
print(employees_data)

students = [
    ['Suresh', 85, 'A'],
    ['Ramesh', 92, 'A+'],
    ['Mahesh', 78, 'B'],
    ['Dinesh', 88, 'A'],
    ['Hitesh', 77, 'B']
]
students_data = pd.DataFrame(students, columns=["Name", 'Marks','Grade'])
print("\n\n\n\n")
# print("Name\tMarks\tGrade")
print(students_data)