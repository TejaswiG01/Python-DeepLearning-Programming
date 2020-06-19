import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
# Load the Dataset
data_frame = pd.read_csv('glass.csv')
X = data_frame.drop("Type", axis=1)
Y = data_frame["Type"]

# Split the data into Training sets and Testing sets
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.3)

# Calling the naive bayes classifier model and training it with the train sets
nb = GaussianNB()
nb.fit(X_Train, Y_Train)
# Predict the target on the Test dataset
Predict_Test = nb.predict(X_Test)

# Evaluating Model: Accuracy Score on Test dataset
accuracy_test = accuracy_score(Y_Test, Predict_Test)
print('Accuracy_score on Test dataset: ', accuracy_test)

# classification report
report1 = classification_report(Y_Test, Predict_Test)
print(report1)

