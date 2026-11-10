
# Import StandardScaler
from sklearn.preprocessing import StandardScaler

# Student dataset
# First column = Study hours
# Second column = Attendance
X = [
    [5, 80],
    [6, 90],
    [8, 95],
    [4, 70]
]

# Create StandardScaler object
scaler = StandardScaler()

# Learn the data statistics and transform the data
X_scaled = scaler.fit_transform(X)

# Display original data
print("Original Data:")
print(X)

# Display scaled data
print("Scaled Data:")
print(X_scaled)
