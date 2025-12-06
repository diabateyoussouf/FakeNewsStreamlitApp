# utils/session.py
import streamlit as st

def initialize_session():
    """Initialise les variables de session"""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": "👋 **Bonjour !** Je suis votre assistant de détection de fake news avec Mistral AI.\n\nJe peux :\n🔍 Analyser la crédibilité d'un texte\n💡 Donner des conseils\n📰 Montrer des exemples",
                "name": "FakeNewsBot"
            }
        ]
    
    # Initialiser l'agent
    if "agent" not in st.session_state:
        try:
            from src.agent import get_agent
            st.session_state.agent = get_agent()
            st.session_state.agent_ready = True
        except Exception as e:
            st.error(f"❌ Erreur agent : {e}")
            st.session_state.agent_ready = False