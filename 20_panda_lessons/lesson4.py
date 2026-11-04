import pandas as pd

print("=== Selecting Rows and Columns in Pandas ===")
# Step 1: Create student data
students = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj'],
    'Age': [22, 25, 21, 24, 23],
    'Marks': [80, 90, 75, 85, 95]
}

# Step 2: Create DataFrame
df = pd.DataFrame(students)

# Step 3: Display complete DataFrame
print("Complete DataFrame:")
print(df)

# Step 4: Select a single column
print("\nName Column:")
print(df['Name'])

# Step 5: Select multiple columns
print("\nName and Marks Columns:")
print(df[['Name', 'Marks']])

# Step 6: Select rows using iloc
print("\nFirst Row:")
print(df.iloc[0])

print("\nSecond Row:")
print(df.iloc[1])

print("\nFirst Three Rows:")
print(df.iloc[0:3])

# Step 7: Select rows using loc
print("\nRow with Index 0:")
print(df.loc[0])

print("\nRows from Index 0 to 2:")
print(df.loc[0:2])

# Step 8: Select a particular row and column
print("\nName of First Student:")
print(df.loc[0, 'Name'])

print("\nMarks of Second Student:")
print(df.loc[1, 'Marks'])

print("\nAge of First Student:")
print(df.iloc[0, 1])

# Step 9: Filter data using conditions
print("\nStudents with Marks Greater Than 80:")
print(df[df['Marks'] > 80])

print("\nStudents with Marks Equal to 90:")
print(df[df['Marks'] == 90])

print("\nStudents with Marks Less Than 80:")
print(df[df['Marks'] < 80])

print("\nStudents with Age Greater Than 22:")
print(df[df['Age'] > 22])
