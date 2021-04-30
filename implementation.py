import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
train_dataset = pd.read_csv("testAll.csv")
cols = [col for col in train_dataset.columns if col not in ['', 'Name']]
train_dataset = train_dataset[cols]
# train_dataset = train_dataset.drop(['Name'], axis=1)
#train_dataset = train_dataset[train_dataset.columns.difference(['', 'Name'])]
labels = np.array(train_dataset.pop('Label'))

X_train, X_test, y_train, y_test = train_test_split(train_dataset, labels, test_size=0.3, random_state=0)
# print(X_train)

# dfObj = pd.DataFrame(
#     columns=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14',
#              'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22'])
# dfObj.loc[0] = [24,18396,755.375,735.84,30.215,0.96,0.96,2.3438424151280612,23,697283,28361.82608695652,
#                 27891.32,1134.4730434782607,0.92,0.92,2.321181556165137,5,0.2,1,2.9132,0,0]
classifier = RandomForestClassifier(n_estimators=20, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
# print(y_pred[0])
# print(type(X_train))
# print(type(X_test))
# print(type(y_train))
# print(type(y_test))
# print(type(y_pred))
# print(y_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score, roc_curve,mean_absolute_error, mean_squared_error,precision_score

print("confusion_matrix: ")
print(confusion_matrix(y_test,y_pred))
print("classification report: ")
print(classification_report(y_test,y_pred))
print("accuracy score: ")
print(accuracy_score(y_test, y_pred))
print("roc_auc score: ")
print(roc_auc_score(y_test, y_pred))
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
print("fpr and tpr: ")
print (fpr)
print (tpr)
print ("mean absolute error: ")
print(mean_absolute_error(y_test, y_pred))
print ("mean squared error: ")
print(mean_squared_error(y_test, y_pred))
print("precision score: ")
print(precision_score(y_test,y_pred))