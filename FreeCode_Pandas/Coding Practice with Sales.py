#Coding practice 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


data_file_path = os.path.join(os.path.dirname(__file__), "data","sales_data.csv") #setting path 
sales = pd.read_csv(data_file_path, parse_dates = ['Date']) #reading csv file 

sales.head() #return first rows in dataframe (can set n = to any integer)

#print("Mean Age of Customer:", sales["Customer_Age"].mean()) #calling the header "Customer_age" with a DataFrame index (column name) and taking the mean with .mean()

#Show KDE type graph with Customer Age data 
#sales["Customer_Age"].plot(kind="kde", figsize=(10,7))
#plt.show()

#Show CUstomer age with a box plot 
#sales["Customer_Age"].plot(kind='box', vert = False, figsize=(10,7))
#plt.show()

##Mean of OrderQuanity 

#print("Mean Order Quanity:", sales['Order_Quantity'].mean())

##Histogram of order quanity 

#sales["Order_Quantity"].plot(kind ='hist', bins = 30, figsize=(7,4))
#plt.show()

##Numer of sales per year 

#print(sales['Year'].value_counts())#Sales looking at year and printing the sales per year with value_counts. where value_counts returns every year and counts return the total

##Pie Chart of number of sales per year
#sales["Year"].value_counts().plot(kind='pie', figsize=(5,3))
#plt.show()

##Sales per month
#print(sales['Month'].value_counts())

##Bar chart of sales per month
#sales["Month"].value_counts().plot(kind= 'bar', figsize=(7,7))
#plt.show()

##Which country has the most sales 

#print(sales["Country"].value_counts().head(1)) #Retuning the country with the most sales with .head returning the list of country and [1] returning the first one
#print(sales["Country"].value_counts())#returning the country list in dataframe 

#bar chart of the amount of sales per country 


#plt.show()

#Searching for unique or elements that only show up once in the selected data frame
#sales["Product"].value_counts().head(10).plot(kind = 'bar', figsize= (7,4))
#plt.show()
##Correlation between unit cost and unit price 
#sales.plot(kind= 'scatter', x='Order_Quantity', y='Profit', figsize=(7,5))

#sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10,6))


#sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10,6))

##Creating a month date and year column 

sales["Calculated_Date"] = sales[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis = 1) #Creating new column
#print(sales["Calculated_Date"].head())

#Parsing new column we created 

sales["Calculated_Date"] = pd.to_datetime(sales["Calculated_Date"])

#Lineplot with calculated date as the oclumn nad sount as the y axis 

#sales['Calculated_Date'].value_counts().plot(kind= 'line', figsize= (7,5))


## Add 50 to everycell in revenue 

sales["Revenue"] = sales["Revenue"] +50 

#print(sales["Revenue"])

##How many sales were made in Canada and France 
#print(sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0]) #| CHecks both canada and france for sales

##How many bike racks orders in canada 
#print(sales.loc[(sales['Country'] == 'Canada') & (sales["Sub_Category"] == 'Bike Racks')].shape[0]) # & checks that it needs to be in canada AND have Bike racks

france_states = sales.loc[sales['Country']== 'France', 'State'].value_counts() #Looking at france and states with loc and counting them
#print(france_states)

#france_states.plot(kind='bar', figsize=(7,5))

#How many sales were made per category 

#print(sales['Product_Category'].value_counts()) #Count all the values in product category 

#sales['Product_Category'].value_counts().plot(kind='pie', figsize=(7,7))

##How many orders were made per accessory sub-category

accessories = sales.loc[sales["Product_Category"] == 'Accessories', 'Sub_Category'].value_counts() #looking at accessories and sub category that is equal to that of product category 
print(accessories)

#accessories.plot(kind = 'bar', figsize=(10,7))

bikes = sales.loc[sales["Product_Category"] == 'Bikes', 'Sub_Category'].value_counts() ##count the values of sub category that are the same as bikes in product category
print(bikes)

#bikes.plot(kind = 'pie', figsize= (5,5))

###What gender has the most sales 

#print(sales["Customer_Gender"].value_counts())#Count all of the elements in Customer Gender

##How many sales with more than 500 in revenue were made by men 

#print(sales.loc[(sales['Customer_Gender']=='M') & (sales['Revenue'] == 500)].shape[0]) #Look for a M customer gender and 500 revenue (.loc looks for arguments) (.shape returns number of elements)

#print(sales['Revenue'].sort_values(ascending= False).head(5)) #return the 5 values in ascending order of the sorted revenue values 

#Highest reveune 
#print(sales['Revenue'].sort_values(ascending= False).head(1))

max_rev= sales['Revenue'] == sales['Revenue'].max()
#print(sales.loc[max_rev])

f = sales['Revenue'] > 10000

print(sales.loc[f, "Order_Quantity"].mean())

f1 = sales['Revenue'] <10000
print(sales.loc[f1, "Order_Quantity"].mean())

m = (sales['Year'] == 2016) & (sales['Month'] == 'May')
print(sales.loc[m].shape[0])

cond = (sales['Year'] == 2016) & (sales['Month'] == 'May')

print(sales.loc[cond].shape[0])


### sales in 2016 that is for may-july
mj =  ((sales['Month'] == 'May') | (sales['Month'] == 'July') | (sales['Month'] == 'June')) & (sales['Year'] == 2016)

print(sales.loc[mj].shape[0])


profit_2016 = sales.loc[sales['Year'] == 2016, ['Profit', 'Month']] #looking at rows profit and month in the year 2016


filt = (sales['Country'] == 'United States', 'Unit_Price')

print(sales.loc[filt])
print(sales.loc[sales['Country'] == 'United States', 'Unit_Price'])

