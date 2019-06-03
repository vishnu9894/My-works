____________________________________________________#DATA IMPORT_____________________________________________
data<-read.csv("C:\\Users\\Vishnu\\Desktop\\case study\\A.FINAL PROJECT\\data.csv",header=T,sep=",",na.strings=c(""))

__________________________________________________#DATA PREP________________________________________________

str(data)
summary(data)
skewness(data$DistanceFromHome)
skewness(data$Age)
skewness(data$DailyRate)
data_int<-subset(data,select=-c(Attrition,BusinessTravel,Department,EducationField,Gender,JobRole,MaritalStatus,Over18,OverTime))
cor_mat<-cor(data_int)
write.csv(cor_mat,"cor_mat.csv")

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

names(data)

model<-glm(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,family = "binomial",data=data)
model
summary(model)
data$preds_glm<-predict(model,data,type="response")
table(data$Attrition,data$preds_glm)
data$outcome<-ifelse(data$preds_glm>=0.5,1,0)
table(data$Attrition,data$outcome)

model_svm<-svm(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,data=data)
summary(model_svm)
data$preds_svm<-predict(model_svm,data,type="response")
table(data$Attrition,data$preds_svm)

model_rf<-randomForest(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,data=data)
summary(model_rf)
data$preds_rf<-predict(model_rf,data,type = "response")
table(data$Attrition,data$preds_rf)