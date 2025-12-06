import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

st.title("ℹ️ À propos du projet")

st.write("""
## 🧠 Fake News AI
Projet universitaire utilisant NLP + Machine Learning  
pour détecter automatiquement les fausses informations.

### 🔧 Architecture du Modèle
- Nettoyage du texte (Regex + NLP)
- Tokenisation
- Suppression des stopwords
- Stemming (Porter)
- TF-IDF Vectorizer (1–3-grams)
- Modèle : **SVM linéaire calibré**
""")

st.image("assets/model_diagram.png")
