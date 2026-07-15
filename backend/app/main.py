from fastapi import FastAPI, HTTPException

from app.schemas import StudentData
from app.predict import predict_career

from app.database import save_prediction, get_prediction_history

app = FastAPI(
    title="Career Compass AI API",
    description="ML-based Career Recommendation System",
    version="1.0.0"
)

# Root Endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Career Compass AI API"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model": "ready"
    }


@app.post("/predict")
def predict(student: StudentData):

    try:
        result = predict_career(student.model_dump())

        save_prediction(
            student.model_dump(),
            result["career"],
            result["confidence"]
        )

        return result
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# For histroy
@app.get("/history")
def history():

    return get_prediction_history()