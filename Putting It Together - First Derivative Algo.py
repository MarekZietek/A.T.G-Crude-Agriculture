#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from quantopian.research.experimental import history
from quantopian.research.experimental import continuous_future
import scipy
import numpy
numpy.arange
import matplotlib.pyplot as plt


# In[11]:


WTI = continuous_future( 'CL', roll = 'volume' ) #Crude Oil Futures

WTI = history(
    WTI, 
    fields='price', 
    frequency='daily', 
    start='2014-04-01', 
    end='2015-01-29'
)

Corn = continuous_future( 'CN' , roll = 'volume')  #Corn Futures

Corn = history(
    Corn, 
    fields='price', 
    frequency='daily', 
    start='2014-10-01', 
    end='2015-05-29'
)

Corn2 = continuous_future( 'CN' , roll = 'volume')  #Corn Futures

Corn2 = history(
    Corn2, 
    fields='price', 
    frequency='daily', 
    start='2015-10-01', 
    end='2016-05-29'
)

Corn3 = continuous_future( 'CN' , roll = 'volume')  #Corn Futures

Corn3 = history(
    Corn3, 
    fields='price', 
    frequency='daily', 
    start='2016-10-01', 
    end='2017-05-29'
)


# In[20]:


x=scipy.signal.savgol_filter( Corn3, 39, 2, 0, 1.0, -1, 'interp', 0.0 )   
df = pd.DataFrame( x, index = Corn3.index )  #Create dataframe
plt.plot(Corn3, "y" )  
plt.plot(df,"b")
plt.figtext(.5,.8,'Corn 2017',fontsize=30,ha='center')


# In[18]:


x=scipy.signal.savgol_filter( Corn2, 39, 2, 0, 1.0, -1, 'interp', 0.0 )   
df = pd.DataFrame( x, index = Corn2.index )  #Create dataframe
plt.plot(Corn2, "y" )  
plt.plot(df,"b")
plt.figtext(.5,.8,'Corn 2016',fontsize=30,ha='center')


# In[ ]:


WTI.corr(Corn)


# In[4]:


len(Corn.index)


# In[19]:


x=scipy.signal.savgol_filter( Corn, 39, 2, 0, 1.0, -1, 'interp', 0.0 )   
df = pd.DataFrame( x, index = Corn.index )  #Create dataframe
plt.plot(Corn, "y" )  
plt.plot(df,"b")  
plt.figtext(.5,.8,'Corn 2015',fontsize=30,ha='center')


# In[21]:


x=scipy.signal.savgol_filter( WTI, 39, 2, 0, 1.0, -1, 'interp', 0.0 )   
df = pd.DataFrame( x, index = WTI.index )  #Create dataframe
plt.plot(WTI, "y" )  
plt.plot(df,"b")
plt.figtext(.5,.8,'OIL 2015',fontsize=30,ha='center')


# In[7]:


corn = pd.Series(np.gradient(df[0]), df.index)


# In[29]:


#this prints out the exact trend dates
i = 0
while ( i < (len(corn)) ):
    
    if( ( corn[i] > 0 ) and ( corn[i+1] < 0 ) ):
        print ( "Max: ", corn.index[i] , round(corn.values[i], 6) , corn.index[i+1], round(corn.values[i+1],6) )
    
    if( ( corn[i] < 0 ) and ( corn[i+1] > 0 ) ):
        print ( "Min: ", corn.index[i] , round(corn.values[i], 6) , corn.index[i+1], round(corn.values[i+1],6) )
    
    i+=1


# In[28]:


plt.plot(corn)


# In[28]:


#Loop that delets all outlier dates
i = 0
count = 0 
while( i < len(corn) ): 
    
    if( (corn[i-1] == None) or (corn[i] == None) ):
        break
    
    if( (corn[i-1] < 0) and (corn[i] > 0 ) and ( corn[i+1] < 0)):
        corn = corn.drop( labels=[corn.index[i]] )
    
    if( ( corn[i-1] > 0 ) and ( corn[i] < 0 ) and ( corn[i+1] > 0 ) ):
        corn = corn.drop( labels=[corn.index[i]] )
    
    i+=1


# In[40]:


# For loop that just loops and counts 
j=0
for i in corn:
    print (i , j)
    j+=1


# In[ ]:


# Ignor this while loop for now
#i = 0
#while( i < len(corn) ): 
 #   i+=1
  #  if( (df[0][i-1] == None) or (df[0][i+1] == None) ):
   #     break
    #if( (df[0][i-1] < 0) and (df[0][i] > 0 ) and ( df[0][i+1] < 0)):
     #   del df[0][i]

