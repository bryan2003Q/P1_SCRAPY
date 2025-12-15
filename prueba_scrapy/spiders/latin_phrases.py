import scrapy
import pandas as pd

class LatinPhrasesSpider(scrapy.Spider):
    name = "latin_phrases"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Latin_phrases_(full)"]

    def parse(self, response):
        tables=response.css("table.wikitable")
        
        dfs=[]
        
        
        for table in tables:
            df=pd.read_html(table.get())[0]
            dfs.append(df)
            
            
        tabla_unificada=pd.concat(dfs, ignore_index=True)
        
        tabla_unificada.to_excel("latin_frases.xlsx", index=False)
        
        self.log("Excel generado correctamente")
            
