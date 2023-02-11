#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# In[32]:


data=pd.read_csv('https://github.com/prasertcbs/basic-dataset/raw/master/study_hours.csv')


# In[33]:


data.T


# In[34]:


data.info()


# In[35]:


data.describe()


# In[36]:


data.isnull().sum()


# In[37]:


sns.scatterplot(data=data,x='Hours',y='Pass')


# In[38]:


sns.lmplot(x='Hours',y='Pass',data=data,logistic=False,ci=None,height=4,aspect=1.5,line_kws={'color':'red'})


# In[39]:


data.at[19,'Hours']=200


# In[40]:


sns.lmplot(x='Hours',y='Pass',data=data,logistic=False,ci=None,height=4,aspect=1.5,line_kws={'color':'red'})


# In[41]:


data


# In[42]:


data.at[19,'Hours']=5.5


# In[43]:


sns.lmplot(x='Hours',y='Pass',data=data,logistic=True,ci=None,height=4,aspect=1.5,line_kws={'color':'red'})


# In[ ]:




