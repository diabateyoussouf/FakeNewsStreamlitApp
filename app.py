# app.py - Fichier principal avec logo
import streamlit as st
from utils.css import load_css
from utils.session import initialize_session
from utils.ui import display_header, display_chat, display_input, display_sidebar
from utils.process import process_user_input
import os

# Au lieu de dotenv, utilisez les secrets Streamlit
api_key = st.secrets.get("MISTRAL_API_KEY", os.getenv("MISTRAL_API_KEY"))

if not api_key:
    st.warning("⚠️ API key manquante. Configurez MISTRAL_API_KEY dans les secrets.")

# -------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------
st.set_page_config(
    page_title="Fake News Chat",
    page_icon="🧠",
    layout="wide",
)

# Charger le CSS
load_css()

# Initialiser la session
initialize_session()

# -------------------------------------------------------
# LOGO FACULTÉ (En haut à gauche)
# -------------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image("assets/logo.png", width=150)  # Assurez-vous d'avoir ce fichier
    st.markdown("<p style='font-size:12px; color:#666;'>Faculté des Sciences<br>Université Moulay Ismael</p>", 
                unsafe_allow_html=True)

# -------------------------------------------------------
# HEADER ET INTERFACE
# -------------------------------------------------------
display_header()
display_chat()

# -------------------------------------------------------
# INPUT UTILISATEUR
# -------------------------------------------------------
user_input = display_input()

# Traiter l'input si envoyé
if user_input and user_input.strip():
    process_user_input(user_input.strip())

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------
display_sidebar()