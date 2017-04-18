# LValadez_Livesession12assignment
Live Session Unit 12 Assignment
     
1.	Create a list named my_list in python with the following data points - 
45.4 44.2 36.8 35.1 39.0 60.0 47.4 41.1 45.8 35.6
a.	Print the 5th element in the list
b.	Append 55.2 to my_list
c.	Remove the 6th element in the list
d.	Iterate over the list to print data points greater than 45
2.	Introduction to numpy – 
a.	Import the numpy library using the following command – import numpy
b.	Declare numpy array with the same data points as in my_list using numpy.array()
c.	Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
d.	Use logical referencing to get only those values that are less than 45
e.	Compute the max and min of the array using numpy.max() and numpy.min()
3.	Introduction to pandas – 
a.	Import the pandas library – import pandas
b.	Read the IRIS dataset into iris using pandas.read_csv(). 
Data file – 
c.	Using iris.head(), display the head of the dataset
d.	Use DataFrame.drop() to drop the id column
e.	Subset dataframe to create a new data frame that includes only the measurements for the setosa species
f.	Use DataFrame.describe() to get the summary statistics
g.	Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()
h.	Use DataFrame.boxplot() to plot boxplots by Species

i.	Plot a scatter matrix plot using the seaborn library. Use the following to load and plot 
i.	Import seaborn
ii.	Seaborn.pairplot(dataframe,by=’column_name’)

