import joblib
import pandas as pd
from pathlib import Path
from app.schemas import GymMemberInput, PredictionOutput

MODELS_DIR = Path(__file__).parent.parent / 'models'

class PredictionService:
    def __init__(self):
        self.model = joblib.load(MODELS_DIR / 'model.pkl')
        self.encoder = joblib.load(MODELS_DIR / 'encoder.pkl')
        
        self.model_accuracy = 0.91 
        
        print("Modèle et encodeur chargés avec succès.")

    def predict(self, data: GymMemberInput) -> PredictionOutput:
        input_data = data.model_dump()
        
        gender_male = True if input_data['Gender'] == 'Male' else False
        
        workout = input_data['Workout_Type']
        is_hiit = True if workout == 'HIIT' else False
        is_strength = True if workout == 'Strength' else False
        is_yoga = True if workout == 'Yoga' else False
        
        df = pd.DataFrame([{
            'Age': input_data['Age'],
            'Weight (kg)': input_data['Weight_kg'],
            'Height (m)': input_data['Height_m'],
            'Max_BPM': input_data['Max_BPM'],
            'Avg_BPM': input_data['Avg_BPM'],
            'Resting_BPM': input_data['Resting_BPM'],
            'Session_Duration (hours)': input_data['Session_Duration_hours'],
            'Calories_Burned': input_data['Calories_Burned'],
            'Fat_Percentage': input_data['Fat_Percentage'],
            'Water_Intake (liters)': input_data['Water_Intake_liters'],
            'Workout_Frequency (days/week)': input_data['Workout_Frequency_days_week'],
            'BMI': input_data['BMI'],
            'Gender_Male': gender_male,
            'Workout_Type_HIIT': is_hiit,
            'Workout_Type_Strength': is_strength,
            'Workout_Type_Yoga': is_yoga
        }])

        pred_encoded = self.model.predict(df)[0]
        probabilities = self.model.predict_proba(df)[0]
        
        confidence = max(probabilities)
        
        real_prediction = int(self.encoder.inverse_transform([pred_encoded])[0])

        return PredictionOutput(
            experience_level=real_prediction,
            message=f"Le niveau d'expérience estimé est de niveau {real_prediction}",
            confidence=round(confidence, 2),
            accuracy=self.model_accuracy
        )