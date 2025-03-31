# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#initialize file path and add the r prefix to prefix the string to let Python know that it is a raw string (to avoid the backlashes being seen as escape sequences)
migration_file_path = r'C:\Users\biyel\OneDrive\Desktop\Project_2025\Migration_Test\IndianMigrationHistory.csv'

#read the csv file

migration_data = pd.read_csv(migration_file_path)

#print all the columns in the csv file

print(migration_data.columns)

#set the targert

y = migration_data['2000[2000]']

#Selecting the features

migration_features = ['Country Origin Name', 'Country Origin Code',
                      'Migration by Gender Name', 'Migration by Gender Code',
                      'Country Dest Name', 'Country Dest Code', '1960 [1960]', 
                      '1970 [1970]','1980 [1980]', '1990 [1990]']

#Storing the features in the x variable

X = migration_data[migration_features]