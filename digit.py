import numpy as np
import pandas as pd
import os

os.chdir("C:\\Users\\Vishnu\\Desktop\\case study\\DIGIT RECONIZER")

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

train_missing=train.isnull().sum()
test_missing=test.isnull().sum()

Y=train["label"]
X=train.iloc[:,1:]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

from sklearn.neural_network import MLPClassifier

MLP=MLPClassifier(hidden_layer_sizes=(50,50,50),solver="adam",verbose=True,max_iter=300)

MLP.fit(x_train,y_train)

Y_preds_train_MLP=MLP.predict(x_train)
Y_preds_test_MLP=MLP.predict(x_test)

from sklearn.metrics import confusion_matrix

co_MLR_train=confusion_matrix(y_train,Y_preds_train_MLP)
co_MLR_test=confusion_matrix(y_test,Y_preds_test_MLP)

preds_test=MLP.predict(test)
