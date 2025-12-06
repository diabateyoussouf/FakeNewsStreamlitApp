# utils/ui.py
import streamlit as st

def display_header():
    """Affiche l'en-tête et les suggestions"""
    st.markdown("""
    <div class="main-title">Chat with UMI-FakeNews</div>
    <div class="main-subtitle">Online • AI Fake News Detection Assistant</div>
    """, unsafe_allow_html=True)
    
    # Suggestions simplifiées
    st.markdown("""
    <div class="suggestions-container">
        <div class="suggestions">
            <button onclick="document.querySelector('textarea').value='Analyse cette news: Trump mort dans un accident'">🔍 Analyse Exemple</button>
            <button onclick="document.querySelector('textarea').value='Donne des conseils'">💡 Conseils</button>
            <button onclick="document.querySelector('textarea').value='Montre un exemple'">📰 Exemple</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_chat():
    """Affiche les messages du chat"""
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="msg-user-container">
                <div class="user-content">
                    <div class="user-name">{msg.get('name', 'User')}</div>
                    <div class="user-message">{msg['content']}</div>
                </div>
                <div class="user-avatar">U</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="msg-bot-container">
                <div class="bot-avatar">F</div>
                <div class="bot-content">
                    <div class="bot-name">
                        {msg.get('name', 'FakeNewsBot')}
                        <span class="online-status">• Online</span>
                    </div>
                    <div class="bot-message">{msg['content']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def display_input():
    """Affiche la zone de saisie"""
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    st.markdown("<div class='input-inner'>", unsafe_allow_html=True)
    
    user_input = st.text_area(
        "", 
        placeholder="Tapez un message ou collez une news...",
        height=100,
        key="input_area",
        label_visibility="collapsed",
        max_chars=5000
    )
    
    col1, col2 = st.columns([5, 1])
    with col1:
        send = st.button("**Envoyer**", use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if send:
        return user_input
    return None

def display_sidebar():
    """Affiche la sidebar"""
    with st.sidebar:
        st.markdown("## 📊 **Statistiques**")
        user_msgs = sum(1 for msg in st.session_state.messages if msg["role"] == "user")
        st.metric("Messages", user_msgs)
        
        st.divider()
        
        if st.button("🗑️ Effacer Chat", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": "Chat effacé ! Comment puis-je vous aider ?", "name": "FakeNewsBot"}
            ]
            st.rerun()
        
        st.divider()
        st.markdown("**Version :** Mistral AI + SVM")