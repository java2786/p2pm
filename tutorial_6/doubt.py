num = 4545
count = 0
even = 0
odd = 0
sum = 0
rev = 0
while num>0:
    digit = num%10
    if digit % 2 == 0:
        even = even+1
    else:
        odd = odd+1
    rev = rev*10 + digit
    sum = sum+digit
    count = count+1
    # even = digit
    num = num//10

print("Sum of num: " ,sum)
print("Count of num: " ,count)
print("Count of even: " ,even)
print("Count of odd: " ,odd)
print("reverse digit: " ,rev)