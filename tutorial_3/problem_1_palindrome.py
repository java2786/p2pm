""" 

m a d a m
0 1 2 3 4

len(str) = 5


racecar => 7
0123456

navin

"""

str = "kamal"

# firstChar = str[0]
# lastChar = str[-1:]
# lastChar = len(str)-1

# print("First Char: ", firstChar)
# print("Last chars: ", lastChar)

# print("len: ",len(str))

# if(firstChar != lastChar):
#     print(f"{str} is not palindrome")
# else:
#     if(str[1]!=len(str)-2):
#         print(f"{str} is not palindrome")
#     else:
#         if(str[2]!=len(str)-3):
#             print(f"{str} is not palindrome")


#  m a d a m
if(str[0] != str[len(str)-1]):
    print(f"{str} is not palindrome")
elif(str[1]!=str[len(str)-2]):
    print(f"{str} is not palindrome")
elif(str[2]!=str[len(str)-3]):
    print(f"{str} is not palindrome")
else:
    print(f"{str} is palindrome")
