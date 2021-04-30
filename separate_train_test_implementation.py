import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from features import ffeatures
X_train = pd.read_csv("t4.csv")
cols = [col for col in X_train.columns if col not in ['', 'Name']]
X_train = X_train[cols]
y_train = np.array(X_train.pop('Label'))

X_test = pd.read_csv("test.csv")
cols = [col for col in X_test.columns if col not in ['', 'Name']]
X_test = X_test[cols]
y_test = np.array(X_test.pop('Label'))
# print(X_train)

classifier = RandomForestClassifier(n_estimators=50, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
# print(y_pred)
# print(type(X_train))
# print(type(X_test))
# print(type(y_train))
# print(type(y_test))
# print(type(y_pred))
# print(y_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,precision_score, recall_score, f1_score

CM = confusion_matrix(y_test,y_pred)
print(CM)
print(classification_report(y_test,y_pred))
TN = CM[0][0]
FN = CM[1][0]
TP = CM[1][1]
FP = CM[0][1]
print("accuracy score: ")
print(accuracy_score(y_test, y_pred))
# Fall out or false positive rate
FPR = FP/(FP+TN)
# False negative rate
FNR = FN/(TP+FN)
print("FPR: ")
print(FPR)
print("FNR: ")
print(FNR)
print("precision score: ")
print(precision_score(y_test,y_pred))
print("recall score: ")
print(recall_score(y_test,y_pred))
print("f1 score: ")
print(f1_score(y_test,y_pred))