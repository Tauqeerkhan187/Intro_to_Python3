import numpy as np

# Creates a simple 2D array
a = np.arange(30).reshape(5, 6)
print("a: \n", a)

# Take row 1, 3 and col 2, 4 
b = a[1:4, 2:5]
print("\nb = a[1:4, 2:5]:\n", b)

# Select all rows and columns 1 to 4
c = a[:, 1:5]
print("\nc = a[:, 1:5]:\n", c)


# single column as 1D
column2 = a[:, 2]
print("\ncolumn2 = a[:, 2]:\n", column2, column2.shape)

# single col as 2D (keep col dimension)
col2_2D = a[:, 2:3]
print("\ncol2_2D = a[:, 2:3]:\n", col2_2D, col2_2D.shape)

# step slicing
every_sec_col = a[:, ::2]
print("\nevery_sec_col = a[:, ::2]:\n", every_sec_col)

# view behavior
print("\nAfter b[0, 0] = 999: ")
print("a:\n", a)
print("b:\n", b)