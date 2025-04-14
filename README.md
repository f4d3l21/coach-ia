# 🧠 Coach IA – Assistant Personnel avec LLM

Bienvenue sur **Coach IA**, une application développée en Python avec Streamlit, qui utilise un modèle de langage (LLM) pour vous motiver, vous écouter et vous accompagner dans vos projets personnels ou professionnels.

---

## 🚀 Fonctionnalités

- 💬 Interface de chat simple et fluide 
- 🎭 Choix du type de coach : Motivation, Écoute, Conseil, Boost express
- 🤖 Réponses personnalisées générées par un LLM hébergé sur Together.ai (Mistral-7B-Instruct)
- 🔐 Sécurité de la clé API via fichier `.env`

---

## 📦 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/tonutilisateur/coach-ia.git
cd coach-ia
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)
```bash
python -m venv venv
source venv/bin/activate  # sur Mac/Linux
venv\Scripts\activate    # sur Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Crée un fichier `.env` à la racine du projet avec cette ligne :
```env
TOGETHER_API_KEY=sk-votre_cle_api_here
```
> 🔑 Tu peux obtenir une clé gratuitement sur [https://together.ai](https://together.ai)

⚠️ **Ne partage jamais ta vraie clé API**. Le fichier `.env` est ignoré par Git via `.gitignore`.

---

## ▶️ Lancer l’application
```bash
streamlit run app.py
```
Puis ouvre le lien local fourni par Streamlit dans ton navigateur.

---

## 🎥 Démonstration

▶️ VIDEO : https://youtu.be/QSaEX2VIu8w

▶️ SITE HEBERGER : https://coach-ia-fybzrdabeouehvedzmxx7n.streamlit.app



---

## 🧠 Modèle utilisé
- **Modèle** : `mistralai/Mistral-7B-Instruct-v0.2`
- **Fournisseur** : [Together.ai](https://together.ai/)
- **API** : compatible OpenAI (via `openai` SDK)

---

## 📄 Licence
Projet réalisé dans le cadre d’un projet pédagogique. Vous pouvez le réutiliser ou l'améliorer librement.

---

f4d3l21
