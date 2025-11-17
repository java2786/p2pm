import matplotlib.pyplot as plt 

mobiles = ['Lenovo', 'Nokia', 'iPhone', 'Spice', 'OnePlus']
market_share = [13, 10, 40, 15, 22]
colors = ['#7f5539', '#b56576', '#0077b6', '#a0a083', '#3c6e71']

plt.pie(market_share, labels=mobiles, colors=colors)
plt.title("Mobile phone share - Delhi")
plt.show()