import pandas as pd
import numpy
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB

csv_file = "data/golf.csv"
csv_file_reader = open(csv_file, "r")
data_set = pd.read_csv(csv_file_reader, sep=",")
csv_file_reader.close()

# data_set.head(10)

# Map string values for Outlook column to numbers
d = {'Sunny': 1, 'Overcast': 2, 'Rain': 3}
data_set.Outlook = [d[item] for item in data_set.Outlook.astype(str)]

# data_set.head(10)

# split the data into training and test data
train, test = model_selection.train_test_split(data_set, test_size=0.3, random_state=0)

# initialise Gaussian Naive Bayes
naive_b = GaussianNB()

# exclude Play Golf column
train_features = train.iloc[:, 0:4]
# Make Play Golf column as label
train_label = train.iloc[:, 4]

# repeat for test data
test_features = test.iloc[:, 0:4]
test_label = test.iloc[:, 4]

# Train the naive bayes model
naive_b.fit(train_features, train_label)

# build a dataframe to show the expected vs predicted values
test_data = pd.concat([test_features, test_label], axis=1)

test_data["prediction"] = naive_b.predict(test_features)

print(test_data, end='\n\n')

# use the score function and output the prediction accuracy
print("Naive Bayes Accuracy : ", naive_b.score(test_features, test_label))