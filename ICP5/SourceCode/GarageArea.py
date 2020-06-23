import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Read data
train = pd.read_csv('train.csv', sep=',', usecols=(62, 80))

# Display the scatter plot of GarageArea and SalePrice in Red
plt.scatter(train.GarageArea, train.SalePrice, color='red')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()

# Finding z-score, called standard score for train data
z = np.abs(stats.zscore(train))

# Filtering the standard data with z-score
modified = train[(z < 2).all(axis=1, keepdims=True)]
# outlier_drop = train[(train.GarageArea > 150) & (train.GarageArea < 1000) & (train.SalePrice < 500000)]

# Display the scatter plot of GarageArea and SalePrice after filtering the normal data with Green
plt.scatter(modified.GarageArea, modified.SalePrice, color='green')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()