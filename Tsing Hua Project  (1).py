#!/usr/bin/env python
# coding: utf-8

# In[202]:


import pandas as pd
import csv
data = pd.read_csv('/Users/annettechiu/Downloads/training.psv', sep='|')
data.columns = ['Student_id', 'Level', 'Course', 'Grade','Major']


# In[203]:


# Visualization 
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
from pandas.tools.plotting import scatter_matrix
from mpl_toolkits.mplot3d import Axes3D


# In[204]:


data.isnull().sum()


# In[205]:


data.head(10)


# In[206]:


data.describe(include=['O'])
# will display all numeric features data.describe()
#Show all kinds of characteristics


# In[207]:


print(set(data['Grade']))


# In[208]:


print(set(data['Level']))


# In[209]:


print(set(data['Major']))


# In[246]:


#breakdown by class
sns.countplot(x=data['Major'], data=df, palette="muted");
plt.show()


# In[253]:


pd.crosstab(data['Major'],data['Grade'])


# In[233]:


# 创建两个新的数据集
dataset_bin = pd.DataFrame() # To contain our dataframe with our **discretised** continuous variables 
dataset_con = pd.DataFrame() # To contain our dataframe with our continuous variables 


# In[ ]:


# Let's fix the Class Feature
dataset_raw.loc[dataset_raw['predclass'] == '>50K', 'predclass'] = 1
dataset_raw.loc[dataset_raw['predclass'] == '>50K.', 'predclass'] = 1
dataset_raw.loc[dataset_raw['predclass'] == '<=50K', 'predclass'] = 0
dataset_raw.loc[dataset_raw['predclass'] == '<=50K.', 'predclass'] = 0

dataset_bin['predclass'] = dataset_raw['predclass']
dataset_con['predclass'] = dataset_raw['predclass']

