'''
Logarithm Curve
@ author: Suyash Shivaji Phatak
Date = 25\04\2020
'''

# Defining Modules
import numpy as np
import matplotlib.pyplot as plt

# Taking input from user
range_for_log = int(input('\nEnter a range of numbers for logarithm with base 2,10 & e: '))

# Log with base 2

# Setting x
x = np.arange(1, range_for_log)

# Setting y fo base 2
y1 = np.log2(x)

# Setting y for base 10
y2 = np.log10(x)

# Setting y for base e
y3 = np.log(x)

# Plotting Points
plt.plot(x,y1, label='Log With Base 2')
plt.plot(x,y2, label='Log With Base 10')
plt.plot(x,y3, label='Log With Base e')
# Seperating figure
plt.figure(1)

# Naming the x axis 
plt.xlabel('X')

# Naming the y axis 
plt.ylabel('Y')

# Giving a title to graph 
plt.title('Logarithm Function')

# Showing legend
plt.legend()
# Function to show the plot 
plt.show() 