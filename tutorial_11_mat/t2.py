import matplotlib.pyplot as plt

# sales data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [150, 120, 125, 165, 147]

# Create chart - line
plt.plot(months, sales, 
        color='green',
        linewidth=4,
        marker="o",
        markersize=15,
        linestyle="--"
    )
plt.title("Monthly Sale")
plt.xlabel("Month")
plt.ylabel("Sale (in K)")
plt.grid(True)

plt.show()