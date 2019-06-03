#DATA IMPORT

data<-read.csv("C:\\Users\\Vishnu\\Desktop\\case study\\A.FINAL PROJECT\\data.csv",header=T,sep=",",na.strings=c(""))

#DATA PREPARATION

str(data)
summary(data)
skewness(data$DistanceFromHome)
skewness(data$Age)
skewness(data$DailyRate)
data_int<-subset(data,select=-c(Attrition,BusinessTravel,Department,EducationField,Gender,JobRole,MaritalStatus,Over18,OverTime))
cor_mat<-cor(data_int)
write.csv(cor_mat,"cor_mat.csv")

#DATA TYPE CONVERSIONS

data$Education<-as.factor(data$Education)
data$EnvironmentSatisfaction<-as.factor(data$EnvironmentSatisfaction)
data$JobInvolvement<-as.factor(data$JobInvolvement)
data$JobLevel<-as.factor(data$JobLevel)
data$JobSatisfaction<-as.factor(data$JobSatisfaction)
data$PerformanceRating<-as.factor(data$PerformanceRating)
data$RelationshipSatisfaction<-as.factor(data$RelationshipSatisfaction)
data$StockOptionLevel<-as.factor(data$StockOptionLevel)
data$WorkLifeBalance<-as.factor(data$WorkLifeBalance)

str(data)

#MODEL BUILDING
#LOGISTIC REG

names(data)

model<-glm(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,family = "binomial",data=data)
model
summary(model)
data$preds_glm<-predict(model,data,type="response")
table(data$Attrition,data$preds_glm)
data$outcome<-ifelse(data$preds_glm>=0.5,1,0)
table(data$Attrition,data$outcome)

#SUPPORT VECTOR MACHINES

model_svm<-svm(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,data=data)
summary(model_svm)
data$preds_svm<-predict(model_svm,data,type="response")
table(data$Attrition,data$preds_svm)

#RANDOM FOREST

model_rf<-randomForest(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,data=data)
summary(model_rf)
data$preds_rf<-predict(model_rf,data,type = "response")
table(data$Attrition,data$preds_rf)

#DATA SPILT(TEST AND TRAIN SPLIT)

set.seed(3033)
intrain<-createDataPartition(y=data$Attrition,p=0.7,list=FALSE)
training<-data[intrain,]
testing<-data[-intrain,]

#AFTER SPLIT TRAIN MODELLING USING RANDOM FOREST

model_rf1<-randomForest(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,data=data)
summary(model_rf1)
training$preds_rf1<-predict(model_rf1,training,type = "response")
table(training$Attrition,training$preds_rf1)

#TEST DATA MODELLING USING RANDOM FOREST

testing1<-subset(testing,select=-c(Attrition,preds_glm,outcome,preds_rf,preds_svm))
testing1$preds<-predict(model_rf1,testing1,type="response")
table(testing$Attrition,testing1$preds)
