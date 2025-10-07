# name = "book"
# last_char = name[-1:]
# print(last_char)
# print(type(name))

num = 223322
copy = num
print(type(num))
reverse = 0

# num//10 => remove last digit
# num%10 => last digit
while(num>0):
    ld = num%10
    reverse = (reverse * 10) + ld
    num = num//10


print(f"Reverse: {reverse}")
num = copy
if reverse == num:
    print(f"{num} Palindrome found")
else:
    print(f"{num} Not palindrome")