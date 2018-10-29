#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Inputs
import numpy as np
import pandas as pd
from quantopian.research.experimental import history
from quantopian.research.experimental import continuous_future
import scipy
import numpy
import matplotlib.pyplot as plt


# In[4]:


#CN - Corn
#CL - Crude Oil
#ES - S P 500
#ER - Russel 2000
#ET - Ethanol
#FC feeder cattle
#GC - Gold
#OA - Oats
#LB Lumber
#LH - Hogs
#LC live cattle
#NG - Natural Gas 
#PL - platnum
#SY - Soybean
#SV - Silver
#SP - S&P 500 future
#HG - Copper
#WC - Wheat 
#ED - Euro Dollar

#Creating Arrays
FutureTicker=["CN","CL","ED","ES","ER","ET","FC","GC","OA","PA","NG","LB","LH","LC","SY","SV","HG","WC"]
Prices=[]
Correlation=[]
Order = []


# In[ ]:


#Pulls data for all futures listed above and curve fits them via Math filter we created

for x in FutureTicker:
    
    y= continuous_future( x , roll = 'volume')
    
    y = history( y,  fields='price', frequency='daily', start='2018-10-21', end='2018-10-21' )
    
    x=pd.Series(scipy.signal.savgol_filter(y,31, 2, 0, 1.0, -1, 'interp', 0.0))

    Prices.append(x)


# In[40]:


#Finds every possible Correlation between futures

for i in range(0,len(FutureTicker)-1):
    for x in range(i+1, len(FutureTicker)):
        Correlation.append((Prices[i].corr(Prices[x])))


# In[42]:


#FInds max and uses correlation to find which futues made the highest correlation

max(Correlation)
for i in range(0,len(FutureTicker)-1):
    for x in range(i+1, len(FutureTicker)):
        if max(Correlation)==((Prices[i].corr(Prices[x]))):
            print "Highest is",FutureTicker[i], "and", FutureTicker[x], "with a correlation of", max(Correlation)


# In[ ]:





# In[43]:


#Output-
#Highest is CN and SY with a correlation of 0.982823931196
#Check to make sure is correct
Prices[0].corr(Prices[2])

#Output-
#0.98282393119642641


# In[47]:


#*One note with the math filter will not work for short term like one month as window length is 31 #and that is greater than a month
Order=numpy.sort(Correlation,-1,'mergesort')
for i in Order:
    for j in range(0,len(FutureTicker)-1):
        for x in range(j+1, len(FutureTicker)):
            if i==((Prices[j].corr(Prices[x]))):
                print "Correlation btwn",FutureTicker[j], "and", FutureTicker[x], "is a correlation of", i


# In[36]:


Order


# In[18]:



##STRONG CORRELATION##
#Ethonal == lumbebr
#Corn == Lomber  
#Corn == Soymeal 
#Gold == Copper

##WEAK CORRELATIONS## 


##Create Rolling correlations looking at cases when dates had a weak correlation. If it every broke that correlation.
# What is a weak correlation tho? 



# In[35]:


Prices[0].corr(Prices[1])


# In[ ]:




