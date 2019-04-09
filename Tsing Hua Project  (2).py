#!/usr/bin/env python
# coding: utf-8

# In[284]:


import pandas as pd
import csv
data = pd.read_csv('/Users/annettechiu/Downloads/training.psv', sep='|')
data.columns = ['Student_id','Level','Course','Grade','Major']


# In[285]:


# Visualization 
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
from pandas.tools.plotting import scatter_matrix
from mpl_toolkits.mplot3d import Axes3D


# In[286]:


data.isnull().sum()


# In[287]:


data.head(10)


# In[288]:


data.describe(include=['O'])
# will display all numeric features data.describe()
#Show all kinds of characteristics


# In[289]:


print(set(data['Grade']))
#Audit Successful/Audit Unsuccessful (AUS/AUU)
#https://clas.uiowa.edu/students/handbook/grading-system
#IPIn Progress
#N_Nonpass
#P_Pass
#S_Satisfactory
#U_Unsatisfactory


# In[208]:


print(set(data['Level']))


# In[209]:


print(set(data['Major']))


# In[246]:


#breakdown by class
sns.countplot(x=data['Major'], data=df, palette="muted");
plt.show()


# In[258]:


#研究方向了解哪個學科給的分數最好
#哪個年級喜歡修哪些科目

data['Major'].value_counts()


# In[256]:


pd.crosstab(data['Major'],data['Grade']).head(20)


# In[269]:


data = data.groupby(data['Student_id'])


# In[270]:


data


# In[255]:


pd.crosstab(data['Major'],data['Level']).head(20)


# In[296]:


#Classification First, the perceptron and SVC will be trained on the continuous data.
data['TotalQ'] = data['Grade']
data['TotalQ'].loc[data.Grade == 'A'] = 0.0
data['TotalQ'].loc[data.Grade == 'B'] = 1.0
data['TotalQ'].loc[data.Grade == 'C'] = 2.0
X = np.array(continuous_subset).astype('float64')
y = np.array(df['TotalQ'])
X.shape


# In[ ]:




