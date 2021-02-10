import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# this is dydt - in a format the odeint likes
def model(y,t):
    dydt = +8*y + 5
    return dydt

# initial condition
y0 = 1

# declaring a vector of time values for odeint to solve
t = np.linspace(0,5)

# actually solving for y at each time point
y = odeint(model, y0, t)

# plotting the results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()