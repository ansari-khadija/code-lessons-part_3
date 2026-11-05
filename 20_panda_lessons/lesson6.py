import pandas as pd
print("=== Data Filtering using isin() and between() ===")

# 1. create student data
data = {
    "Name": ["Riya","Priya","Sonam","Sonali","Maya"],
    "Marks": [80,77,67,90,83],
    "Age": [22,23,21,25,24]
    }
# 2. create data frame
df = pd.DataFrame(data)

# Step 3: Filter using isin()
print("\nStudents with Age 21, 23 or 25:")
print(df[df['Age'].isin([21, 23, 25])])

# Step 4: Filter using between()
print("\nStudents with Marks between 80 and 90:")
print(df[df['Marks'].between(80, 90)])

# Step 5: Sort Marks in ascending order
print("\nMarks in Ascending Order:")
print(df.sort_values(by='Marks'))

# Step 6: Sort Marks in descending order
print("\nMarks in Descending Order:")
print(df.sort_values(by='Marks', ascending=False))

# 7. using loc
df.loc[0, 'Marks'] = 88

# 8. using replace
df['Name'] = df['Name'].replace('Rahul', 'Rohan')