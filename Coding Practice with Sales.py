#Coding practice 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


data_file_path = os.path.join(os.path.dirname(__file__), "data","sales_data.csv") #setting path 
sales = pd.read_csv(data_file_path, parse_dates = ['Date']) #reading csv file 

sales.head() #return first rows in dataframe (can set n = to any integer)

print("Mean Age of Customer:", sales["Customer_Age"].mean()) #calling the header "Customer_age" with a DataFrame index (column name) and taking the mean with .mean()

#Show KDE type graph with Customer Age data 
#sales["Customer_Age"].plot(kind="kde", figsize=(10,7))
#plt.show()

#Show CUstomer age with a box plot 
#sales["Customer_Age"].plot(kind='box', vert = False, figsize=(10,7))
#plt.show()

##Mean of OrderQuanity 

print("Mean Order Quanity:", sales['Order_Quantity'].mean())

##Histogram of order quanity 

#sales["Order_Quantity"].plot(kind ='hist', bins = 30, figsize=(7,4))
#plt.show()

##Numer of sales per year 

print(sales['Year'].value_counts())#Sales looking at year and printing the sales per year with value_counts. where value_counts returns every year and counts return the total

##Pie Chart of number of sales per year
#sales["Year"].value_counts().plot(kind='pie', figsize=(5,3))
#plt.show()

##Sales per month
print(sales['Month'].value_counts())

##Bar chart of sales per month
#sales["Month"].value_counts().plot(kind= 'bar', figsize=(7,7))
#plt.show()

##Which country has the most sales 

print(sales["Country"].value_counts().head(1)) #Retuning the country with the most sales with .head returning the list of country and [1] returning the first one
print(sales["Country"].value_counts())#returning the country list in dataframe 

#bar chart of the amount of sales per country 

sales["Country"].value_counts().plot(kind = 'bar', figsize=(7,4))
plt.show()



