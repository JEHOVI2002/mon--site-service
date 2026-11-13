# Site de Jehovi Ngalibua — version Streamlit

## Fichiers
- `streamlit_app.py` : point d'entrée de l'application Streamlit
- `index.html` : design du site
- `jehovi-portrait.jpg` : photo du profil
- `requirements.txt` : dépendance Python

## Lancement local
Dans un terminal, depuis ce dossier :

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Publication sur Streamlit Community Cloud
1. Dépose les quatre fichiers du projet dans un dépôt GitHub.
2. Ouvre https://share.streamlit.io/
3. Connecte GitHub et sélectionne le dépôt.
4. Choisis `streamlit_app.py` comme fichier principal.
5. Clique sur Deploy.

Le site est actuellement présenté dans un composant HTML intégré à Streamlit. La photo est incorporée automatiquement afin d'éviter les problèmes de chemin d'image.
