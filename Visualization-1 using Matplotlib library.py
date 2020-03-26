#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn-whitegrid')
X=[590,540,740,130,810,300,320,230,470,620,770,250]
Y=[32,36,39,52,61,72,77,75,68,57,48,48]
plt.scatter(X,Y)
plt.xlim(0,1000)
plt.ylim(0,100)
#Adding color to scatter plot
plt.scatter(X,Y,s=60,c='red',marker='^')
#Change axes ranges
plt.xlim(0,1000)
plt.ylim(0,100)
#Axis Title
plt.title('Relationship between temparature and iced coffee sales')

#add x and y labels
plt.xlabel('Sold Coffee')
plt.ylabel('Temperature in Fahrenheit')

#Show plt
plt.show()


# In[2]:





# In[ ]:




