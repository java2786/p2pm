import matplotlib.pyplot as plt 

# Sales data -> sales by city

cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Pune']
revenue = [125, 110, 120, 85, 92]
# colors = ['#7f5539', '#b56576', '#0077b6', '#a0a083', '#3c6e71']
colors = ['#7f5539', '#0077b6']

plt.bar(cities, revenue, color=colors)
# plt.barh(cities, revenue, color='#7f5539')
plt.title("Cities By Revenue")
plt.xlabel("City")
plt.ylabel("Revenu (in Lakhs)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()