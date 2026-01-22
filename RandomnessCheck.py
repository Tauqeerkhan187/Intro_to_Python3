# Author: TK
# Date: 22-01-2026
# Desc: check randomness
# Uniform (0, 1), all values in 0,1 are equally likely - histogram tends to look flat
# Normal (0, 1), values cluster around 0, with fewer far away. shows as bell curve, it is unbounded can produce big positive and neg values.


import numpy as np
import matplotlib.pyplot as plt

uni = np.random.uniform(0, 1, 10000)
norm = np.random.normal(0, 1, 10000)

# Histogram uniform
plt.figure()
plt.hist(uni, bins = 50)
plt.title("Uniform (0, 1) samples (n = 10000)")
plt.xlabel("Val")
plt.ylabel("Count")
plt.show()


# Histogram normal
plt.figure()
plt.hist(norm, bins = 50)
plt.title("Normal (0, 1) samples (n = 10000)")
plt.xlabel("Value")
plt.ylabel("Count")
plt.show()