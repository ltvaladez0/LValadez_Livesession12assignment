
# coding: utf-8

# In[1]:

##Leticia Valadez 
##MSDS 6306-402
##Assignment 12
##April 20, 2017


# In[2]:

#1. Create a list named my_list
my_list = [45.4, 44.2, 36.8,  35.1, 39.0, 60.0,  47.4,  41.1,  45.8, 35.6]

#a.Print the 5th element in the list
print (my_list[4])


# In[3]:

#b.Append 55.2 to my_list
my_list.append(55.2) 
print (my_list)


# In[4]:

#c. Remove the 6th element in the list
del my_list[5]
print (my_list)


# In[5]:

#d. Iterate over the list to print data points greater than 45
x= [x for x in my_list if x >45]
print (x)


# In[6]:

#2. Introduction to numpy – 
#a. Import the numpy library
import numpy


# In[7]:

#b. Declare numpy array with the same data points as in my_list using numpy.array()
numpylist=numpy.array(my_list)
print(numpylist)


# In[8]:

#c. Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
numpylist_mean=numpy.mean(numpylist)
print(numpylist_mean)


# In[9]:

numpylist_std=numpy.std(numpylist)
print(numpylist_std)


# In[10]:

#d. Use logical referencing to get only those values that are less than 45
numpylist_lessthan45=numpylist[numpylist < 45]
print(numpylist_lessthan45)


# In[11]:

#e. Compute the max and min of the array using numpy.max() and numpy.min()
numpylist_max=numpy.max(numpylist)
print(numpylist_max)


# In[12]:

numpylist_min=numpy.min(numpylist)
print(numpylist_min)


# In[13]:

#3. Introduction to pandas – 
#a. Import the pandas library
import pandas


# In[14]:

#b. Read the IRIS dataset into iris using pandas.read_csv().
Iris=pandas.read_csv("Iris.csv")


# In[15]:

#c. Using iris.head(), display the head of the dataset
Iris.head()


# In[16]:

#d. Use DataFrame.drop() to drop the id column
Iris_dropId=Iris.drop('Id', 1)
Iris_dropId.head()


# In[17]:

#e.Subset dataframe to create a new data frame that includes only the measurements for the setosa species
Iris_setosa= Iris_dropId[Iris_dropId.Species == "Iris-setosa"]


# In[18]:

#f. Use DataFrame.describe() to get the summary statistics (for setosa species)
Iris_setosa.describe()


# In[19]:

#g. Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()
Iris_grouped = Iris_dropId.groupby('Species')
Iris_grouped.head()


# In[20]:

Iris_grouped.describe()


# In[21]:

#h. Use DataFrame.boxplot() to plot boxplots by Species
#Display all plots in this notebook
get_ipython().magic('matplotlib inline')
Iris_grouped.boxplot(figsize=(15, 20))


# In[22]:

#i.Plot a scatter matrix plot using the seaborn library. Use the following to load and plot 
import seaborn as sns
sns.pairplot(Iris_dropId,hue='Species')

