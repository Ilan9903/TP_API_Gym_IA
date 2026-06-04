# 🏋️‍♂️ Gym Experience Predictor API

Une API de Machine Learning développée avec FastAPI qui prédit le niveau d'expérience d'un membre de salle de sport (de 1 à 3) en fonction de ses métriques physiques et de sa routine d'entraînement.

Ce projet implémente un modèle `RandomForestClassifier` optimisé (via `GridSearchCV`) et traqué avec `MLflow`, le tout servi par une architecture orientée service.

---

## ✨ Fonctionnalités clés

- **Prédiction ML** : Modèle Random Forest entraîné sur les données physiologiques et d'entraînement.
- **Architecture Propre** : Séparation stricte entre les contrôleurs (routes HTTP) et la logique métier (services).
- **Validation des données** : Utilisation de Pydantic pour sécuriser et typer les requêtes entrantes.
- **Documentation Interactive** : Interface Swagger (OpenAPI) générée automatiquement.

---

## 🏗️ Architecture du Projet

Le dépôt suit une structure modulaire pour faciliter la maintenance et l'évolution du code :

```text
gym-api/
├── app/
│   ├── __init__.py
│   ├── main.py         # Points d'entrée de l'API (Contrôleurs)
│   ├── schemas.py      # Modèles Pydantic (Contrats de données)
│   └── service.py      # Logique métier et prédiction
├── data/
│   └── gym_members_exercise_tracking.csv
├── models/
│   ├── model.pkl       # Modèle ML sérialisé
│   ├── encoder.pkl     # Encodeur pour le model
├── notebook/
│   └── train.ipynb     # Notebook Jupyter (EDA, Entraînement, MLflow)
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Installation et Lancement

### 1. Prérequis

- Python 3.10 ou supérieur
- Git

### 2. Cloner le dépôt

```bash
git clone https://github.com/VOTRE_USERNAME/gym-api.git
cd gym-api
```

### 3. Créer l'environnement virtuel et installer les dépendances

```bash
python3 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### 4. Générer les modèles d'Intelligence Artificielle

Avant de lancer l'API, il faut entraîner le modèle et générer les fichiers `.pkl`.

1. Ouvrez le fichier `notebook/train.ipynb`.
2. Exécutez toutes les cellules pour :
   - réaliser l'analyse exploratoire des données (EDA),
   - entraîner le modèle Random Forest,
   - effectuer le suivi des expérimentations avec MLflow,
   - sauvegarder les artefacts dans le dossier `models/`.

### 5. Lancer le serveur local

```bash
uvicorn app.main:app --reload --port 8000
```

Le flag `--reload` permet de recharger automatiquement le serveur à chaque modification du code.

---

## 🧪 Utilisation de l'API

Une fois le serveur lancé, accédez à la documentation interactive Swagger UI via votre navigateur :

👉 http://localhost:8000/docs

---

## 📡 Endpoints disponibles

### `GET /health`

Vérifie l'état de santé de l'API.

### `POST /predict`

Point d'entrée principal. Reçoit les données d'un utilisateur et retourne la prédiction du niveau d'expérience.

---

## 📥 Exemple de requête (cURL)

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "Age": 25,
    "Gender": "Male",
    "Weight_kg": 75.5,
    "Height_m": 1.80,
    "Max_BPM": 190,
    "Avg_BPM": 150,
    "Resting_BPM": 60,
    "Session_Duration_hours": 1.5,
    "Calories_Burned": 600.0,
    "Workout_Type": "HIIT",
    "Fat_Percentage": 15.5,
    "Water_Intake_liters": 2.5,
    "Workout_Frequency_days_week": 4,
    "BMI": 23.3
  }'
```

---

## 📤 Exemple de réponse

```json
{
  "experience_level": 3,
  "message": "Le niveau d'expérience estimé est de niveau 3",
  "confidence": 0.77,
  "accuracy": 0.91
}
```

---

## 🧠 Technologies utilisées

- FastAPI
- Scikit-learn
- RandomForestClassifier
- GridSearchCV
- MLflow
- MatPlotLib
- Pandas
- NumPy
- Pydantic
- Uvicorn

---

## 📚 Contexte du projet

Projet réalisé dans le cadre de l'évaluation du module **API & Intelligence Artificielle**.

# 👨‍💻 Auteur

**Ilan**

- Apprenti Concepteur Développeur d'Applications (CDA)
- EPSI Bachelor SIN
- Spécialisation DevOps & Full Stack

### Dernière mise à jour : 04-06-2026
