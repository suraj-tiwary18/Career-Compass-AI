import time
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


# Timer
start = time.time()

# Load Dataset
df = pd.read_csv("../dataset/processed/career_dataset.csv")

# Remove Student_ID
# df.drop(columns=["Student_ID"], inplace=True)



# Label Encoding
gender_encoder = LabelEncoder()
degree_encoder = LabelEncoder()
branch_encoder = LabelEncoder()
career_encoder = LabelEncoder()


# Encoder Columns
df["Gender"] = gender_encoder.fit_transform(df["Gender"])
df["Degree"] = degree_encoder.fit_transform(df["Degree"])
df["Branch"] = branch_encoder.fit_transform(df["Branch"])
df["Career"] = career_encoder.fit_transform(df["Career"])


# Save Encoders
joblib.dump(gender_encoder, "../artifacts/gender_encoder.pkl")

joblib.dump(degree_encoder, "../artifacts/degree_encoder.pkl")

joblib.dump(branch_encoder, "../artifacts/branch_encoder.pkl")

joblib.dump(career_encoder, "../artifacts/career_encoder.pkl")


# Features and Target
X = df.drop(columns=["Career"])

y = df["Career"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2, stratify=y)
# stratify=y because classes are not prefectly equal

# Prnt Shape
print("\nTraining Data Shape")

print(X_train.shape)

print("\nTesting Data Shape")

print(X_test.shape)


# Save Processed Data
joblib.dump(X_train, "../artifacts/X_train.pkl")
joblib.dump(X_test, "../artifacts/X_test.pkl")

joblib.dump(y_train, "../artifacts/y_train.pkl")
joblib.dump(y_test, "../artifacts/y_test.pkl")


# Execution Time
end = time.time()

print(f"\nExecution Time: {end-start:.2f} seconds")