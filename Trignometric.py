'''
Trignometric Function Curve
@author : Suyash Shivaji Phatak
Date = 25\04\2020
'''

# Defining Modules
import numpy as np
import matplotlib.pyplot as plt

# Taking input from user
angle = float(input('\nEnter angle(in radians) to show the curve: '))

'''
1. Sine & Cosine curve
'''

# Sine Curve

# Setting x 
x = np.arange(0, angle*(np.pi), 0.1)

# Setting y for sin
y1 = np.sin(x)

# setting y for cos
y2 = np.cos(x)

# Seperating Graphs
plt.figure(1)

# Plotting both points 
plt.plot(x, y1,label = 'Sine curve')
plt.plot(x, y2,label = 'Cosine curve')

# Naming the x axis 
plt.xlabel('θ')

# Naming the y axis 
plt.ylabel('Y')

# Giving a title to graph 
plt.title('Sine curve VS Cosine curve')

'''
2. Tangent curve
'''

# Setting x 
x3 = np.arange(0, angle*(np.pi), 0.1)

# Setting y 
y3 = np.tan(x3)

# Seperating Graphs
plt.figure(2)

# Plotting first points 
plt.plot(x3, y3,label = 'Tangent curve')

# Naming the x axis 
plt.xlabel('θ')

# Naming the y axis 
plt.ylabel('Y')

# Giving a title to graph 
plt.title('Tangent Curve')

# Showing legend
plt.legend()

# Function to show the plot 
plt.show() 