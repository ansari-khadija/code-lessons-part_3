import pandas as pd

students = {
    "Name": ["Amit", "Priya", "Rahul","Amit","Priya"],
    "Age": [22, 25, 21,22,25],
    "Marks": [80, 90, 75,80,90]
}

# Step 2: Create DataFrame
df = pd.DataFrame(students)

print("\nOriginal DataFrame:")
print(df)

# Step 3: Find duplicate rows
print("\nCheck Duplicate Rows:")
print(df.duplicated())

# Step 4: Count duplicate rows
print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

# Step 5: Display only duplicate rows
print("\nDuplicate Records:")
print(df[df.duplicated()])

# Step 6: Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Step 7: Remove duplicates and keep last record
df2 = pd.DataFrame(students)

print("\nKeep Last Duplicate Record:")
print(df2.drop_duplicates(keep='last'))

# Step 8: Remove duplicates based on Name only
print("\nRemove Duplicates Based on Name:")
print(df2.drop_duplicates(subset=['Name']))