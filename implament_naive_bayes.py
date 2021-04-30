import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#Create a Gaussian Classifier
gnb = GaussianNB()

#Choose train and test dataset
# X_train = pd.read_csv("t4.csv")
# cols = [col for col in X_train.columns if col not in ['', 'Name']]
# X_train = X_train[cols]
# y_train = np.array(X_train.pop('Label'))
#
# X_test = pd.read_csv("test.csv")
# cols = [col for col in X_test.columns if col not in ['', 'Name']]
# X_test = X_test[cols]
# y_test = np.array(X_test.pop('Label'))
train_dataset = pd.read_csv("testAll.csv")
cols = [col for col in train_dataset.columns if col not in ['', 'Name']]
train_dataset = train_dataset[cols]
labels = np.array(train_dataset.pop('Label'))
X_train, X_test, y_train, y_test = train_test_split(train_dataset, labels, test_size=0.2, random_state=0)

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)



print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
