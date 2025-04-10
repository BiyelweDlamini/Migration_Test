# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

#from sklearn.model_selection import train_test_split

#DATA COLLECTION

#initialize file path and add the r prefix to prefix the string to let Python know that it is a raw string (to avoid the backlashes being seen as escape sequences)
migrationFilePath = r'C:\Users\biyel\OneDrive\Desktop\Project_2025\Migration_Test\IndianMigrationHistory.csv'

#read the csv file

migrationData = pd.read_csv(migrationFilePath)

#print all the columns in the csv file

#Columns before the column 2000 [2000] is changed to target
#print(migrationData.columns)

#Set the targert

#Rename the target column 

migrationData.rename(columns = {'2000 [2000]' : 'target'}, inplace = True)

#Columns after the column 2000 [2000] is changed to target
#print(migrationData.columns)

# Renamed target stored in the variable y and set as the target
y = migrationData.target

#Selecting the features

migrationFeatures = ['Country Origin Name', 'Country Origin Code',
                      'Migration by Gender Name', 'Migration by Gender Code',
                      'Country Dest Name', 'Country Dest Code', '1960 [1960]', 
                      '1970 [1970]','1980 [1980]', '1990 [1990]']

#Storing the features in the x variable

X = migrationData[migrationFeatures]

print(X.describe())

print(X.head())

#splitting data for training and validation for more accurate results
#trainX, valX, trainy, valy = train_test_split(X, y, random_state = 0)

# Defining the model and specifying the random state

migrationModel = RandomForestRegressor(random_state=1)

# Fitting the model, or training the model

#migrationModel.fit(X, y)






