import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Read Data and Handling the null values
wine_quality = pd.read_csv('winequality-red.csv')
data = wine_quality.select_dtypes(include=[np.number]).interpolate().dropna()

# Finding the top 3 most correlated features to the target label(quality).
numeric_features = data.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print(corr['quality'].sort_values(ascending=False)[1:4], '\n')
# Build a linear model
X = data.iloc[:, :-1].values
y = data.iloc[:, 11].values

# split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)
# train the model with the train sets
regressor = LinearRegression()
model = regressor.fit(X_train, y_train)

# Evaluate the performance and visualize results
print("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
print('RMSE is: \n', mean_squared_error(y_test, predictions))