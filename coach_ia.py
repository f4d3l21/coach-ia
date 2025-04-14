import os
from dotenv import load_dotenv
from openai import OpenAI

# Charger la clé depuis un fichier .env
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Initialisation du client Together.ai
client = OpenAI(
    api_key=api_key,
    base_url="https://api.together.xyz/v1"
)

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

def demander_au_coach(prompt_utilisateur):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "Tu es un coach IA bienveillant et motivant."},
                {"role": "user", "content": prompt_utilisateur}
            ],
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Erreur : {e}"

if __name__ == "__main__":
    print("🧠 Coach IA ")
    user_input = input("🗣️ Que veux-tu dire à ton coach IA ?\n> ")
    reponse = demander_au_coach(user_input)
    print("\n🧠 Coach IA :\n" + reponse)
