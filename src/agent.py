# src/agent.py - Version compatible Streamlit secrets
import os
import streamlit as st
from .predict import predict_news

class FakeNewsAgent:
    def __init__(self):
        # Essayer d'abord les secrets Streamlit, puis .env
        self.api_key = self._get_api_key()
    
    def _get_api_key(self):
        """Récupère l'API key depuis Streamlit secrets ou .env"""
        api_key = None
        
        # 1. Essayer Streamlit secrets
        try:
            api_key = st.secrets.get("MISTRAL_API_KEY")
            if api_key:
                print("✅ API key chargée depuis Streamlit secrets")
        except Exception as e:
            print(f"⚠️ Secrets non disponibles: {e}")
        
        # 2. Si pas dans secrets, essayer .env
        if not api_key:
            try:
                from dotenv import load_dotenv
                load_dotenv()
                api_key = os.getenv("MISTRAL_API_KEY")
                if api_key:
                    print("✅ API key chargée depuis .env")
            except:
                pass
        
        return api_key

    def _ask_mistral(self, prompt: str) -> str:
        """Utilise Mistral pour générer une explication courte."""
        if not self.api_key:
            return ""
        try:
            from mistralai import Mistral
            client = Mistral(api_key=self.api_key)
            response = client.chat.complete(
                model="mistral-small-latest",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=120,
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ Erreur Mistral: {e}")
            return ""

    def _links(self, label: str) -> str:
        """Liens de vérification."""
        base = """
🔍 **Vérification recommandée :**
• AFP Factuel : https://factuel.afp.com/
• Snopes : https://www.snopes.com/
• Les Décodeurs (Le Monde) : https://www.lemonde.fr/les-decodeurs/
• Google Fact Check : https://toolbox.google.com/factcheck/
"""
        if label == "FAKE":
            return base + "\n⚠️ Cette information semble douteuse, vérifiez impérativement la source."
        else:
            return base + "\n✅ Vous pouvez recouper avec d'autres sources fiables."
    
    def chat(self, message: str) -> str:
        msg = message.lower().strip()

        # 1️⃣ Salutations intelligentes
        if any(msg.startswith(s) for s in ["bonjour", "salut", "hello", "bonsoir", "hi", "hey"]):
            return (
                "👋 **Bonjour !** Je suis votre assistant de détection de fake news.\n"
                "Envoyez un texte pour analyse, ou demandez des *conseils*."
            )

        # 2️⃣ Merci → réponse naturelle
        if "merci" in msg or "thanks" in msg:
            return "😊 Avec plaisir ! Voulez-vous analyser un autre texte ?"

        # 3️⃣ Conseils
        if "conseil" in msg or "tips" in msg:
            return (
                "💡 **Conseils pour vérifier une information :**\n"
                "1. Vérifiez la source (site officiel ? journaliste identifié ?)\n"
                "2. Comparez avec plusieurs médias fiables\n"
                "3. Vérifiez la date du contenu\n"
                "4. Méfiez-vous du ton alarmiste ou sensationnel\n\n"
                + self._links("REAL")
            )

        # 4️⃣ Exemple
        if "exemple" in msg:
            example = "Elon Musk offre 1000€ à ceux qui partagent cette publication."
            label, cleaned, conf = predict_news(example)
            return (
                "📰 **EXEMPLE D'ANALYSE**\n\n"
                f"Texte : \"{example}\"\n"
                f"Résultat : {label} ({conf:.0%} confiance)\n\n"
                "Pourquoi c’est suspect :\n"
                "• Promesse irréaliste\n"
                "• Pas de source\n"
                "• Ton sensationnaliste\n\n"
                + self._links("FAKE")
            )

        # 5️⃣ Analyse automatique (texte suffisamment long)
        if len(message.split()) >= 8:
            label, cleaned, conf = predict_news(message)

            emoji = "🚨" if label == "FAKE" else "✅"
            verdict = "FAKE NEWS" if label == "FAKE" else "INFORMATION CRÉDIBLE"

            result = (
                f"🎯 **RÉSULTAT : {verdict} {emoji} (Confiance : {conf:.0%})**\n\n"
                f"📝 **Texte analysé :** {cleaned[:200]}...\n"
            )

            # Explication courte via Mistral
            if self.api_key:
                expl = self._ask_mistral(
                    f"En 2 lignes, explique pourquoi ce texte semble {label.lower()}: {cleaned[:250]}"
                )
                if expl:
                    result += f"\n📝 **Explication :** {expl}\n"

            return result + "\n" + self._links(label)

        # 6️⃣ Cas par défaut (questions génériques)
        return (
            "🤖 **Assistant Fake News**\n"
            "Je peux analyser une news, donner des conseils ou expliquer comment vérifier une information.\n"
            "Envoyez-moi un texte pour commencer !"
        )

def get_agent():
    return FakeNewsAgent()