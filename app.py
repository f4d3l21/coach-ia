import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Charger la clé API depuis .env
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Init du client Together
client = OpenAI(api_key=api_key, base_url="https://api.together.xyz/v1")
model_name = "mistralai/Mistral-7B-Instruct-v0.2"

# Configuration Streamlit
st.set_page_config(page_title="Coach IA 💬", page_icon="🧠")
st.markdown("""
    <style>
    body {background-color: #F5F5F5;}
    .chat-header {
        display: flex; align-items: center; gap: 10px; margin-bottom: 10px;
    }
    .chat-avatar {
        width: 40px; height: 40px; border-radius: 50%;
    }
    .message-box {
        max-width: 70%; padding: 10px 15px; border-radius: 18px;
        margin-bottom: 10px; font-size: 16px; line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="chat-header">
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" class="chat-avatar">
    <h2 style='margin: 0;'>Coach IA</h2>
</div>
""", unsafe_allow_html=True)

# Mode de coaching
mode = st.selectbox(
    "🎭 Choisis ton type de coaching :",
    ["💪 Motivation", "🧘 Écoute", "🧠 Conseil", "⚡ Boost express"]
)

# Prompts selon le mode
prompts_system = {
    "💪 Motivation": "Tu es un coach motivant. Tu encourages avec énergie et optimisme.",
    "🧘 Écoute": "Tu es un coach empathique. Tu écoutes, tu rassures, tu soutiens avec douceur.",
    "🧠 Conseil": "Tu es un coach pragmatique. Tu analyses calmement et tu donnes des conseils utiles.",
    "⚡ Boost express": "Tu es un coach rapide et impactant. En quelques phrases puissantes, tu réveilles la motivation."
}

# Initialisation de la session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": prompts_system[mode]}
    ]

# Zone d'entrée de texte
user_input = st.text_area("✍️ Ton message :", placeholder="Exprime-toi librement ici...", height=100)
if st.button("📤 Envoyer") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("💭 Le coach réfléchit..."):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=512
            )
            assistant_message = response.choices[0].message.content
        except Exception as e:
            assistant_message = f"❌ Erreur : {e}"
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

# Affichage de l’historique
st.markdown("<hr style='margin-top:30px;'>", unsafe_allow_html=True)
for msg in st.session_state.messages[1:]:  # skip system
    if msg["role"] == "user":
        st.markdown(f"""
            <div style='display:flex; justify-content:flex-end;'>
                <div class='message-box' style='background-color:#007AFF; color:white; border-bottom-right-radius:4px;'>
                    {msg['content']}
                </div>
            </div>
        """, unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"""
            <div style='display:flex; justify-content:flex-start;'>
                <div class='message-box' style='background-color:#E5E5EA; color:black; border-bottom-left-radius:4px;'>
                    {msg['content']}
                </div>
            </div>
        """, unsafe_allow_html=True)
