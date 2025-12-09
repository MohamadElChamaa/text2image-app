README.md :
Text2Image — Générateur IA (Stable Diffusion)
Description
Text2Image est une application permettant de générer des images à partir de texte grâce au modèle IA Stable Diffusion.
Elle fournit une interface utilisateur simple avec Gradio et un backend optimisé basé sur Hugging Face Diffusers.
________________________________________
1. Fonctionnalités
•	Génération d’images haute qualité à partir de prompts
•	Interface web intuitive (Gradio)
•	Paramètres configurables :
o	nombre d’images
o	guidance scale (CFG)
o	steps
o	dimensions
o	seed
o	negative prompts
•	Sauvegarde automatique des images générées
•	Support CPU et GPU
•	Déploiement Docker prêt à l’emploi
________________________________________
2. Architecture du Projet
text2image-app/
 ├─ app/
 │   ├─ main.py
 │   ├─ model_loader.py
 │   ├─ utils.py
 │   ├─ static/
 ├─ outputs/
 ├─ Dockerfile
 ├─ docker-compose.yml
 ├─ requirements.txt
 ├─ README.md
________________________________________
3. Installation Locale
1) Cloner le projet
git clone https://github.com/<your-repo>/text2image-app.git
cd text2image-app
2) Créer un environnement Python
python -m venv .venv
source .venv/bin/activate   # Linux / MacOS
.\.venv\Scripts\activate     # Windows
3) Installer les dépendances
pip install -r requirements.txt
________________________________________
4. Configuration Hugging Face
Obtenez un token gratuit :
👉 https://huggingface.co/settings/tokens
Puis l’injecter dans votre environnement :
export HF_TOKEN="VOTRE_TOKEN"
Vous pouvez changer de modèle :
export HF_MODEL="stabilityai/stable-diffusion-2-1-base"
________________________________________
5. Lancement en local
python app/main.py
Ensuite ouvrez le navigateur :
👉 http://localhost:7860/
________________________________________
6. Exécution avec Docker
🔧 Build
docker build -t text2image .
▶️ Run
docker run -e HF_TOKEN=$HF_TOKEN -p 7860:7860 text2image
________________________________________
7. Déploiement via Docker Compose
docker-compose up --build
Accès :
👉 http://localhost:7860/
________________________________________
8. Licences & Droits
Le projet s'appuie sur :
•	Stable Diffusion (CreativeML Open RAIL-M)
•	Diffusers (Apache 2.0)
•	Gradio (Apache 2.0)
Veuillez respecter les règles d’usage de Stable Diffusion.
________________________________________

