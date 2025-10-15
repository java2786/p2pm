# list, tuple, set, map

# Tuple -> 

# Employee info
# employee = "Ramesh", 32, "Software Engineer", "Pune"
# employee = ("Ramesh", 32, "Software Engineer", "Pune")
employee = tuple(["Ramesh", 32, "Software Engineer", "Pune"])
# index             0       1       2                   3

print(type(employee))

print("Name: ",employee[0])
print("Address: ", employee[len(employee)-1])
print("Address: ", employee[-1])
print("Range: ",employee[0:5]) # mislead

std = "Ramesh",38

# std[1] = 52

print(std)
