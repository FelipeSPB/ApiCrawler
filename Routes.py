from Server import App, cache
from flask import jsonify,request
from Services import ColetarStrings, ContandoPalavra
from Models import Resposta, Palavra


@App.route("/busca/", methods=["GET"])
@cache.cached(timeout=50)
def CrawlPalavra():
    Resposta.Resposta["Status"] = "Sucesso"
    Resposta.Resposta["Palavra"] = Palavra.Palavra
    Resposta.Resposta["Dados"] = ContandoPalavra.Retorno()
    return jsonify(Resposta.Resposta) 

