import pandas as pd
import random

df2 = pd.read_csv('datasets/OrderReport.csv')

# create an age column for the dataset to give the customers age
# create an age distribution from  25 to 45
# create a random age for each customer
# save the dataset as a csv file

age_distribution = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
# the percentage of customers in each age group
age_distribution_percentage = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                               0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]  # 100%

random.seed(42)

# Sample the same number of customers as rows in your existing dataset
existing_rows = len(df2)
sampled_age = random.choices(age_distribution, weights=age_distribution_percentage, k=existing_rows)

# Assign the sampled age to your existing DataFrame
df2['Age'] = sampled_age

# Save the DataFrame to a CSV file
df2.to_csv('datasets/OrderReport.csv', index=False)

print(df2.head())
print(df2['Age'].value_counts())

# transfer the gender column from OrderReport_withGender.csv to OrderReport.csv
df3 = pd.read_csv('OrderReport_withGender.csv')


