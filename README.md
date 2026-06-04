# 🏋️‍♂️ Gym Experience Predictor API

Une API de Machine Learning développée avec FastAPI qui prédit le niveau d'expérience d'un membre de salle de sport (de 1 à 3) en fonction de ses métriques physiques et de sa routine d'entraînement.

Ce projet implémente un modèle `RandomForestClassifier` optimisé (via `GridSearchCV`) et traqué avec `MLflow`, le tout servi par une architecture orientée service et conteneurisé avec Docker.

---

## ✨ Fonctionnalités clés

* **Prédiction ML** : Modèle Random Forest entraîné sur les données physiologiques et d'entraînement.
* **Indicateurs de confiance** : L'API renvoie désormais la probabilité (certitude) de la prédiction ainsi que la précision (*accuracy*) globale du modèle.
* **Architecture Propre** : Séparation stricte entre les contrôleurs (routes HTTP) et la logique métier (services).
* **Validation des données** : Utilisation de Pydantic pour sécuriser et typer les requêtes entrantes.
* **Conteneurisation Docker** : Environnement isolé garantissant un fonctionnement identique sur n'importe quelle machine ou serveur Cloud (ex : Render).

---

## 🏗️ Architecture du Projet

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
│   ├── model.pkl       # Modèle ML sérialisé (Random Forest)
│   └── encoder.pkl     # Encodeur pour la variable cible (Experience_Level)
├── notebook/
│   └── train.ipynb     # Notebook Jupyter (EDA, Entraînement, MLflow)
├── .dockerignore       # Fichiers ignorés lors de la construction Docker
├── Dockerfile          # Recette pour construire le conteneur de l'API
├── requirements.txt
└── README.md
```

---

## 🐳 Lancement Rapide (via Docker) — Recommandé

La façon la plus simple et la plus fiable de lancer l'API en évitant les problèmes de dépendances Python locales.

### Construire l'image Docker

```bash
docker build -t gym-api .
```

### Lancer le conteneur

```bash
docker run -p 8000:8000 gym-api
```

L'API est maintenant accessible à l'adresse :

```text
http://localhost:8000/docs
```

---

## 💻 Installation et Lancement (Local / Développement)

Si vous souhaitez modifier le code ou réentraîner le modèle localement.

### 1. Prérequis

* Python 3.11 ou supérieur
* Git

### 2. Cloner le dépôt et préparer l'environnement

```bash
git clone https://github.com/VOTRE_USERNAME/gym-api.git
cd gym-api

# Créer et activer l'environnement virtuel
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

# Installer les dépendances
pip install matplotlib --prefer-binary
pip install -r requirements.txt
```

### 3. Générer les modèles d'Intelligence Artificielle

Avant de lancer l'API pour la première fois, il faut entraîner le modèle.

1. Ouvrez le fichier `notebook/train.ipynb`.
2. Exécutez toutes les cellules pour :

   * réaliser l'analyse exploratoire des données (EDA),
   * entraîner le modèle Random Forest,
   * suivre les expérimentations avec MLflow,
   * générer les fichiers `model.pkl` et `encoder.pkl` dans le dossier `models/`.

### 4. Lancer le serveur local

```bash
uvicorn app.main:app --reload --port 8000
```

---

## 🧪 Utilisation de l'API

Accédez à la documentation interactive Swagger UI via votre navigateur pour tester facilement les requêtes :

👉 `http://localhost:8000/docs`

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

## 📤 Exemple de réponse JSON

```json
{
  "experience_level": 2,
  "message": "Le niveau d'expérience estimé est de niveau 2",
  "confidence": 0.85,
  "accuracy": 0.91
}
```

---

## 🛠️ Technologies utilisées

* FastAPI
* Scikit-learn
* RandomForestClassifier
* GridSearchCV
* MLflow
* Pandas
* NumPy
* Pydantic
* Uvicorn
* Docker

---

## 📚 Contexte du projet

Projet réalisé dans le cadre de l'évaluation du module **API & Intelligence Artificielle**.

# 👨‍💻 Auteur

**Ilan**

- Apprenti Concepteur Développeur d'Applications (CDA)
- EPSI Bachelor SIN
- Spécialisation DevOps & Full Stack

### Dernière mise à jour : 04-06-2026
