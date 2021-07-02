import numpy as np
import matplotlib.pyplot as plt

def u(t):
    return 1 if t > 0 else 0

def f(t):
    return np.sin(3*np.pi*t)/(3*np.pi) * (u(t) - u(t-1)) + 2/(3 * np.pi) * np.sin(3*np.pi*t) * (u(t-1))

def g(t):
    return np.sin(np.pi * 2 * t)/(np.pi * 2) * (u(t) - u(t-1))

t_interval = np.arange(-1, 5, 0.001)

plt.plot(t_interval, [g(t) for t in t_interval])
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()