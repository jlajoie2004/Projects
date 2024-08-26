import numpy as np
import matplotlib.pyplot as plt

# Homework 4

# Problem 2

x = np.linspace(0,4,100)
y = 3*np.cos(5*x) - 2*x**3 + x**2 - 4*x + 16
dy_true = -15*np.sin(5*x) - 6*x**2 + 2*x -4
h = x[1] - x[0]

dy5 = np.zeros(len(x))
for i in range(len(x)):
    if i == 0:
        dy5[i] = (-25*y[i] + 48*y[i+1] - 36*y[i+2] + 16*y[i+3] - 3*y[i+4])/(12*h)
    elif i == 1:
        dy5[i] = (-3*y[i-1] - 10*y[i] + 18*y[i+1] - 6*y[i+2] + y[i+3])/(12*h)
    elif i == len(x)-2:
        dy5[i] = (-y[i-3] + 6*y[i-2] - 18*y[i-1] + 10*y[i] + 3*y[i+1])/(12*h)
    elif i == len(x)-1:
        dy5[i] = (3*y[i-4] - 16*y[i-3] + 36*y[i-2] - 48*y[i-1] + 25*y[i])/(12*h)
    else:
        dy5[i] = (y[i-2] - 8*y[i-1] + 8*y[i+1] - y[i+2])/(12*h)

error = abs(dy5 - dy_true)

plt.semilogy(x,error,'-',label='5pt Central Difference Error')
plt.legend()
plt.show()

# Problem 4:

x = np.array([0,5,10,15,20,25], dtype = float)
y = np.array([80,44.5,30,24.1,21.7,20.7], dtype = float)
h = 5

dy3 = np.zeros(len(x))
for i in range(len(x)):
    if i == 0:
        dy3[i] = (-3*y[i] + 4*y[i+1] - y[i+2])/(2*h)
    elif i == len(x) - 1:
        dy3[i] = (y[i-2] - 4*y[i-1] + 3*y[i])/(2*h)
    else:
        dy3[i] = (y[i+1] - y[i-1])/(2*h)

print(f'Problem 4:')
for i in range(len(x)):
    print(f'df at x={x[i]} is {dy3[i]:.2f}')