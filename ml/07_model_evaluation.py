import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

# Load Model
model = joblib.load("../artifacts/career_model.pkl")
career_encoder = joblib.load("../artifacts/career_encoder.pkl")

# Load Test Data
X_test = joblib.load("../artifacts/X_test.pkl")
y_test = joblib.load("../artifacts/y_test.pkl")

# Prediction 
y_pred = model.predict(X_test)

# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy : {accuracy:.4f}")

# Classification Report 
print("\nClassifiaction Report\n")
print(classification_report(y_test, y_pred, target_names=career_encoder.classes_))

# for this method we will get precision, recall and f1 score



# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

fig, ax = plt.subplots(figsize=(8, 6))

disp.plot(ax=ax)

plt.title("Confusion Matrix")

plt.tight_layout()

plt.savefig("../graphs/confusion_matrix.png")

plt.show()

plt.close()


# Feature Importance
feature_names = X_test.columns

importance = model.feature_importances_

plt.figure(figsize=(10, 6))

plt.bar(feature_names, importance)

plt.xticks(rotation=45)
plt.title("Features")
plt.ylabel("Importances")

plt.xlabel("Features")
plt.ylabel("Importance")

plt.tight_layout()

plt.savefig("../graphs/feature_importance.png")

plt.show()
plt.close()