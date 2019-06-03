train<-read.csv("F:\\case study\\train.csv",header=T,sep=",",na.strings=c(""))
test<-read.csv("F:\\case study\\test.csv",header=T,sep=",",na.strings=c(""))
# audit the data
str(train)
# missing values
sum(is.na(train))
sum(is.na(train$Item_Identifier))
sum(is.na(train$Item_Weight))
sum(is.na(train$Item_Fat_Content))
sum(is.na(train$Item_Visibility))
sum(is.na(train$Item_Type))
# another way to audit data
skewness(train$Item_Weight)
skewness(train$Item_MRP)
summary(train)
# impute the median with missing value
train$Item_Weight<-ifelse(is.na(train$Item_Weight),median(train$Item_Weight,na.rm=T),train$Item_Weight)
sum(is.na(train$Item_Weight))
#output values for outlet size
table(train$Outlet_Size)
train$Outlet_Size<-as.character(train$Outlet_Size)
train$Outlet_Size<-ifelse(is.na(train$Outlet_Size),"Medium",train$Outlet_Size)
table(train$Item_Fat_Content)
train$Item_Fat_Content<-as.character(train$Item_Fat_Content)
train$Item_Fat_Content<-ifelse(train$Item_Fat_Content=="LF","Low fat",train$Item_Fat_Content)                          
train$Item_Fat_Content<-ifelse(train$Item_Fat_Content=="low fat","Low Fat",train$Item_Fat_Content)
train$Item_Fat_Content<-ifelse(train$Item_Fat_Content=="reg","Regular",train$Item_Fat_Content)
train$Item_Fat_Content<-ifelse(train$Item_Fat_Content=="low Fat","Low Fat",train$Item_Fat_Content)
sum(is.na(train))
train$YOB<-2018-train$Outlet_Establishment_Year                          
# visual
boxplot(train$Item_Weight)
boxplot(train$Item_Visibility)
boxplot(train$Item_MRP)
cor(train$Item_Weight,train$Item_MRP)
cor(train$Item_Weight,train$Item_Visibility)
cor(train$Item_Weight,train$Item_Outlet_Sales)
cor(train$Item_MRP,train$Item_Outlet_Sales)
#multivariate analysis
names(train)
model<-lm(Item_Outlet_Sales~Item_Weight+Item_Fat_Content+Item_Visibility+Item_Type+Item_MRP+Outlet_Size+Outlet_Location_Type+Outlet_Type+YOB,data=train)
summary(model)
boxplot(model$residuals)
model$fitted.values
train$pred<-predict(model,train)
train$resid<-train$Item_Outlet_Sales-train$pred
train$sqrd<-train$resid*train$resid
mean_squared_error<-mean(train$sqrd)
root_mean_squared_error<-sqrt(mean_squared_error)
