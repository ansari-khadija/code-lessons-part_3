
# ==========================================
# CATBOOST - COMPLETE 80/20 GUIDE
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from catboost import CatBoostClassifier, CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ==========================================
# 1. CREATE SAMPLE DATA
# ==========================================

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "salary": [20000, 25000, 30000, 35000, 40000,
               45000, 50000, 55000, 60000, 65000],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai",
             "Pune", "Delhi", "Mumbai", "Pune", "Delhi"],
    "purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
})

X = df.drop("purchased", axis=1)
y = df["purchased"]

# Categorical column names
cat_features = ["city"]

# ==========================================
# 2. SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# ==========================================
# 3. CREATE CLASSIFIER
# ==========================================

model = CatBoostClassifier(
    iterations=200,
    learning_rate=0.05,
    depth=4,
    loss_function="Logloss",
    verbose=False,
    random_seed=42
)

# ==========================================
# 4. TRAIN MODEL
# ==========================================

model.fit(
    X_train,
    y_train,
    cat_features=cat_features,
    eval_set=(X_test, y_test),
    early_stopping_rounds=30,
    verbose=False
)

# ==========================================
# 5. PREDICTIONS
# ==========================================

predictions = model.predict(X_test)

# Prediction probabilities
probabilities = model.predict_proba(X_test)

print("Predictions:", predictions)
print("Probabilities:", probabilities)

# ==========================================
# 6. MODEL EVALUATION
# ==========================================

print("Accuracy:", accuracy_score(y_test, predictions))

print(classification_report(y_test, predictions))

# ==========================================
# 7. FEATURE IMPORTANCE
# ==========================================

importance = model.feature_importances_

print("Feature Importance:", importance)

# Get feature importance
importance = model.get_feature_importance()

# Plot feature importance
plt.bar(X.columns, importance)

plt.title("CatBoost Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.show()

# ==========================================
# 8. SAVE AND LOAD MODEL
# ==========================================

model.save_model("catboost_model.cbm")

new_model = CatBoostClassifier()

new_model.load_model("catboost_model.cbm")

print("Model loaded successfully!")

# ==========================================
# 9. NEW PREDICTION
# ==========================================

new_customer = pd.DataFrame({
    "age": [32],
    "salary": [38000],
    "city": ["Mumbai"]
})

result = new_model.predict(new_customer)

print("New Customer Prediction:", result)


# ==========================================
# 10. REGRESSION EXAMPLE
# ==========================================

# Predict salary using age and city

X_reg = df[["age", "city"]]
y_reg = df["salary"]

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_reg, y_reg,
    test_size=0.3,
    random_state=42
)

reg_model = CatBoostRegressor(
    iterations=100,
    learning_rate=0.05,
    depth=4,
    verbose=False
)

reg_model.fit(
    Xr_train,
    yr_train,
    cat_features=["city"]
)

reg_predictions = reg_model.predict(Xr_test)

print("Salary Predictions:", reg_predictions)

print("\nCATBOOST COMPLETED!")
