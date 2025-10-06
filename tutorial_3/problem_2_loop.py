str = "naveen"
count = 0
isPalindrom = True

while(count < len(str)//2):
    if(str[count] != str[len(str)-1-count]):
        
        isPalindrom = False
        break
    count = count + 1

if isPalindrom == True:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")
    
# number 10001, 43734, 232, 11, 454