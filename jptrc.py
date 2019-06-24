#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  pandas  as  pd


# In[3]:


import  matplotlib.pyplot  as  plt
import  findspark


# In[4]:


findspark.init('/spark')


# In[5]:


from  pyspark import SparkContext


# In[11]:


df=pd.read_csv('/root/Desktop/DATASETS-IPL/social.csv')


# In[12]:


#df.info()
df.head(5)


# In[16]:


df.plot(x='EstimatedSalary',y='Age',kind='scatter')


# In[58]:


#df['Gender'].unique()


# In[59]:


df_male = df['Gender']=='Male'
df[df_male]


# In[45]:



plt.bar(df['Gender'],df['Age'],color=['red','blue'])


# In[51]:


#plt.pie(df['Gender'].value_counts(), 'Age')


# In[57]:


#a=df['Gender']='Male'


# In[30]:


#help(plt.plot)


# In[ ]:



plt.show()
