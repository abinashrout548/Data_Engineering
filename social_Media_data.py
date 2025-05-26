#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np



# In[2]:


social_data=pd.read_csv(r'C:\DataScience\DATA\Social Media Engagement Dataset.csv')


# In[3]:


social_data.head()


# In[4]:


social_data.info()


# In[6]:


social_data.describe()


# In[8]:


social_data.value_counts()


# In[7]:


social_data.isnull().sum()


# In[9]:


social_data['mentions'].fillna(social_data['mentions'].mode()[0], inplace=True)


# In[11]:


social_data.isnull().sum()


# In[12]:


social_data.duplicated().sum()


# In[13]:


social_data.drop_duplicates(inplace=True)


# In[15]:


social_data["user_id"] = social_data["user_id"].str.strip()
social_data.head()


# In[16]:


social_data['day_of_week'] = social_data['day_of_week'].str.upper()
social_data.head()


# In[ ]:


social_data["

