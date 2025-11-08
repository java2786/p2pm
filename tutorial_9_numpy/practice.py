# How can we analyze ticket prices for train bookings based on distances and class multipliers, 
# and what insights can we derive from the generated booking data?

# 1001 - 1020
# 50 500, 20
# 2.5
# sl - 1, 3ac - 1.5, 2ac - 2.5, 1ac - 3

# Task: Analyze ticket prices for 20 bookings
# Data: [BookingId, Distance, BasePrice, ClassMultipliers]

import numpy as np

# reproducable result
np.random.seed(42)

booking_ids = np.arange(1001, 1021)
distances = np.random.randint(50, 500, 20)
base_price_per_km = 1.50

# sl - 1, 3ac - 1.5, 2ac - 2.5, 1ac - 3
class_multipliers = np.random.choice([1.0, 1.5, 2.5, 4.0], 20)

# Calculate ticket prices
ticket_prices = distances * base_price_per_km * class_multipliers

# Add service tax
final_prices = ticket_prices * 1.05

# Create complete booking data
booking_data = np.column_stack((booking_ids, distances, class_multipliers, ticket_prices, final_prices))

print("********* Booking Analysis Report *********")
print(f"Total Bookings: {len(booking_ids)}")
print(f"Average distance: {np.mean(distances):.2f} KM")
print(f"Total distance: {np.sum(distances):.2f} KM")
print(f"Average ticket price: Rs. {np.mean(final_prices):.2f}")
print(f"Max Fare: Rs. {np.max(final_prices):.2f}")
print(f"Min Fare: Rs. {np.min(final_prices):.2f}")
print(f"Total Revenue: Rs. {np.sum(final_prices):.2f}")

# conditional query - long journey/distance
long_distances = distances > 300
print(f"Revenue of Long distance bookings: Rs. {np.sum(final_prices[long_distances]):.2f}")
