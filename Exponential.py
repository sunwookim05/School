'''
Exponential Curve
@ author: Suyash Shivaji Phatak
Date = 25\04\2020
'''

# Defining Modules
import numpy as np
import matplotlib.pyplot as plt

# Taking input from user
range_for_exp = int(input('\nEnter a range of numbers for exponential function with base 2: '))

# Log with base 2

# Setting x
x = np.arange(1, range_for_exp)

# Setting y fo base 2
y1 = np.exp2(x)

# Plotting Points
plt.plot(x,y1, label='2**x')

# Seperating figure
plt.figure(1)

# Naming the x axis 
plt.xlabel('X')

# Naming the y axis 
plt.ylabel('Y')

# Giving a title to graph 
plt.title('Exponential Function')

# Showing legend
plt.legend()
# Function to show the plot 
plt.show() 