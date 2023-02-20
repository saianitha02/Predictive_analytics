#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/deep-bits/PA/blob/main/Python_probability_plots" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[1]:


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
from sklearn.datasets import load_iris
from sklearn import preprocessing


# In[2]:


mu, sigma = 0, 1 # mean and standard deviation
rsnd = np.random.normal(mu, sigma, size = 1000)
#print("Distribution = ",rsnd)
print("Mean = ",abs(mu - np.mean(rsnd)))
print("S.D. = ",abs(sigma - np.std(rsnd)))


# In[3]:


count, bins, ignored = plt.hist(rsnd, 50, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=4, color='green')
plt.show()


# In[4]:


res = stats.probplot(rsnd, plot=plt)


# In[5]:


data = load_iris()

# Raw variables
predictors = data.data #{Petal,Sepal}x{Width,Length}
target = data.target #Species

# Standardization
predictors_Z = preprocessing.scale(predictors)
print("Mean = ", st.mean(predictors_Z[:,0]))
print("S.D. = ", st.stdev(predictors_Z[:,0]))


# In[6]:


res = stats.probplot(predictors[:,0], plot=plt)


# In[7]:


res = stats.probplot(predictors_Z[:,0], plot=plt)


# In[9]:


print("Skewness =",stats.skew(predictors_Z[:,0]))

