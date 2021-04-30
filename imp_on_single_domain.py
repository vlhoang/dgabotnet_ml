import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from features import ffeatures
X_train = pd.read_csv("testAll.csv")
cols = [col for col in X_train.columns if col not in ['', 'Name']]
X_train = X_train[cols]
y_train = np.array(X_train.pop('Label'))

print("Training...")

classifier = RandomForestClassifier(n_estimators=20, random_state=0)
classifier.fit(X_train, y_train)

while(True):
    domain = input("Nhap domain muon kiem tra: ")
    if (domain == "0"):
        print ("Program exit!")
        break
    y_pred = classifier.predict(ffeatures(domain))
    if (y_pred[0] == 1): print ("Ten mien binh thuong!")
    elif (y_pred[0] == 0): print ("Ten mien DGA!")
