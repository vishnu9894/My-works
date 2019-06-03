import numpy as np
import pandas as pd
import os

os.chdir("C:\\Users\\Vishnu\\Desktop\\case study\\HR ANALYTICS")

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

train_missing=train.isnull().sum()
test_missing=test.isnull().sum()

train["education"].value_counts()
new_education=np.where(train["education"].isnull(),"Bachelor's",train["education"])
train["education"]=new_education
train["education"].isnull().sum()

train["previous_year_rating"].value_counts()
new_pyr=np.where(train["previous_year_rating"].isnull(),np.nanmedian(train["previous_year_rating"]),train["previous_year_rating"])
train["previous_year_rating"]=new_pyr
train["previous_year_rating"].isnull().sum()

from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()

train["department"]=LE.fit_transform(train["department"])
train["department"].value_counts()

train["region"]=LE.fit_transform(train["region"])
train["region"].value_counts()

train["education"]=LE.fit_transform(train["education"])
train["education"].value_counts()

train["gender"]=LE.fit_transform(train["gender"])
train["gender"].value_counts()

train["recruitment_channel"]=LE.fit_transform(train["recruitment_channel"])
train["recruitment_channel"].value_counts()

train["is_promoted"]=LE.fit_transform(train["is_promoted"])

y=train["is_promoted"]
x=train.iloc[:,1:13]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=123)


from sklearn.neural_network import MLPClassifier

MLP=MLPClassifier(hidden_layer_sizes=(20,20,20),solver="adam",verbose=True,max_iter=200)

MLP.fit(x_train,y_train)

preds_MLP=MLP.predict(x_train)

from sklearn.metrics import confusion_matrix

co_mlp=confusion_matrix(y_train,preds_MLP)

preds_train_test=MLP.predict(x_test)
co_mpl_traintest=confusion_matrix(y_test,preds_train_test)

from sklearn.ensemble import RandomForestClassifier
RF=RandomForestClassifier()
RF=RandomForestClassifier(n_estimators=500)

RF.fit(x_train,y_train)

preds_rf=RF.predict(x_train)

co_rf_reg=confusion_matrix(y_train,preds_rf)

preds_rft=RF.predict(x_test)
co_rftest=confusion_matrix(y_test,preds_rft)


