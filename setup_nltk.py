# setup_nltk.py
import nltk
import os
import sys

def setup_nltk_for_streamlit():
    """Setup NLTK data specifically for Streamlit Cloud"""
    print("🔧 Setting up NLTK for Streamlit Cloud...", file=sys.stderr)
    
    # Chemin sur Streamlit Cloud
    nltk_dir = '/home/appuser/nltk_data'
    os.makedirs(nltk_dir, exist_ok=True)
    nltk.data.path.append(nltk_dir)
    
    # Télécharger les packages nécessaires
    packages = ['punkt', 'punkt_tab', 'stopwords']
    
    for pkg in packages:
        try:
            # Vérifier si déjà présent
            if pkg == 'punkt_tab':
                nltk.data.find(f'tokenizers/{pkg}/english')
            else:
                nltk.data.find(f'tokenizers/{pkg}' if 'punkt' in pkg else f'corpora/{pkg}')
            print(f"✅ {pkg} already exists", file=sys.stderr)
        except LookupError:
            print(f"📦 Downloading {pkg}...", file=sys.stderr)
            try:
                nltk.download(pkg, quiet=False, raise_on_error=True)
                print(f"✅ {pkg} downloaded", file=sys.stderr)
            except Exception as e:
                print(f"⚠️ Failed to download {pkg}: {e}", file=sys.stderr)

if __name__ == "__main__":
    setup_nltk_for_streamlit()