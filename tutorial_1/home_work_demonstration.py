"""
80 above -> Grade A 
60 above -> Grade B 
40 above -> Grade C 
else -> fail

Home work
    students -> 5 subjects marks -> sum, avg, max, min, Grade
"""

marks1 = 55
marks2 = 67
marks3 = 89
marks4 = 81
marks5 = 72

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
# print("Total score is: ",total_marks)
print(f"Total score is: {total_marks}")

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
# print("Avg score is: ",total_marks/5)
avg_marks = total_marks/len((marks1, marks2, marks3, marks4, marks5))
print("Avg score is: ",avg_marks)

print("Max score is: ",max(marks1, marks2, marks3, marks4, marks5))

print("Min score is: ",min(marks1, marks2, marks3, marks4, marks5))



if(avg_marks>80):
	print("Grade A")
elif(avg_marks>60):
	print("Grade B")
elif(avg_marks>40):
	print("Grade C")
else:
	print("Fail")
