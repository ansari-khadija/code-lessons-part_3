
# ==================================
# XGBOOST - IMPORTANT FUNCTIONS
# ==================================

import xgboost as xgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Create sample dataset
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=1000,
    n_features=10,
    random_state=42
)

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# 3. Create XGBoost classifier
model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42
)

# 4. Train model
model.fit(X_train, y_train)

# 5. Make predictions
predictions = model.predict(X_test)

# 6. Predict probabilities
probabilities = model.predict_proba(X_test)

# 7. Evaluate model
print("Accuracy:", accuracy_score(y_test, predictions))

print(classification_report(y_test, predictions))

# 8. Feature importance
print("Feature Importance:", model.feature_importances_)

# 9. Plot feature importance
xgb.plot_importance(model)
plt.show()

# 10. Save model
model.save_model("xgboost_model.json")

# 11. Load model
new_model = xgb.XGBClassifier()
new_model.load_model("xgboost_model.json")

# 12. New prediction
print(new_model.predict(X_test[:5]))

print("XGBoost completed!")
