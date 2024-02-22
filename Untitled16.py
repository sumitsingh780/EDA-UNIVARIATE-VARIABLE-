#!/usr/bin/env python
# coding: utf-8

# # EDA (Univariate analysis)

# In[18]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


# In[2]:


df=pd.read_csv('train.csv')


# In[3]:


df


# In[4]:


df.head()


# # categorical data 

# # A : countplot

# In[29]:


sns.countplot(x="Pclass",data=df)


# In[30]:


sns.countplot(x="Survived",data=df)


# In[31]:


sns.countplot(x="Sex",data=df)


# In[50]:


df["Sex"].value_counts().plot(kind= "pie")


# # numerical data 

# # histplot

# In[45]:


plt.hist(df['Age'])
plt.show()


# # distplot

# In[49]:


sns.distplot(df["Age",])


# # boxplot

# In[55]:


sns.boxplot(df['Age'])


# In[ ]:




