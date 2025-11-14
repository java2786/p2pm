import matplotlib.pyplot as plt
import numpy as np

# Create plot
plt.figure(figsize=(8, 6))

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


# Customize the grid
plt.grid(color='blue', linestyle=':', linewidth=1)  # Custom grid appearance


# Annotate each data point with its value
for i, value in enumerate(sales):
    plt.text(months[i], value, f'{value}K', fontsize=28)  # Show value in thousands

plt.show()


