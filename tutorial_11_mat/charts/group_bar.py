import matplotlib.pyplot as plt 
import numpy as np
# Cricket

overs = ['1st', '2nd', '3rd', '4th', '5th']
teamA = [12, 4, 5, 2, 11]
teamB = [9, 7, 6, 3, 1]

count = np.arange(len(overs))
width = .35

plt.bar(count-width, teamA, width, label="Team A", color='#7f5539')
plt.bar(count, teamB, width, label="Team B", color='#0077b6')
# plt.bar(count+width=)


plt.title("Match Overs")
plt.xlabel("overs")
plt.ylabel("Runs")

plt.xticks(count, overs)
plt.tight_layout()

plt.show()