df<-USArrests
library(e1071)
skewness(df$Murder)
skewness(df$Assault)
skewness(df$UrbanPop)
skewness(df$Rape)
df_scaled<-scale(df)

df_scaled_df<-as.data.frame(df_scaled)
skewness(df_scaled_df$Murder)
skewness(df_scaled_df$Assault)
skewness(df_scaled_df$UrbanPop)
skewness(df_scaled_df$Rape)

distance<- get_dist(df_scaled)
distance
fviz_dist(distance)

k2<-kmeans(df_scaled,centers=5,nstart = 25)
df$clusters<-k2$cluster
fviz_cluster(k2,data=df)

wss_values<-function(k)(kmeans(df,k,nstar=10)$tot.withinss)
k.values<-1:15
wss_values<-map_db1(k.values,wss)
