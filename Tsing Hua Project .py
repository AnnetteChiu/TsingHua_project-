#!/usr/bin/env python
# coding: utf-8

# In[176]:


import pandas as pd
import csv
data = pd.read_csv('/Users/annettechiu/Downloads/training.psv', sep='|')
data.columns = ['Student_id', 'Level', 'Course', 'Grade','Major']


# In[177]:


# Visualization 
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
from pandas.tools.plotting import scatter_matrix
from mpl_toolkits.mplot3d import Axes3D


# In[178]:


data.head(10)


# In[179]:


data.describe(include=['O'])
# will display all numeric features data.describe()
#Show all kinds of characteristics


# In[ ]:




