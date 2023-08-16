#!/usr/bin/env python
# coding: utf-8

# <h1><center> PPOL564 - Data Science I: Foundations<br><br><font color='grey'> Working with Nested Lists </font> </center><h1>

# ## Learning Goals
# 
# In this notebook, we will cover:
# 
# - open csv as nested lists
# - Working with retangular data as nested lists
# - Intro to `numpy`
# 
# 
# This is mostly code I will go over during the lecture. 

# In[1]:


# Batteries included Functions
import csv # convert a .csv to a nested list
import os  # library for managing our operating system. 


# Read in the gapminder data 
with open("gapminder.csv",mode="rt") as file:
    data = [row for row in csv.reader(file)]


# What does the data looks like?

# In[2]:


# it is a nested list. 
data


# ## Indexing Nested Lists
# 
# Notice something important here, because we open the data using a iterator, the code doesn't know that the first row is the header of the csv

# In[6]:


# accessing the header
print(data[0])

# %% -----------------------------------------
# Indexing Rows


# For any row > 0, row == 0 is the column names. 
print(data[100])


# ### Indexing by columns

# In[ ]:


# Indexing Columns - Remember this is a nested lest

# Referencing a column data value
d = data[100] # First select the row
d[1] # Then reference the column

# doing the above all in one step
data[100][1]

# The key is to keep in mind the column names
cnames = data.pop(0)

# We can now reference this column name list to pull out the columns we're interested in.
ind = cnames.index("lifeExp") # Index allows us to "look up" the location of a data value. 
data[99][ind]


# %% -----------------------------------------
# Drawing out specific COLUMN of data

# identify the position
ind = cnames.index("lifeExp")


# ## Accessing a entire column
# 
# If I want to extract all the values of a particular columns, I need to loop through all the *j* element of a sublist. 

# In[ ]:


# Looping through each row pulling out the relevant data value
life_exp = []
for row in data:
    life_exp.append(float(row[ind]))

# Same idea, but as a list comprehension 
life_exp = [float(row[ind]) for row in data]


# Make this code more flexible 
var_name = "gdpPercap"
out = [row[cnames.index(var_name)] for row in data]
out


# ## Motivating Numpy
# 
# All of the above seems a little to much for working with retangular data in Python. And it is. 
# 
# A first approach to facilitate our lifes will be using `numpy` to convert nested lists in `arrays`. If you coming from R, think about numpy arrays as matrices. 
# 
# We will see more of numpy soon. However, let's compare briefly the speed boost of using numpy to access data in Python
# 

# In[ ]:


# %% -----------------------------------------
# Numpy offers an efficiency boost, especially when indexing
import numpy as np


# Convert to a numpy array
data_np = np.array(data)


# Column Variable we wish to access is easy using slicing. 
data_np[:,2]


# We will see more of numpy soon. However, let's compare briefly the speed boost of using numpy to access data in Python

# In[ ]:


# We want to access all the observations of a dataset. Which way is faster?

# %% -----------------------------------------
get_ipython().run_line_magic('%timeit', '')
out1 = []
for row in data:
    out1.append(row[var_ind])


# %% -----------------------------------------
get_ipython().run_line_magic('%timeit', '')
out2 = [row[var_ind] for row in data]

    
# %% -----------------------------------------
get_ipython().run_line_magic('%timeit', '')
out3 = data_np[:,var_ind]


# In[ ]:


#

