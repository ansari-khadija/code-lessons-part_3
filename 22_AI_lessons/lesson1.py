# Import train_test_split function from Scikit-learn
from sklearn.model_selection import train_test_split

# sklearn → Scikit-learn library
# model_selection → Module containing tools for splitting data
# train_test_split → Function that divides data into training and testing sets


# X = Input data (Features)
# These values represent the input information given to the ML model
x = [[10], [20], [30], [40], [50]]

# y = Output data (Target)
# These are the correct answers corresponding to each input
y = [100, 200, 300, 400, 500]


# Split the dataset into training and testing data
x_train, x_test, y_train, y_test = train_test_split(

    x,                  # Input features
    y,                  # Target/output values

    test_size=0.8,      # 80% data for testing
                        # Remaining 20% data for training

    random_state=38     # Keeps the random split the same
                        # every time we run this code
)


# Display training input data
print("X_Train:", x_train)

# Display testing input data
print("X_Test:", x_test)

# Display actual training output values
print("Y_Train:", y_train)

# Display actual testing output values
print("Y_Test:", y_test)
