# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:10:44 2019

@author: Vishnu
"""

import numpy as np
import pandas as pd
import os

os.chdir("C:\\Users\\Vishnu\\Desktop\\case study\\LOAN")

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

#missing values

train_missing=train.isnull().sum()
test_missing=test.isnull().sum()

#imputing

train["Gender"].value_counts()
new_gender=np.where(train["Gender"].isnull(),"Male",train["Gender"])
train["Gender"]=new_gender
train["Gender"].isnull().sum()

train["Married"].value_counts()
new_married=np.where(train["Married"].isnull(),"Yes",train["Married"])
train["Married"]=new_married
train["Married"].isnull().sum()

train["Dependents"].value_counts()
train["Dependents"]=train["Dependents"].replace("3+",3)
train["Dependents"]=train["Dependents"].replace("0",0)
new_dependents=np.where(train["Dependents"].isnull(),0,train["Dependents"])
train["Dependents"]=new_dependents
train["Dependents"]=pd.to_numeric(train["Dependents"])
train["Dependents"].dtypes
train["Dependents"].isnull().sum()

train["Self_Employed"].value_counts()
new_Self_Employed=np.where(train["Self_Employed"].isnull(),"No",train["Self_Employed"])
train["Self_Employed"]=new_Self_Employed
train["Self_Employed"].isnull().sum()

train["LoanAmount"]=np.where(train["LoanAmount"].isnull(),np.nanmedian(train["LoanAmount"]),train["LoanAmount"])
train["LoanAmount"].isnull().sum()

train["Loan_Amount_Term"].value_counts()
train["Loan_Amount_Term"]=np.where(train["Loan_Amount_Term"].isnull(),360,train["Loan_Amount_Term"])
train["Loan_Amount_Term"].isnull().sum()

train["Credit_History"].value_counts()
train["Credit_History"]=np.where(train["Credit_History"].isnull(),1.0,train["Credit_History"])
train["Credit_History"].isnull().sum()

check_missing=train.isnull().sum()

from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
train["Gender"]=LE.fit_transform(train["Gender"])
train["Gender"].value_counts()

train["Married"]=LE.fit_transform(train["Married"])
train["Married"].value_counts()

train["Self_Employed"]=LE.fit_transform(train["Self_Employed"])
train["Self_Employed"].value_counts()

train["Education"]=LE.fit_transform(train["Education"])
train["Education"].value_counts()

train["Property_Area"]=LE.fit_transform(train["Property_Area"])
train["Property_Area"].value_counts()

train["Loan_Status"]=LE.fit_transform(train["Loan_Status"])
train["Loan_Status"].value_counts()

Y=train["Loan_Status"]
X=train.iloc[:,1:11]

#MODELLING

from sklearn.linear_model import LogisticRegression
LR=LogisticRegression()

LR.fit(X,Y)

preds_lgr=LR.predict(X)

from sklearn.metrics import confusion_matrix

co_lr_reg=confusion_matrix(Y,preds_lgr)

#random forest

from sklearn.ensemble import RandomForestClassifier
RF=RandomForestClassifier()
RF=RandomForestClassifier(n_estimators=500)

RF.fit(X,Y)

preds_rf=RF.predict(X)

co_rf_reg=confusion_matrix(Y,preds_rf)

from sklearn.naive_bayes import GaussianNB
NB=GaussianNB()

NB.fit(X,Y)

preds_nb=NB.predict(X)

co_nb_rg=confusion_matrix(Y,preds_nb)


#test

test["Gender"].value_counts()
new_gender_test=np.where(test["Gender"].isnull(),"Male",test["Gender"])
test["Gender"]=new_gender_test
test["Gender"].isnull().sum()

test["Dependents"].value_counts()
test["Dependents"]=test["Dependents"].replace("3+",3)
test["Dependents"]=test["Dependents"].replace("0",0)
new_dependents_test=np.where(test["Dependents"].isnull(),0,test["Dependents"])
test["Dependents"]=new_dependents_test
test["Dependents"]=pd.to_numeric(test["Dependents"])
test["Dependents"].dtypes
test["Dependents"].isnull().sum()

test["Self_Employed"].value_counts()
new_Self_Employed_test=np.where(test["Self_Employed"].isnull(),"No",test["Self_Employed"])
test["Self_Employed"]=new_Self_Employed_test
test["Self_Employed"].isnull().sum()

test["LoanAmount"]=np.where(test["LoanAmount"].isnull(),np.nanmedian(test["LoanAmount"]),test["LoanAmount"])
test["LoanAmount"].isnull().sum()

test["Loan_Amount_Term"].value_counts()
test["Loan_Amount_Term"]=np.where(test["Loan_Amount_Term"].isnull(),360,test["Loan_Amount_Term"])
test["Loan_Amount_Term"].isnull().sum()

test["Credit_History"].value_counts()
test["Credit_History"]=np.where(test["Credit_History"].isnull(),1.0,test["Credit_History"])
test["Credit_History"].isnull().sum()

check_missing=test.isnull().sum()

test["Gender"]=LE.fit_transform(test["Gender"])
test["Gender"].value_counts()

test["Married"]=LE.fit_transform(test["Married"])
test["Married"].value_counts()

test["Self_Employed"]=LE.fit_transform(test["Self_Employed"])
test["Self_Employed"].value_counts()

test["Education"]=LE.fit_transform(test["Education"])
test["Education"].value_counts()

test["Property_Area"]=LE.fit_transform(test["Property_Area"])
test["Property_Area"].value_counts()

test_data=test.iloc[:,1:11]
test_data["Loan_Status"]=RF.predict(test_data)

test_data.to_csv("output.csv")