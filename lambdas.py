"""
Learning pandas library operations with help of lambda for function expressions
"""
import pandas as pd

#dictionary {'key':value, 'key':[value1, value2]}
df = pd.DataFrame({
    'Name': ['Luke','Gina','Sam','Emma'],
    'Status': ['Father', 'Mother', 'Son', 'Daughter'],
    'Birthyear': [1976, 1984, 2013, 2016],
})
print(df)
print("-----------------------------")

#Higher Order Functions:
# When a function or method takes a function as an argument (or returns a function), it is called a "higher-order function".

#This function applies an operation to every element of the column.
df['age'] = df['Birthyear'].apply(lambda x: 2021-x)
print(df)
print("-----------------------------")

#Double the age of everyone
df['double_age'] = df['age'].map(lambda x: x*2)
print(df)
print("-----------------------------")

#Lambda with conditional statement
df['Gender'] = df['Status'].map(lambda x: 'Male' if x == 'Father' or x == 'Son' else 'Female')
print(df)
print("-----------------------------")

#The Pandas "Series" object
"""
A Pandas Series is a one-dimensional array of indexed data. It can be created from a list or array as follows:
"""
data = pd.Series(['white', 'yellow', 'blue', 'red']) #Series object assigns the indexing to the list of items in the array
print(data)
print("-----------------------------")
#print(data.keys) - prints the keys
#print(data.values) - prints the values
