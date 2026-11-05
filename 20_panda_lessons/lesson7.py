import pandas as pd
import numpy as np

print("=== Pandas Lesson 10: Missing Values ===")

# Step 1: Create student data
students = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj'],
    'Age': [22, 25, np.nan, 24, 23],
    'Marks': [80, np.nan, 75, 85, np.nan]
}

# Step 2: Create DataFrame
df = pd.DataFrame(students)

print("\nOriginal DataFrame:")
print(df)

# Step 3: Check missing values
print("\nCheck Missing Values:")
print(df.isnull())

# Step 4: Count missing values
print("\nCount Missing Values:")
print(df.isnull().sum())

# Step 5: Check non-missing values
print("\nNon-Missing Values:")
print(df.notnull())

# Step 6: Remove rows containing missing values
print("\nAfter Removing Missing Rows:")
print(df.dropna())

# Step 7: Fill missing values with zero
print("\nFill Missing Values with Zero:")
print(df.fillna(0))

# Step 8: Fill Age with average Age
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nFill Missing Age with Average:")
print(df)

# Step 9: Fill Marks with average Marks
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print("\nFill Missing Marks with Average:")
print(df)