# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:49:58 2023

@author: anany
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.tools as tls
import plotly.graph_objects as go

df1=pd.read_csv("C:\\Users\\anany\\OneDrive\\Documents\\UGPP year 3\\Sem 5\\SA\\Task 4\\Data viz\\dataset1.csv")
print(df1)

df1 = df1.replace('NA', np.nan)


#Country vs Year vs Globalization index vs Gender wage gap %
plt.figure(figsize=(10,8))
ax=plt.axes(projection='3d')

scatter_plot=ax.scatter3D(df1['Gender wage gap %'],df1['Year'],df1['Globalization index'],
                          c=df1['CountryCode'] ,cmap='autumn')

plt.colorbar(scatter_plot)

ax.set_xlabel('Gender wage gap %')
ax.set_ylabel('Year')
ax.set_zlabel('Globalization Index')

plt.show()




#Country vs Year vs Labour force participation(men) vs Population
plt.figure(figsize=(10,8))
ax=plt.axes(projection='3d')

scatter_plot=ax.scatter3D(df1['% Labour force participation(Men)'],df1['Year'],df1['Population'],
                          c=df1['CountryCode'] ,cmap='autumn')

plt.colorbar(scatter_plot)

ax.set_xlabel('Labour force participation(Men')
ax.set_ylabel('Year')
ax.set_zlabel('Population')

plt.show()



#Country vs Year vs Labour force participation(women) vs Population
plt.figure(figsize=(10,8))
ax=plt.axes(projection='3d')

scatter_plot=ax.scatter3D(df1['% Labour force participation(Women)'],df1['Year'],df1['Population'],
                          c=df1['CountryCode'] ,cmap='autumn')

plt.colorbar(scatter_plot)

ax.set_xlabel('Labour force participation(women)')
ax.set_ylabel('Year')
ax.set_zlabel('Population')

plt.show()


#Country vs Year vs Employment rates of women with Low education level and have atleast 1 child vs Population
plt.figure(figsize=(10,8))
ax=plt.axes(projection='3d')

scatter_plot=ax.scatter3D(df1['Employment rates of women with Low education level and have atleast 1 child'],df1['Year'],df1['Population'],
                          c=df1['CountryCode'] ,cmap='winter')

plt.colorbar(scatter_plot)

ax.set_xlabel('Employment rates of women with Low education level and have atleast 1 child')
ax.set_ylabel('Year')
ax.set_zlabel('Population')

plt.show()


#Country vs Year vs Employment rates of women with Moderate education level and have atleast 1 child vs Population
plt.figure(figsize=(10,8))
ax=plt.axes(projection='3d')

scatter_plot=ax.scatter3D(df1['Employment rates of women with Moderate education level and have atleast 1 child'],df1['Year'],df1['Population'],
                          c=df1['CountryCode'] ,cmap='winter')

plt.colorbar(scatter_plot)

ax.set_xlabel('Employment rates of women with Moderate education level and have atleast 1 child')
ax.set_ylabel('Year')
ax.set_zlabel('Population')

plt.show()







