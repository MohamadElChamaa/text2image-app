README.md :
Text2Image — Générateur IA avec Stable Diffusion
Objectif:
Cette application permet de générer automatiquement des images à partir d’un texte grâce à des modèles IA open-source (Stable Diffusion).

Fonctionnalités:

Interface web simple (Gradio)
Génération d’images à partir de prompts
Sauvegarde automatique des résultats
Configuration des paramètres (guidance, steps, dimension, nombre d’images)
Déploiement Docker

Architecture
text2image-app
 ├─ app/
 │   ├─ main.py            → UI + logique Gradio
 │   ├─ model_loader.py    → Chargement du modèle IA
 │   ├─ utils.py           → Sauvegarde & gestion fichiers
 │   ├─ static/            → assets éventuels
 ├─ outputs/               → génération images
 ├─ Dockerfile
 ├─ docker-compose.yml
 ├─ requirements.txt
 └─ README.md

Installation Locale
1. Cloner le projet
git clone https://github.com/<repo>/text2image-app.git
cd text2image-app

2. Créer un environnement Python
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# ou
.\.venv\Scripts\activate     # Windows

3. Installer les dépendances
pip install -r requirements.txt

Configuration HuggingFace

Obtenir un token gratuit :

https://huggingface.co/settings/tokens

Créer un token lecture puis l'injecter dans l'environnement :

export HF_TOKEN="TON_TOKEN"

Lancer localement
python app/main.py


Ouvrir le navigateur :
http://localhost:7860/

Exécution avec Docker
Build
docker build -t text2image .

Run
docker run -e HF_TOKEN=$HF_TOKEN -p 7860:7860 text2image