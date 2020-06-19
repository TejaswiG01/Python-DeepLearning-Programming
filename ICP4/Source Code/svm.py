import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
# Load the Dataset
data_frame = pd.read_csv('glass.csv')
X = data_frame.drop("Type", axis=1)
Y = data_frame["Type"]

# Split the data into Training sets and Testing sets
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2)

# calling the naive bayes classifier model and training it with the train sets
svc = SVC()
svc.fit(X_Train, Y_Train)
# Predict the target on the Test dataset
Predict_Test = svc.predict(X_Test)

# Evaluating Model: Accuracy Score on Test dataset
accuracy_test = accuracy_score(Y_Test, Predict_Test)
print('Accuracy_score on Test dataset: ', accuracy_test)

# classification report
report1 = metrics.classification_report(Y_Test, Predict_Test)
print(report1)

