from fastapi import FastAPI, HTTPException
from app.schemas import GymMemberInput, PredictionOutput
from app.service import PredictionService

app = FastAPI(title='Gym Experience API', description='API ML de classification', version='1.0')
svc = PredictionService()

@app.get('/health')
def health():
    return {'status': 'ok', 'model': 'RandomForest Classifier'}

@app.post('/predict', response_model=PredictionOutput)
def predict(member: GymMemberInput):
    """Prédit le niveau d'expérience d'un membre à partir de ses métriques physiques."""
    try:
        return svc.predict(member)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))