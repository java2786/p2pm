num = 40, 80, 68, 91, 40
print(type(num))

total = sum(num)
avg = total/len(num)
max = max(num)
if avg >80:
    print("Grade: A")
elif avg <=80 and avg >60:
    print("Grade: B")
elif avg >=40 and avg <=60:
    print("Grade: C")
else:
    print("Fail")
print("Highest num:", max)
print("Average num:", avg)
print("Total num:", total)