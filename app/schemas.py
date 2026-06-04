from pydantic import BaseModel, Field

class GymMemberInput(BaseModel):
    Age: int = Field(..., gt=0, example=25)
    Gender: str = Field(..., example="Male")
    Weight_kg: float = Field(..., gt=0, example=75.5)
    Height_m: float = Field(..., gt=0, example=1.80)
    Max_BPM: int = Field(..., gt=0, example=190)
    Avg_BPM: int = Field(..., gt=0, example=150)
    Resting_BPM: int = Field(..., gt=0, example=60)
    Session_Duration_hours: float = Field(..., gt=0, example=1.5)
    Calories_Burned: float = Field(..., gt=0, example=600.0)
    Workout_Type: str = Field(..., example="HIIT")
    Fat_Percentage: float = Field(..., gt=0, example=15.5)
    Water_Intake_liters: float = Field(..., gt=0, example=2.5)
    Workout_Frequency_days_week: int = Field(..., gt=0, example=4)
    BMI: float = Field(..., gt=0, example=23.3)

class PredictionOutput(BaseModel):
    experience_level: int
    message: str
    confidence: float
    accuracy: float