# Import OneHotEncoder
from matplotlib import colors
from sklearn.preprocessing import OneHotEncoder
# Import LabelEncoder
from sklearn.preprocessing import LabelEncoder

# Create text dataset_1
cities = [["Mumbai"],["Pune"],["Delhi"],["Mumbai"],["Pune"]]

# Create OneHotEncoder object
encoder = OneHotEncoder(sparse_output=False)

# Learn categories and convert them into numerical columns
encoded_cities = encoder.fit_transform(cities)

# Display original data
print("Original Cities:", cities)

# Display encoded data
print("Encoded Cities:", encoded_cities)

# Display column names
print("Categories:", encoder.get_feature_names_out(["City"]))

# Create text dataset_2
colors = ["Red", "Black", "Navy-Blue", "White", "Pine-green"]

# Create LabelEncoder object
encoder = LabelEncoder()

# Convert text categories into numbers
colors_encoded = encoder.fit_transform(colors)

# Display original data
print("Original Colors:", colors)

# Display encoded data
print("Encoded Colors:", colors_encoded)

# Display category-to-number mapping
print("Categories:", encoder.classes_)

