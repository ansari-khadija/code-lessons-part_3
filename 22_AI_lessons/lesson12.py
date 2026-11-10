from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

y_actual = [0, 0, 1, 1, 0, 1, 1, 0]

# Model prediction probabilities
y_probability = [0.1, 0.3, 0.8, 0.9, 0.4, 0.7, 0.6, 0.2]

# Calculate ROC values
fpr, tpr, thresholds = roc_curve(y_actual, y_probability)

print("False Positive Rate:", fpr)
print("True Positive Rate:", tpr)
print("Thresholds:", thresholds)

auc = roc_auc_score(y_actual, y_probability)
print("ROC AUC Score:", auc)