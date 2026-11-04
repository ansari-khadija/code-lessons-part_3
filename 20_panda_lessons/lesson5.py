import pandas as pd

print("=== Data Filtering in Pandas (AND, OR, NOT) ===")

# Step 1: Create student data
students = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj'],
    'Age': [22, 25, 21, 24, 23],
    'Marks': [80, 90, 75, 85, 95]
}

# Step 2: Create DataFrame
df = pd.DataFrame(students)

# Step 3: Filter using AND condition
print("\nStudents with Age Greater Than 22 AND Marks Greater Than 80:")
print(df[(df['Age'] > 22) & (df['Marks'] > 80)])

# Step 4: Filter using OR condition
print("\nStudents with Age Less Than 22 OR Marks Less Than 80:")
print(df[(df['Age'] < 22) | (df['Marks'] < 80)])

# Step 5: Filter using NOT condition
print("\nStudents NOT in Age Group 22:")
print(df[~(df['Age'] == 22)])
