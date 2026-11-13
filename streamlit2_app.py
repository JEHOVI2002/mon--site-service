from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="Jehovi Ngalibua | Scientifique des données",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
HTML_PATH = BASE_DIR / "index.html"
PHOTO_PATH = BASE_DIR / "jehovi-portrait.jpg"

# Intègre la photo directement dans le HTML pour qu'elle s'affiche
# correctement dans le composant intégré de Streamlit.
page_html = HTML_PATH.read_text(encoding="utf-8")
photo_b64 = base64.b64encode(PHOTO_PATH.read_bytes()).decode("utf-8")
page_html = page_html.replace(
    'src="jehovi-portrait.jpg"',
    f'src="data:image/jpeg;base64,{photo_b64}"'
)

# Le site est affiché dans toute la largeur de la page.
components.html(page_html, height=3400, scrolling=True)
