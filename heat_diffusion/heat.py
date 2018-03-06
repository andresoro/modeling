from matplotlib import pyplot as plt
import numpy as np

def u(x, t):
    results = []
    first_term = 1/(np.sqrt(4*np.pi*t))
    for xval in x:
        second_term = np.exp((-xval**2)/(4*t))
        results.append(first_term*second_term)
    return results
z = np.linspace(-2*np.pi, 2*np.pi, 100)
t = np.arange(0, 5)
for tval in t:
    plt.plot(z, u(z, tval))
plt.show()