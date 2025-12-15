
pip install --upgrade pip
pip install scrapy pandas openpyxl lxml
pip install spacy stanza deep-translator


python -m spacy download en_core_web_sm
python -c "import stanza; stanza.download('la')"


// comandos de scrapy

scrapy startproject prueba_scrapy
cd prueba_scrapy
scrapy genspider latin_phrases en.wikipedia.org

// se crea
prueba_scrapy/prueba_scrapy/spiders/latin_phrases.py

//Ejecutar
scrapy crawl latin_phrases



// ejecutar desde la raiz
python analisis_nlp.py

