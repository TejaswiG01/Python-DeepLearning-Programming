#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sns.set(style='white', color_codes=True)


# In[3]:


# Loading dataset
data = pd.read_csv('C:/Users/Tejaswi/Desktop/Python/ICP6/CC.csv')


# In[4]:


# Checking no of clusters => 7
print(data['TENURE'].value_counts())


# In[5]:


#Looking for null values
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)


# In[6]:


# Replacing MINIMUM_PAYMENTS and CREDIT_LIMIT by mean values as they have null values

data.loc[(data['MINIMUM_PAYMENTS'].isnull()==True), 'MINIMUM_PAYMENTS'] = data['MINIMUM_PAYMENTS'].mean()
data.loc[(data['CREDIT_LIMIT'].isnull()==True), 'CREDIT_LIMIT'] = data['CREDIT_LIMIT'].mean()


# In[7]:


# Deviding data into x train set
x = data.iloc[:,1:]
print(x.shape)


# In[8]:


# Displaying Null value count for each feature after replacing with mean values
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:16])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)


# In[9]:


#Elbow Method
#within-cluster sums of squares

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

#Display the graph
print(wcss)
plt.plot(range(1, 10), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


# In[10]:


#From the map, at k=3 is the best number for clusters
#Silhouette score

km = KMeans(n_clusters=3)
km.fit(x) # training our model with 3 clusters
y_cluster_kmeans = km.predict(x) # predicting the cluster for each data point in x

from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette score for 3 clusters',score)


# In[12]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

km = KMeans(n_clusters=3)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)

score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('Silhouette score for 3 clusters after scaling:',score)


# In[13]:


#Apply PCA
#scale the features
scaler = StandardScaler()
scaler.fit(x)
x_scaler = scaler.transform(x)
pca = PCA(3)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
final  = pd.concat ([df2,data[['TENURE']]], axis=1)
print(final)


# In[15]:


#Apply KMeans to PCA
km = KMeans(n_clusters=3)
km.fit(x_pca)

#predicting the luster for each data point after applying pca 
y_cluster_kmeans = km.predict(x_pca)

score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print("Silhoutte Score with PCA: " + str(score))


# In[16]:


plt.scatter(x_pca[:,0], x_pca[:,1], c = y_cluster_kmeans ,s=50)
plt.show()

