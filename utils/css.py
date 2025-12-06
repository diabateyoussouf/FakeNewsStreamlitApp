import streamlit as st

def load_css():
    """Charge le CSS de l'application"""
    st.markdown("""
    <style>
    body { background-color: #F5F7FA; font-family: 'Segoe UI'; margin: 0; padding: 0; }
    .chat-container { max-width: 800px; margin: 0 auto; padding: 20px; padding-bottom: 180px; }
    .msg-bot-container { display: flex; align-items: flex-start; margin: 20px 0; animation: fadeIn 0.3s ease-in; }
    .bot-avatar { width: 40px; height: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; margin-right: 12px; flex-shrink: 0; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    .bot-content { flex-grow: 1; }
    .bot-name { font-weight: 600; color: #2D3748; margin-bottom: 5px; display: flex; align-items: center; gap: 8px; }
    .online-status { color: #48BB78; font-size: 12px; font-weight: 500; }
    .bot-message { background: white; padding: 20px; border-radius: 18px; border-top-left-radius: 5px; color: #2D3748; line-height: 1.6; box-shadow: 0 2px 10px rgba(0,0,0,0.05); border: 1px solid #E2E8F0; max-width: 600px; animation: slideInLeft 0.3s ease-out; }
    .msg-user-container { display: flex; align-items: flex-start; margin: 20px 0; justify-content: flex-end; animation: fadeIn 0.3s ease-in; }
    .user-avatar { width: 40px; height: 40px; background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; margin-left: 12px; flex-shrink: 0; box-shadow: 0 2px 5px rgba(79, 70, 229, 0.2); }
    .user-content { flex-grow: 1; display: flex; flex-direction: column; align-items: flex-end; }
    .user-name { font-weight: 600; color: #2D3748; margin-bottom: 5px; }
    .user-message { background: #4F46E5; padding: 15px 20px; border-radius: 18px; border-top-right-radius: 5px; color: white; line-height: 1.5; max-width: 600px; box-shadow: 0 2px 10px rgba(79, 70, 229, 0.2); animation: slideInRight 0.3s ease-out; }
    .input-container { position: fixed; bottom: 0; left: 0; right: 0; background: white; padding: 20px; border-top: 1px solid #E2E8F0; box-shadow: 0 -2px 15px rgba(0,0,0,0.08); z-index: 1000; }
    .input-inner { max-width: 800px; margin: 0 auto; display: flex; gap: 12px; align-items: flex-end; }
    .stTextArea textarea { border-radius: 12px !important; border: 2px solid #E2E8F0 !important; padding: 15px !important; flex-grow: 1; font-size: 15px !important; transition: all 0.3s !important; min-height: 60px !important; }
    .stTextArea textarea:focus { border-color: #4F46E5 !important; box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important; }
    .stButton>button { border-radius: 12px; background: #4F46E5; color: white; padding: 12px 28px; border: none; font-size: 15px; font-weight: 500; transition: all 0.3s; height: 60px; min-width: 100px; }
    .stButton>button:hover { background: #4338CA; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3); }
    .main-title { text-align: center; font-size: 32px; font-weight: 800; color: #2D3748; margin-bottom: 10px; background: linear-gradient(90deg, #4F46E5, #7C3AED); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .main-subtitle { text-align: center; font-size: 16px; color: #718096; margin-bottom: 40px; font-weight: 500; }
    .suggestions-container { text-align: center; margin: 30px 0 40px 0; }
    .suggestions-title { font-size: 14px; color: #718096; margin-bottom: 15px; font-weight: 500; }
    .suggestions { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
    .suggestion-btn { background: white; border: 1px solid #E2E8F0; border-radius: 20px; padding: 10px 20px; font-size: 14px; color: #4F46E5; cursor: pointer; transition: all 0.3s; font-weight: 500; }
    .suggestion-btn:hover { background: #4F46E5; color: white; transform: translateY(-2px); box-shadow: 0 4px 10px rgba(79, 70, 229, 0.2); border-color: #4F46E5; }
    </style>
    """, unsafe_allow_html=True)