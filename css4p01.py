# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
df = pd.read_csv("movie_dataset.csv")
print(df.info())

# Remove spaces in column names
df.columns = df.columns.str.replace(' ', '_')

# Remove NANs, filling missing numerical values with the mean
x = df["Revenue_(Millions)"].mean()
df["Revenue_(Millions)"].fillna(x, inplace = True)

x = df["Metascore"].mean()
df["Metascore"].fillna(x, inplace = True)

print(df)

# Save the cleaned dataset
df.to_csv("C:/Users/sikha/Project_IMDB_Data/Output/movie_dataet_cleaned.csv", index=False)


import pandas as pd 
df = pd.read_csv("Output/movie_dataet_cleaned.csv")

#Question 2 
avg_revenue = df['Revenue_(Millions)'].mean()
print(avg_revenue)

#Question 3
df_3 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
                                                   
avg_revenue_2 = df_3['Revenue_(Millions)'].mean()
print(avg_revenue)

#Question 4 
print(df[df['Year'] == 2016])

#Question 5
print(df[df['Director'] == 'Christopher Nolan'])

#Question 6 
print(df[df['Rating'] >= 8.0])

#Question 7
df_6 = df[df['Director'] == 'Christopher Nolan']
med_rating = df_6['Rating'].median()
print(med_rating)

#Question 8 
df_7 = df.groupby('Year')['Rating'].mean()
max_avg_rating = df_7.idxmax()
print(max_avg_rating)
                                                   
#Question 9
df_81 = df[(df['Year'] == 2006)] 
df_82 = df[(df['Year'] == 2016)]

movies_2006 = len(df_81)
movies_2016 = len(df_82)

perc_inc = ((movies_2016 - movies_2006)/movies_2006) * 100

#Question 10
df_9 = df['Actors'].str.split(',').explode().str.strip()
common_actor = df_9.mode().iloc[0]

# Question 11
df_10 = df['Genre'].str.split(',').explode().str.strip()
no_unique = df_10.nunique()

#Question 12

df_12 = df.select_dtypes(include='number')

corr_matrix = df_12.corr()
print(corr_matrix)

# Visualize 
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Correlation Matrix")
plt.show()





















