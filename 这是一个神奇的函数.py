import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1 / (1 + np.e ** (-x))

def g(x, a, b):
    return (x / a) / ( ( 1 + ( ( x / a ) ** 2 ) ) * b) + 0.5

x = np.arange(-20, 20, 0.01)
y1 = f(x)

y2 = g(x, 5, 1.5)
y = y1 - y2 + 0.5

plt.plot(x, y1, 'r--')
plt.plot(x, y2, 'b--')
plt.plot(x, y)

plt.show()