# -*- coding: utf-8 -*-
"""Exploratory_Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ACTjcAw2ki1TJBd46jVIpWJzDZdx3ZUu
"""

# Connect the colab notebook with drive
from google.colab import drive
drive.mount('/content/drive')

#import necessary packages
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from sklearn import preprocessing

# import data from the drive
data = pd.read_csv("/content/drive/MyDrive/customer_churn_for_github/Churn_Modelling.csv")

# print the first few rows of the data and make sure the data is loaded correctly
data.head(10)

# print the first few rows of the data and make sure the data is loaded correctly
data.tail()

# check the shape of the data(rows,columns)
data.shape

#Check the type of variables in tha dataset
data.info()

#Check if there is any null values in the dataset
data.isnull().sum()

"""### **print the unique values in each column and find if there is any wrongly enterd values**

"""

data.loc[data['RowNumber'].idxmax()]

# find maximum value of a column

maxClm = data['RowNumber'].max()

print("Maximum value in column 'RowNumber': ",maxClm)

# find minimum value of a column
minClm = data['RowNumber'].min()

print("Minimum value in column 'RowNumber': ",minClm)

# another method to find the maximum value

maxClm = data['RowNumber'].max()

print("Maximum value in column 'RowNumber': ",maxClm)

maxage = data['Age'].max()
minage = data['Age'].min()

print("Maximum value in column 'Age': ",maxage)
print("Minimum value in column 'Age': ",minage)

maxcreditscore = data['CreditScore'].max()
mincreditscore = data['CreditScore'].min()

print("Maximum value in column 'CreditScore': ",maxcreditscore)
print("Minimum value in column 'CreditScore': ",mincreditscore)

maxTenure  = data['Tenure'].max()
minTenure  = data['Tenure'].min()

print("Maximum value in column 'Tenure': ",maxTenure)
print("Minimum value in column 'Tenure': ",minTenure)

maxBalance  = data['Balance'].max()
minBalance  = data['Balance'].min()


print("Maximum value in column 'Balance': ",maxBalance)
print("Minimum value in column 'Balance': ",minBalance)

maxEstimatedSalary  = data['EstimatedSalary'].max()
minEstimatedSalary  = data['EstimatedSalary'].min()

print("Maximum value in column 'EstimatedSalary': ",maxEstimatedSalary)
print("Minimum value in column 'EstimatedSalary': ",minEstimatedSalary)

# Print unique values of a column
print(data.Geography.unique())

# Another method to print unique values of a column
print(pd.unique(data['Geography']))

print(data.Gender.unique())

print(data.NumOfProducts.unique())

print(data.IsActiveMember.unique())

print(data.Exited.unique())

import plotly.express as px
# df = px.data.tips()
fig = px.histogram(data, x="CreditScore",title= "Histogram fo creditScore")
fig.show()

# Get count duplicates single column using dataframe.pivot_table()
df2 = data.pivot_table(index = ['Geography'], aggfunc ='size')
print(df2)

# initialize list elements

unique_counts= [["France",5014],["Germany",2509],["Spain",2477]] 

# Create the pandas DataFrame with column name is provided explicitly
geo_data = pd.DataFrame(unique_counts, columns=['Geography','count'])

# print dataframe.
geo_data

import plotly.express as px

fig = px.pie(geo_data, values='count', names='Geography', color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()

import plotly.express as px

fig = px.histogram(data, x="Gender", y="Exited",
             color='Exited', barmode='group',
             height=400)
fig.show()

import plotly.express as px
# data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.histogram(data, x='Gender',color="Exited",title="Histogram of Churned and not churned customers based on Gender")
fig.show()

import plotly.express as px
fig = px.scatter_matrix(data, dimensions=['CreditScore','Gender','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary','Exited'], color="Exited")
fig.show()

'CreditScore','Gender','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary','Exited'

import plotly.express as px
# df = px.data.tips()
fig = px.ecdf(data, x="IsActiveMember", color="Exited")
fig.show()