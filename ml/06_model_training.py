import time
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Timer
start = time.time()

# Load Dataset
X_train = joblib.load("../artifacts/X_train.pkl")
X_test = joblib.load("../artifacts/X_test.pkl")

y_train = joblib.load("../artifacts/y_train.pkl")
y_test = joblib.load("../artifacts/y_test.pkl")

# Create Model
model = RandomForestClassifier(
    n_estimators=100, random_state=42
)

# 100 ->creates 100 decision trees
# random_state=42 for same result



# Train Modle
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy : {accuracy:.4f}")

# Save Temporary Model
joblib.dump(model, "../artifacts/career_model.pkl")

print("\nModle saved successfully")


end = time.time()
print(f"\nExecution Time : {end-start:.2f} seconds")

