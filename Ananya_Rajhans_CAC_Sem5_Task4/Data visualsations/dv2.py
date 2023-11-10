# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 06:04:05 2023

@author: anany
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df1=pd.read_csv("C:\\Users\\anany\\OneDrive\\Documents\\UGPP year 3\\Sem 5\\SA\\Task 4\\Data viz\\dataset1.csv")
print(df1)



df1 = df1.replace('NA', np.nan)


#Country vs Year vs Gender wage gap %
plt.figure(figsize=(10,8))
ax=plt.axes(projection='3d')

scatter_plot=ax.scatter3D(df1['Gender wage gap %'],df1['Year'],df1['CountryCode'],
                          cmap='autumn')

plt.colorbar(scatter_plot)

ax.set_xlabel('Gender wage gap %')
ax.set_ylabel('Year')
ax.set_zlabel('Country Code')

plt.show()