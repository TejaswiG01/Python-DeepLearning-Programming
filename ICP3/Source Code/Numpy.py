import numpy as np
from collections import Counter

# creating random vector of size 20
array = []
array = np.random.uniform(low=1.0, high=20.0, size=20)
print("Random float array:", array)

# reshaping the matrix into 4x5
shape = array.reshape(4, 5)
print("Reshaped 4x5 array:", shape)

# replacing the the max value of each row with zero
replace = np.where(shape == np.max(shape, axis=1, keepdims=True), 0, shape)
print('Replacing Max No. by 0:', replace)
