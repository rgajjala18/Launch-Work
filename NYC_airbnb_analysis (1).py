#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


get_ipython().run_line_magic('pylab', 'inline')


# In[11]:


df = pd.read_csv("/Users/ruthvikgajjala/Downloads/new-york-city-airbnb-open-data/AB_NYC_2019.csv")


# In[13]:


df.head(10)


# In[14]:


df.describe()


# In[16]:


to_drop=['id','host_id','latitude','longitude','name','host_name','neighbourhood','last_review']
df.drop(to_drop,inplace=True,axis=1)


# In[39]:


#Dropping columns that are not neccesary to the exploratory analysis


# In[17]:


df.head(10)


# In[19]:


df['neighbourhood_group'].value_counts()


# In[21]:


df.index.values


# In[ ]:


#checking that the dataframe has an index


# In[22]:


df.dtypes


# In[38]:


#checking that there are no type mistmatches in the data


# In[23]:


df.info()


# In[26]:


df.drop(['reviews_per_month'],inplace=True,axis=1)


# In[40]:


#dropping the reviews_per_month column due to large number of null values


# In[31]:


df = df[df.availability_365 != 0]


# In[ ]:


#removing rows from the dataframe that have an availability of 0 days per year


# In[32]:


df.head(10)


# In[33]:


df['room_type'].value_counts()


# In[37]:


df['calculated_host_listings_count'].value_counts()


# In[41]:


sns.boxplot(x=df['price'])


# In[42]:


df = df.sample(frac=0.05, replace=False, random_state=1)


# In[47]:


#taking a random sample of 5% with no replacement to glean a better understanding of the data


# In[48]:


sns.boxplot(x=df['price'])


# In[46]:


#using a seaborn boxplot to identify the outliers in price that may skew data predictions


# In[68]:


df.reset_index()


# In[71]:


df.info()


# In[72]:


from scipy import stats

z = np.abs(stats.zscore(df['price']))
print(z)


# In[73]:


#finding the zscores of each point in price


# In[74]:


bar=3
print(np.where(z>bar))


# In[87]:


#using zscores higher than 3 to identify major outliers


# In[88]:


df = df.drop([df.index[108] , df.index[116] , df.index[156] , df.index[238], df.index[240] , df.index[432] , 
                    df.index[516] , df.index[548] , df.index[606] , df.index[1003] , df.index[1027] , df.index[1074]
                    , df.index[1268] , df.index[1480] , df.index[1511] , df.index[1533] , df.index[1542]])


# In[89]:


#removing the major outliers from the data sample to see bigger trends


# In[ ]:


#preprocessing of data completed


# In[90]:


sns.pairplot(df)
sns.plt.show()


# In[ ]:


#creation of a correlogram to observe correlations between variables


# In[91]:


plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.show()


# In[ ]:


#correlation matrix showing low correlations between price and the other variables


# In[92]:


plt.hist(df['price'],bins=15)


# In[ ]:


#the maximum number of price listings are in the range $0-200


# In[93]:


f,ax=plt.subplots(figsize=(16,16))
sns.heatmap(df.corr(), annot=True, linewidths=5, fmt='.1f', ax=ax)
plt.show()


# In[94]:


#another correlation matrix showing the levels of correlation between the variables


# In[96]:


fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(df['availability_365'], df['price'])
ax.set_xlabel('Yearly availability')
ax.set_ylabel('Price per night (dollars)')
plt.show()


# In[97]:


#a scatterplot to further analyze if any correlation exists between the two variables


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




