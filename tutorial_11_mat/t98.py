import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)

# Customize the grid
plt.grid(color='blue', linestyle=':', linewidth=1)  # Custom grid appearance
plt.xticks(np.arange(0, 11, 1))  # X-axis ticks
plt.yticks(np.arange(-1, 1.1, 0.1))  # Y-axis ticks

# Add labels and title
plt.title("Sine Wave with Custom Unit Grid")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show plot
plt.show()
