import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,precision_score, recall_score,f1_score
from sklearn.tree import DecisionTreeClassifier

# train_dataset = pd.read_csv("t2.csv")
# cols = [col for col in train_dataset.columns if col not in ['', 'Name']]
# train_dataset = train_dataset[cols]
# labels = np.array(train_dataset.pop('Label'))
# X_train, X_test, y_train, y_test = train_test_split(train_dataset, labels, test_size=0.3, random_state=0)

X_train = pd.read_csv("t4.csv")
cols = [col for col in X_train.columns if col not in ['', 'Name']]
X_train = X_train[cols]
y_train = np.array(X_train.pop('Label'))

X_test = pd.read_csv("test.csv")
cols = [col for col in X_test.columns if col not in ['', 'Name']]
X_test = X_test[cols]
y_test = np.array(X_test.pop('Label'))

clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=15, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=15, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)

y_pred1 = clf_gini.predict(X_test)
y_pred2 = clf_entropy.predict(X_test)

print("Gini")
CM1 = confusion_matrix(y_test,y_pred1)
print(CM1)
print(classification_report(y_test,y_pred1))
TN1 = CM1[0][0]
FN1 = CM1[1][0]
TP1 = CM1[1][1]
FP1 = CM1[0][1]
print("accuracy score: ")
print(accuracy_score(y_test, y_pred1))
# Fall out or false positive rate
FPR1 = FP1/(FP1+TN1)
# False negative rate
FNR1 = FN1/(TP1+FN1)
print("FPR: ")
print(FPR1)
print("FNR: ")
print(FNR1)
print("precision score: ")
print(precision_score(y_test,y_pred1))
print("recall score: ")
print(recall_score(y_test,y_pred1))
print("f1 score: ")
print(f1_score(y_test,y_pred1))
print("Entropy")
CM2 = confusion_matrix(y_test,y_pred2)
print(CM2)
print(classification_report(y_test,y_pred2))
TN2 = CM2[0][0]
FN2 = CM2[1][0]
TP2 = CM2[1][1]
FP2 = CM2[0][1]
print("accuracy score: ")
print(accuracy_score(y_test, y_pred2))
# Fall out or false positive rate
FPR2 = FP2/(FP2+TN2)
# False negative rate
FNR2 = FN2/(TP2+FN2)
print("FPR: ")
print(FPR2)
print("FNR: ")
print(FNR2)
print("precision score: ")
print(precision_score(y_test,y_pred2))
print("recall score: ")
print(recall_score(y_test,y_pred2))
print("f1 score: ")
print(f1_score(y_test,y_pred2))