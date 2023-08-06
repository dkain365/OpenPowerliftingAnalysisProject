# -*- coding: utf-8 -*-
"""USAPL Growth Chart

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dF-Yiq7kXvTdm37-xuUAuey60ds9Ac6b

# **USAPL Growth Chart by Year**
"""

# Line chart to see the rate of growth in the USAPL by year.
# This graph considers the unique names of athletes, determining
# how many unique individuals have entered a USAPL competiton by year

import pandas as pd
import matplotlib.pyplot as plt

path_to_csv = 'FinalOpenPowerliftingAugust2023.csv'

df = pd.read_csv(path_to_csv)

# Convert the "Date" column to datetime type to facilitate grouping by year
df['Date'] = pd.to_datetime(df['Date'])


df['Year'] = df['Date'].dt.year

# Filter the DataFrame for Males & Females seperately
df_male = df[df['Sex'] == 'M']
df_female = df[df['Sex'] == 'F']


unique_name_counts_male = df_male.groupby('Year')['Name'].nunique()
unique_name_counts_female = df_female.groupby('Year')['Name'].nunique()


plt.figure(figsize=(10, 6))
plt.plot(unique_name_counts_male.index, unique_name_counts_male, marker='o', color='blue', label='Male')
plt.plot(unique_name_counts_female.index, unique_name_counts_female, marker='o', color='magenta', label='Female')



plt.title('USAPL Growth Chart (2015 - 2023)', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Count of Unique Athletes', fontsize=16)
plt.xticks(rotation=0)
plt.legend(loc='upper left', prop={'size': 14})

plt.grid(True)

plt.show()