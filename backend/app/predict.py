import joblib
import pandas as pd
from pathlib import Path


# Artifacts Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"


# Load Model
model = joblib.load(ARTIFACTS_DIR / "career_model.pkl")

# Load Encoders
gender_encoder = joblib.load(ARTIFACTS_DIR / "gender_encoder.pkl")

degree_encoder = joblib.load(ARTIFACTS_DIR / "degree_encoder.pkl")

branch_encoder = joblib.load(ARTIFACTS_DIR / "branch_encoder.pkl")

career_encoder = joblib.load(ARTIFACTS_DIR / "career_encoder.pkl")



# Prediction Function 
def predict_career(data: dict):


    data["Gender"] = data["Gender"].value
    data["Degree"] = data["Degree"].value
    data["Branch"] = data["Branch"].value


    df = pd.DataFrame([data])

    df["Gender"] = gender_encoder.transform(df["Gender"])
    df["Degree"] = degree_encoder.transform(df["Degree"])
    df["Branch"] = branch_encoder.transform(df["Branch"])

    prediction = model.predict(df)
    confidence = model.predict_proba(df).max()

    career = career_encoder.inverse_transform(prediction)[0]

    return {
        "career": career,
        "confidence": round(confidence * 100, 2)
    }

