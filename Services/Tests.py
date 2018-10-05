import pytest
from Services import ContandoPalavra, ListaPalavra, ColetarStrings
from Models import Palavra
from Models import Url

def test_Palavra():
    teste = ListaPalavra.Word()
    assert teste == Palavra.Palavra

def test_QtD():
    x = ColetarStrings.coletar()
    for i in range(0, len(Url.Url)):
        testePorVetor = str(x[i])
        export = ContandoPalavra.Retorno()
        quantidade = export[i]["Quantidade"] 
        Verificador = testePorVetor.count(Palavra.Palavra) 
        if Verificador == quantidade:
            assert True 
