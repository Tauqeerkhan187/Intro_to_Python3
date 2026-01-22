# Author:TK
# Date: 22-01-2026
# Desc: scatter 2000 points, show difference inside vs outside

import numpy as np
import matplotlib.pyplot as plt

total = 2000
x = np.random.uniform(-1, 1, total)
y = np.random.uniform(-1, 1, total)

inside = (x * x + y * y) <= 1.0

# plot figure
plt.figure()
plt.scatter(x[inside], y[inside], s=8, label="Inside circle")
plt.scatter(x[~inside], y[~inside], s=8, label="Outside circle")
plt.title("π points (2000 points)")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.legend()
plt.show()

pi_est = 4 * inside.mean()
print("pi_est (2000 points) =", pi_est)