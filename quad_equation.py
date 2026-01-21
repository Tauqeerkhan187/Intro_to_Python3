import matplotlib.pyplot as plt
import numpy as np

# function
def f(x):
    return x**2 - 4*x + 3

# Interval
x = np.linspace(-2, 6, 400)
y = f(x)

# plotting
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of the function f(x) = x^2 - 4x + 3")
plt.grid(True)
plt.show()


