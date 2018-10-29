#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from quantopian.research.experimental import history
from quantopian.research.experimental import continuous_future
import scipy
import numpy
numpy.arange
import matplotlib.pyplot as plt


# In[3]:


WTI = continuous_future( 'CL', roll = 'volume' ) #Crude Oil Futures

WTI = history(
    WTI, 
    fields='price', 
    frequency='daily', 
    start='2008-08-31', 
    end='2018-08-31'
)

Corn = continuous_future( 'CN' , roll = 'volume')  #Corn Futures

Corn = history(
    Corn, 
    fields='price', 
    frequency='daily', 
    start='2008-08-31', 
    end='2018-08-31'
)


# In[4]:


plt.plot(Corn)


# In[3]:


type(Corn.index)


# In[12]:


df


# In[5]:


x=scipy.signal.savgol_filter(Corn, 31, 2, 0, 1.0, -1, 'interp', 0.0)   
df = pd.DataFrame( x, index = Corn.index )  #Create dataframe
plt.plot(Corn, "y")  
plt.plot(df,"b")  


# In[6]:


OilDervative = pd.Series(np.gradient(WTI), WTI.index, name='Derivative')


# In[7]:


CornDervative = pd.Series(np.gradient(Corn), Corn.index, name='Derivative')


# In[9]:


dfOil = pd.concat([WTI.rename('Crude Oil Price'), OilDervative], axis=1)
dfCorn = pd.concat([Corn.rename('Corn Price'), CornDervative], axis=1)


# In[11]:


dfCorn

