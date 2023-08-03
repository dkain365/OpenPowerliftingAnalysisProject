# -*- coding: utf-8 -*-
"""Top_Bottom_25_States_Lifter_Count_Visualizations

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VDAngEu8kb9P6x3jVHzTrt9JF4Mdn9ZP

**Bar Graphs -- States with the most unique lifters since 2015**

**Bar graph of all 50 states -- Too clunky, will break down into Top & Bottom 25**
"""

import pandas as pd
import matplotlib.pyplot as plt

path_to_csv_file = 'FinalOpenPowerliftingAugust2023.csv'


df = pd.read_csv(path_to_csv_file)

# Drop duplicate rows based on the 'Name' column, keeping the first occurrence
df_unique_names = df.drop_duplicates(subset='Name', keep='first')

# Get the counts of unique values in the 'State' column after removing duplicates
state_counts = df_unique_names['State'].value_counts()

# Bar chart
plt.figure(figsize=(12, 6))
state_counts.plot(kind='bar', color=['blue', 'green', 'orange', 'red', 'purple', 'brown'])

# Customize the chart
plt.title('Lifters By State', fontsize=16)
plt.xlabel('State', fontsize=14)
plt.ylabel('Count of Lifters', fontsize=14)
plt.xticks(rotation=45, ha='right')


plt.tight_layout()
plt.show()

"""**Horizontal Bar Graph - Top 25 States with the most Unique Lifters Since 2015**"""

path_to_csv_file = 'FinalOpenPowerliftingAugust2023.csv'

df = pd.read_csv(path_to_csv_file)

#Drop Duplicate names
df_unique_names = df.drop_duplicates(subset='Name', keep='first')

# Get the counts of unique values in the 'State' column after removing duplicates
state_counts = df_unique_names['State'].value_counts()

# Sort the state_counts Series in ascending order
state_counts_sorted = state_counts.sort_values(ascending=True)


top_25_states = state_counts_sorted.tail(25)


plt.figure(figsize=(10, 8))
top_25_states.plot(kind='barh', color=plt.cm.Paired.colors)


plt.title('25 States with the Most Lifters', fontsize=16)
plt.xlabel('Count of Lifters', fontsize=14)
plt.ylabel('State', fontsize=14)

plt.tight_layout()
plt.show()

"""Horizontal Bar Graph - Bottom 25 States with the least Unique Lifters Since 2015"""

path_to_csv_file = 'FinalOpenPowerliftingAugust2023.csv'

df = pd.read_csv(path_to_csv_file)

# Drop duplicate rows based on the 'Name' column, keeping the first occurrence
df_unique_names = df.drop_duplicates(subset='Name', keep='first')


# Get the counts of unique values in the 'State' column after removing duplicates
state_counts = df_unique_names['State'].value_counts()


# Sort the state_counts Series in ascending order
state_counts_sorted = state_counts.sort_values(ascending=True)



bottom_25_states = state_counts_sorted.head(25)



plt.figure(figsize=(10, 10))
bottom_25_states.plot(kind='barh', color=plt.cm.Paired.colors)


plt.title('25 States with the Least Lifters', fontsize=16)
plt.xlabel('Count of Lifters', fontsize=14)
plt.ylabel('State', fontsize=14)


plt.tight_layout()
plt.show()

"""**Grabbing Insights**

Total Lifter Counts
"""

#Total Count of combined Unique Lifters in the Bottom 25 States

path_to_csv_file = 'FinalOpenPowerliftingAugust2023.csv'

df = pd.read_csv(path_to_csv_file)

# Drop duplicate rows from name column
df_unique_names = df.drop_duplicates(subset='Name', keep='first')


# Get the counts of unique values in State column
state_counts = df_unique_names['State'].value_counts()



state_counts_sorted = state_counts.sort_values(ascending=True)


bottom_25_states = state_counts_sorted.head(25)


total_count_bottom_states = bottom_25_states.sum()

print("Total lifter count: bottom 25 states =", total_count_bottom_states)