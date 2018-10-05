from bs4 import BeautifulSoup
import requests
from Models import Url

def coletar():
    ConteudoSite = []
    for x in Url.Url:
        requerirUrl = requests.get(x)
        soup = BeautifulSoup(requerirUrl.content, "html.parser")
        ColentandoConteudo = str(soup.get_text())
        ConteudoSite.append(ColentandoConteudo)
    return ConteudoSite


     
