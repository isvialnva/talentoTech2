import numpy as np

x = np.array([1, 2, 3, 4, 5])
h = np.array([-1, 5, 3, -2, 1])

y = np.convolve(x, h)
print(y)
