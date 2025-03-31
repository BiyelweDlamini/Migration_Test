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

y = [["2000[2000]"]] 

#Select the features


