import pandas as pd
train_df = pd.read_csv('train_preprocessed.csv')
# Finding the correlation (statistical summary of the relationship)
print("Correlation:", train_df['Survived'].corr(train_df['Sex']))

