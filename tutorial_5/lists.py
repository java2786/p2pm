# name1 = "Ramesh"
# name2 = "Mahesh"
# name3 = "Rajesh"
# name4 = "Dinesh"

# score1 = 48
# score2 = 72
# score3 = 81
# score4 = 91

# []
#           0.        1.        2.         3.        4
names = ["ramesh", "suresh", "mukesh", "mahesh", "dinesh", "kamlesh"]
scores =[34, 56, 92, 83, 97, 62]
address = ["delhi", "pune", "bangalore", "pune", "delhi", "mumbai"]

print("Total count: ",len(names))
print("At index 2:", names[2])


# print(f"{names[0].upper()} has scored {scores[0]} marks and lives in {address[0].capitalize()}.")
# print(f"{names[1].upper()} has scored {scores[1]} marks and lives in {address[1].capitalize()}.")
# print(f"{names[2].upper()} has scored {scores[2]} marks and lives in {address[2].capitalize()}.")
# print(f"{names[3].upper()} has scored {scores[3]} marks and lives in {address[3].capitalize()}.")
# print(f"{names[4].upper()} has scored {scores[4]} marks and lives in {address[4].capitalize()}.")

# gukesh, 99, Kerala
names.append("gukesh")
scores.append(99)
address.append("kerala")

# Add as first: Himesh, 39, Punjab
names.insert(0, "himesh")
scores.insert(0, 39)
address.insert(0, "punjab")

del names[2]
del scores[2]
del address[2]

for i in range(0,len(names)):
    print(f"{names[i].upper()} has scored {scores[i]} marks and lives in {address[i].capitalize()}.")

sum = 0
for i in range(0, len(scores)):
    sum = sum + scores[i]
print(sum/len(scores))


print(scores)
scores.sort(reverse=True)
print(scores)