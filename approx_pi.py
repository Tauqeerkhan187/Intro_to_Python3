# Author: TK
# Date: 22-01-2026
# Des: Generate random points in the square [-1, 1] × [-1, 1]

import numpy as np

total = 300000

x = np.random.uniform(-1, 1, total)
y = np.random.uniform(-1, 1, total)

inside = (x * x + y * y) <= 1.0
pi_est = 4 * inside.mean()

print("PI_est =", pi_est)
