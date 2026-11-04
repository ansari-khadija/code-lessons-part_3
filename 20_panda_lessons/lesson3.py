import pandas as pd

# Step 1: Create student data
students = {
    'Name': ['Amit', 'Priya', 'Rahul'],
    'Age': [22, 25, 21],
    'Marks': [80, 90, 75]
}

# Step 2: Create DataFrame
df = pd.DataFrame(students)

# Step 3: Save data into CSV file
df.to_csv("students.csv", index=False)

# Step 4: Read CSV file
df = pd.read_csv("students.csv")

# Step 5: Display data
print(df)