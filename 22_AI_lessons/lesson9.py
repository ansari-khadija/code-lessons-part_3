
# Import SimpleImputer
from sklearn.impute import SimpleImputer

# Import NumPy
import numpy as np

# Create dataset with missing values
X = [
    [2, 40],
    [4, 60],
    [np.nan, 70],
    [6, np.nan],
    [8, 90]
]

# Create SimpleImputer object
# strategy="mean" replaces missing values with column averages
imputer = SimpleImputer(strategy="mean")

# Calculate averages and fill missing values
X_filled = imputer.fit_transform(X)

# Display original dataset
print("Original Data:")
print(X)

# Display dataset after filling missing values
print("Updated Data:")
print(X_filled)
