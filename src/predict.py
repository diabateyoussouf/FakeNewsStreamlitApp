# src/predict.py - Version corrigée
import pickle
import numpy as np
from .preprocess import preprocess_text

# Charger une fois
_vectorizer = None
_model = None

def load_model():
    """Charge les modèles"""
    global _vectorizer, _model
    try:
        _vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
        _model = pickle.load(open("models/svm_model.pkl", "rb"))
        return _vectorizer, _model
    except Exception as e:
        print(f"❌ Erreur chargement: {e}")
        return None, None

def predict_news(text: str):
    """Prédit si c'est REAL ou FAKE"""
    try:
        # Charger modèle si besoin
        if _vectorizer is None:
            load_model()
            if _vectorizer is None:
                return "ERROR", "Modèle non chargé", 0.5
        
        # Nettoyer texte
        cleaned = preprocess_text(text)
        if not cleaned or len(cleaned.split()) < 3:
            return "UNKNOWN", "Texte trop court", 0.5
        
        # Prédire
        X = _vectorizer.transform([cleaned])
        prediction = _model.predict(X)[0]
        
        # Convertir 0/1 en FAKE/REAL
        if prediction == 0:
            label = "FAKE"
        elif prediction == 1:
            label = "REAL"
        else:
            label = str(prediction)
        
        # Confiance
        try:
            proba = _model.predict_proba(X)[0]
            conf = max(proba)
        except:
            conf = 0.85 if label == "REAL" else 0.75
        
        return label, cleaned[:100], conf
    
    except Exception as e:
        print(f"❌ Erreur prédiction: {e}")
        return "ERROR", str(e), 0.5