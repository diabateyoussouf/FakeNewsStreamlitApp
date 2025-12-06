# utils/process.py
import streamlit as st

def process_user_input(user_input):
    """Traite l'input utilisateur"""
    # Ajouter message utilisateur
    st.session_state.messages.append({
        "role": "user", 
        "content": user_input,
        "name": "User"
    })
    
    # Indicateur de frappe
    with st.spinner("Analyse en cours..."):
        # Obtenir réponse
        if st.session_state.agent_ready:
            response = st.session_state.agent.chat(user_input)
        else:
            response = "Agent non disponible. Vérifiez l'installation."
    
    # Ajouter réponse
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response,
        "name": "FakeNewsBot"
    })
    
    st.rerun()