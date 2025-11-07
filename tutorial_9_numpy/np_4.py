import numpy as np

# Array operations
item_prices = [500,1200,800, 1500,950]

np_price = np.array(item_prices)

print(np_price)
# apply 10% discount
dicounted_price = np_price * .9
print(dicounted_price)

# add flat 40 rupees as delivery charge
final_prices = dicounted_price + 40
print(final_prices)

# add gst - 18%
final_prices = final_prices*1.18
print(final_prices)

