import numpy as np

# students - scores => 2D array
# Subjects (Math, Science, English)
# Scores of 4 students in 3 subjects

scores = np.array([
    [85,90,78], # Suresh
    [92,88,95], # Mahesh
    [76,82,80], # Ramesh
    [88,85,92], # Dinesh
])

students = [
    "Suresh",
    "Mahesh",
    "Ramesh",
    "Dinesh"
]


print("All scores:",scores)

# Suresh's score in Math (row, col)
print("Suresh's Math score:",scores[0,0])
# Suresh's score in English
print("Suresh's Enslish score:",scores[0,1])
# Suresh's score in all subjects
print("Suresh's all score:",scores[0,:])

# Ramesh's score in English 
print("Ramesh's English  score:",scores[2,2])

# All scores in Science
print("All Science scores:",scores[:,1])


# Student average
students_avg = np.mean(scores, axis=1)
# Subject average
subjects_avg = np.mean(scores, axis=0)

print("std avg:",students_avg)
print("sub avg:",subjects_avg)

max_score = np.argmax(students_avg)

print("Topper:",students[max_score]) # -> index
