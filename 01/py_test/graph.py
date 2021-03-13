import pandas as pd
import matplotlib.pyplot as plt

# Load the data
# plt.title('Original Method')
# data = pd.read_csv('original_twenty.csv')
# square_scale = 1_000_000
# cube_scale = square_scale * 430

plt.title('Improved Method')
data = pd.read_csv('new_ten.csv')
square_scale = 6_000_000
cube_scale = 5_450_000_000

print(data)

# Graph the dat
x = list(data.n)
y = list(data.secs)
plt.plot(x, y, label='Real Data')

# Plot comparison lines
start, stop = min(x), max(y)
squared = [(i ** 2) / square_scale for i in x]
plt.plot(x, squared, label=f'Squared (scaled by: {square_scale:3,})')

cubed = [(i ** 3) / cube_scale for i in x]
plt.plot(x, cubed, label=f'Cubed (scaled by: {cube_scale:3,})')

# Show the graph
plt.xlabel('Size of Input')
plt.ylabel('Seconds of Runtime')
plt.legend()
plt.show()