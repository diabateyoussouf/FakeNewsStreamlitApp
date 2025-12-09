import os
import json
import streamlit as st
from .predict import predict_news


class FakeNewsAgent:
    def __init__(self):
        self.api_key = self._get_api_key()
    
    def _get_api_key(self):
        api_key = None
        try:
            api_key = st.secrets.get("MISTRAL_API_KEY")
        except:
            pass

        if not api_key:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("MISTRAL_API_KEY")

        return api_key


    # --------------------------------------------------------
    # TOOL: appelé automatiquement par le LLM
    # --------------------------------------------------------
    def _tool_predict_news(self, text: str):
        label, cleaned, conf = predict_news(text)
        return {
            "label": label,
            "confidence": conf,
            "cleaned": cleaned
        }


    # --------------------------------------------------------
    # AGENT PRINCIPAL
    # --------------------------------------------------------
    def _ask_mistral(self, user_message: str) -> str:
        """L'agent utilise un tool si et seulement si le LLM le décide."""
        if not self.api_key:
            return "❌ API Key manquante"

        from mistralai import Mistral
        client = Mistral(api_key=self.api_key)

        # Prompt intelligent : LLM décide ENTRE discuter / répondre / analyser
        system_prompt = """
Tu es un assistant intelligent et autonome de détection de fake news.

🎯 RÈGLES FONDAMENTALES :
- Si le message est une QUESTION → répondre normalement.
- Si le message est une DISCUSSION → discuter naturellement.
- Si le message contient une INFORMATION ou un TEXTE journalistique → tu DOIS appeler l’outil `predict_news`.
- Tu n’inventes PAS la classification : seul le tool a raison.
- Après avoir reçu la réponse du tool, tu génères la réponse finale au format :

🎯 RÉSULTAT : REAL / FAKE / UNKNOWN (Confiance : XX%)
📝 Explication : courte (2–3 lignes), basée sur le modèle + ton analyse du style
🔍 Vérification recommandée : 1–2 conseils sans liens marketing

Tu décides SEUL si un tool doit être appelé.
"""

        # Déclaration du tool
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "predict_news",
                    "description": "Analyse un texte et renvoie REAL ou FAKE.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"}
                        },
                        "required": ["text"]
                    }
                }
            }
        ]

        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            tools=tools,
            max_tokens=300,
            temperature=0.3
        )

        msg = response.choices[0].message

        
        if msg.tool_calls:
            full_messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
                msg
            ]

            for call in msg.tool_calls:
                if call.function.name == "predict_news":
                    args = json.loads(call.function.arguments)
                    result = self._tool_predict_news(args["text"])

                    # On renvoie le résultat du tool au LLM
                    full_messages.append({
                        "role": "tool",
                        "tool_call_id": call.id,
                        "name": "predict_news",
                        "content": json.dumps(result)
                    })

                    # Deuxième appel : génération du message final
                    final = client.chat.complete(
                        model="mistral-small-latest",
                        messages=full_messages,
                        max_tokens=300,
                        temperature=0.3
                    )

                    return final.choices[0].message.content.strip()

    
        return msg.content.strip()


    def chat(self, message: str) -> str:
        return self._ask_mistral(message)


def get_agent():
    return FakeNewsAgent()
