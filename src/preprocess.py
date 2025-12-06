import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')



def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'\(Reuters\)\s*-?\s*', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s\']', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    words = word_tokenize(text)
    filtered = [stemmer.stem(w) for w in words if w not in stop_words and len(w)>2]
    return ' '.join(filtered)

def preprocess_dataframe(df):
    df_clean = df.copy()
    df_clean['text_clean'] = df_clean['text'].apply(clean_text)
    df_clean['text_clean'] = df_clean['text_clean'].apply(remove_stopwords)
    df_clean = df_clean[df_clean['text_clean'].str.len() > 100]
    print(f"Dataset après nettoyage : {df_clean.shape}")
    return df_clean

def preprocess_text(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    return text
