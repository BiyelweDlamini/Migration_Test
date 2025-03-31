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
migration_data = pd.read_csv(migration_file_path)
print(migration_data.columns)

y = [[2000[2000]]] 
