# input number 1
# input number 2
# ask what to do => add, div, mul, square


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# sum, mul, div, minus, +, *, /, -
operator = input("Enter what to do: ")

print("num1: ",num1)
print("num2: ",num2)
print("Operator: ", operator)

# if(operator == "sum" or operator=="+"):
#     print(num1+num2) 
# else:
#     print("not sum")
# if operator == "div" or operator=="/":
#     print(num1/num2) 
# else:
#     print("not div")
# if operator == "mul" or operator=="*":
#     print(num1*num2) 
# else:
#     print("not mul")
# if operator == "minus" or operator=="-":
#     print(num1-num2) 
# else:
#     print("not minus")



if(operator == "sum" or operator=="+"):
    print(num1+num2) 
elif operator == "div" or operator=="/":
    print(num1/num2) 
elif operator == "mul" or operator=="*":
    print(num1*num2) 
elif operator == "minus" or operator=="-":
    print(num1-num2) 
else:
    print("not possible")

