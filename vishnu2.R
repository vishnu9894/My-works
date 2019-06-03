train<-read.csv("C:\\Users\\Vishnu\\Desktop\\case study\\BOSTON\\train.csv",header=T,sep=",",na.strings=c(""))
test<-read.csv("C:\\Users\\Vishnu\\Desktop\\case study\\BOSTON\\\\test.csv",header=T,sep=",",na.strings=c(""))
summary(train)
str(train)
skewness(train$crim)
skewness(train$zn)
skewness(train$indus)
skewness(train$chas)
skewness(train$nox)
skewness(train$rm)
skewness(train$age)
skewness(train$dis)
skewness(train$rad)
skewness(train$tax)
skewness(train$ptratio)
skewness(train$black)
skewness(train$lstat)
boxplot(train$crim)
boxplot(train$zn)
boxplot(train$indus)
boxplot(train$chas)
boxplot(train$nox)
boxplot(train$rm)
boxplot(train$age)
boxplot(train$dis)
boxplot(train$rad)
boxplot(train$tax)
boxplot(train$ptratio)
boxplot(train$black)
boxplot(train$lstat)
correlation.matrix<-cor(train)
write.csv(correlation.matrix,"cormat.csv")
#__________________________linear reg________________

names(train)
train$chas<-as.factor(train$chas)
linear_model<-lm(medv~crim+zn+indus+chas+nox+rm+age+dis+rad+tax+ptratio+black+lstat,data =train)
linear_model
summary(linear_model)
train$pred_lm<-predict(linear_model,train)
train$res<-(train$medv-train$pred_lm)
train$ressquare<-(train$res*train$res)
mean_sqr_error<-mean(train$ressquare)
root_mean_error<-sqrt(mean_sqr_error)
print(root_mean_error)
#______________Decision tree____________

png(file="decision_tree1.png")
model_tree<-ctree(medv~crim+zn+indus+chas+nox+rm+age+dis+rad+tax+ptratio+black+lstat,data =train)
#plot tree
plot(model_tree)
dev.off()
summary(model_tree)
model_tree
train$preds_tree<-predict(model_tree,train)
mse_tree<-sqrt(mean((train$medv-train$preds_tree)^2))
print(mse_tree)

#___________Random forest_________

model_rf<-randomForest(medv~crim+zn+indus+chas+nox+rm+age+dis+rad+tax+ptratio+black+lstat,data =train)
train$preds_rf<-predict(model_rf,train)
train_mserf<-sqrt(mean((train$medv-train$preds_rf)^2))
print(train_mserf)

#______________svm__________
library(e1071)
model_svm<-svm(medv~crim+zn+indus+chas+nox+rm+age+dis+rad+tax+ptratio+black+lstat,data =train)
model_svm
train$preds_svm<-predict(model_svm,train)
mse_svm<-sqrt(mean((train$medv-train$preds_svm)^2))
print(mse_svm)


#_____________test data_________

str(test)
summary(test)
test$chas<-as.factor(test$chas)
test$medv<-predict(model_rf,test)
write.csv(test,"medvfinal.csv")
