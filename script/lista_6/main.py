import numpy as np
import matplotlib.pyplot as plt


def D(w0, n):
    return np.sin(n*w0/40)/(n*w0/40)


def H(w):
    return 100/(100 + 1j *w)

S = 0
C = np.zeros(41)
w = 20*np.pi
n_interval = range(-20, 21)

for i in n_interval:
    C[i+20] = D(w, i)

plt.plot(n_interval , C, "o")
plt.plot(n_interval , C, "-")