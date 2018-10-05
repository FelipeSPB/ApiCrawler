from flask import jsonify
from bs4 import BeautifulSoup
import requests
from Services import ColetarStrings
from Models import Url , Resposta
from Models  import Palavra


def Retorno():
    Dados = []
    for x in range(0, len(Url.Url)):
        Link = Url.Url[x]
        ExportarFunc = ColetarStrings.coletar()
        Conteudo = str(ExportarFunc[x])
        qtd = Conteudo.count(Palavra.Palavra)
        Dados.append({"Url": Link , "Quantidade": qtd})
    return Dados
    
    