from fastapi import FastAPI, HTTPException

from app.schemas import StudentData
from app.predict import predict_career

from app.database import save_prediction, get_prediction_history, delete_prediction

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Career Compass AI API",
    description="ML-based Career Recommendation System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://career-compass-ai-beta.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


# Delete Prediction
@app.delete("/history/{prediction_id}")
def delete_history(prediction_id: int):

    if delete_prediction(prediction_id):
        return {
            "message": "Deleted Successfully"
        }

    raise HTTPException(
        status_code=404,
        detail="Prediction Not Found"
    )