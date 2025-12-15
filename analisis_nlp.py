import pandas as pd
import spacy
import stanza
from collections import Counter
from deep_translator import GoogleTranslator


#cargo excel
df=pd.read_excel("prueba_scrapy/latin_frases.xlsx")

#Ingles
nlp_en= spacy.load("en_core_web_sm")


# Stanza latín
stanza.download("la")
nlp_lat = stanza.Pipeline("la")

print(df.head())


# Se unen todas las frases en latín en un solo texto
# dropna(): elimina valores nulos
# astype(str): asegura que todo sea texto
texto_latin = " ".join(df["Latin"].dropna().astype(str))

# Se unen todas las traducciones al inglés en un solo texto
texto_english = " ".join(df["Translation"].dropna().astype(str))


# Se procesa el texto en latín con Stanza
doc_latin = nlp_lat(texto_latin)

# Se procesa el texto en inglés con spaCy
doc_english = nlp_en(texto_english)


# PALABRAS (SUSTANTIVOS Y ADJETIVOS) EN LATÍN
palabras_latin = [
    word.text.lower()           # Se pasa la palabra a minúsculas
    for sent in doc_latin.sentences   # Se recorren las oraciones
    for word in sent.words            # Se recorren las palabras
    if word.text.isalpha()            # Solo palabras (sin números ni símbolos)
    and word.upos in {"NOUN", "ADJ"}  # Solo sustantivos y adjetivos
]

# Se cuentan las frecuencias de las palabras en latín
frecuencia_palabras_latin = Counter(palabras_latin)

# Se muestran las 10 palabras más comunes
frecuencia_palabras_latin.most_common(10)


# VERBOS EN LATÍN
verbos_latin = [
    word.lemma.lower()      # Se usa el lema (forma base del verbo)
    for sent in doc_latin.sentences
    for word in sent.words
    if word.upos == "VERB"  # Solo verbos
]

# Se cuentan las frecuencias de los verbos
frecuencia_verbos_latin = Counter(verbos_latin)

# Se muestran los 10 verbos más comunes
frecuencia_verbos_latin.most_common(10)



# PALABRAS EN INGLÉS
palabras_english = [
    token.text.lower()      # Palabra en minúsculas
    for token in doc_english
    if token.is_alpha       # Solo palabras (sin símbolos)
    and not token.is_stop   # Se eliminan stopwords (the, and, of, etc.)
]

# Se cuentan las palabras en inglés
frecuencia_palabras_english = Counter(palabras_english)

# Top 10 palabras en inglés
frecuencia_palabras_english.most_common(10)


# VERBOS EN INGLÉS
verbos_english = [
    token.lemma_.lower()    # Lema del verbo
    for token in doc_english
    if token.pos_ == "VERB" # Solo verbos
]

# Se cuentan los verbos en inglés
frecuencia_verbos_english = Counter(verbos_english)

# Top 10 verbos en inglés
frecuencia_verbos_english.most_common(10)



# 4. GENERAR FRASES EN ESPAÑOL A PARTIR DE LAS PALABRAS MÁS USADAS
# Se obtienen las 5 palabras más frecuentes en latín
top_palabras_latin = [palabra for palabra, _ in frecuencia_palabras_latin.most_common(5)]

# Se obtienen las 5 palabras más frecuentes en inglés
top_palabras_english = [palabra for palabra, _ in frecuencia_palabras_english.most_common(5)]


# Traducción de palabras latinas al español
print("LATÍN:\n")
for palabra in top_palabras_latin:
    traduccion = GoogleTranslator(source='latin', target='es').translate(palabra)
    print(f"La palabra '{palabra}' significa '{traduccion}' en español.")

# Traducción de palabras inglesas al español
print("\nINGLÉS:\n")
for palabra in top_palabras_english:
    traduccion = GoogleTranslator(source='en', target='es').translate(palabra)
    print(f"La palabra '{palabra}' significa '{traduccion}' en español.")
