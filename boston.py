# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:31:19 2019

@author: Vishnu
"""

import numpy as np
import pandas as pd
import os

#set working directory

os.chdir("C:\\Users\\Vishnu\\Desktop\\case study\\BOSTON")

#importing files

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

#audit the data

train["ID"].isna().value_counts()
train["crim"].isna().value_counts()
train.isna().sum()
summary=train.describe()
train["crim"].mean()

#converting to array

train_array=np.array(train)

#audit data

train.skew()

train["crim"].value_counts()

train["log_crim"]=np.log(train["crim"])

train["scale_crim"]=((train["crim"]-np.mean(train["crim"])/np.std(train["crim"])))

def standard_scalar(var):
    mean=np.mean(var)
    std=np.std(var)
    scale_var=(var-mean)/std
    return scale_var

train_scale=standard_scalar(train)

corr_matrix=np.corrcoef(train["crim"],train["tax"])
corr_matrix_pd=train.corr()

#dividing the data
Y=train["medv"]
X=train.iloc[:,1:14]

#modelling

from sklearn.linear_model import LinearRegression
LR=LinearRegression()

LR.fit(X,Y)

LR.coef_
LR.intercept_
preds_LR=LR.predict(X)

from sklearn.metrics import mean_squared_error
mse_lr=mean_squared_error(Y,preds_LR)

rmse_lr=np.sqrt(mse_lr)

#random forest

from sklearn.ensemble import RandomForestRegressor
RF=RandomForestRegressor()
RF=RandomForestRegressor(n_estimators=500)

RF.fit(X,Y)

preds_rf=RF.predict(X)

mse_rf=mean_squared_error(Y,preds_rf)

rmse_rf=np.sqrt(mse_rf)

#support vector

from sklearn import svm

svm_RF=svm.SVR()

svm_RF.fit(X,Y)

preds_svm=svm_RF.predict(X)

mse_svm=mean_squared_error(Y,preds_svm)

rmse_svm=np.sqrt(mse_svm)

#test

test_data=test.iloc[:,1:14]
test_data["preds medv"]=RF.predict(test_data)

test_data.to_csv("output.csv")
