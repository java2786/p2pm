import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.randn(1000)

# Create histogram
plt.hist(data, bins=4, alpha=1, color='blue', edgecolor='black')

# Customize chart
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.show()
