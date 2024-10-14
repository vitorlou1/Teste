# arquivo: test_imc.py
import pytest
from main import calculo

# Verifica se o valor esta sendo calculado corretamente
def test_calculo_normal():
    imc = calculo(70, 1.75)
    assert imc == pytest.approx(22.86, 0.01)

#Verifica se de fato os erros previstos estão sendo considerados
def test_peso_zero():
    imc = calculo(0, 1.75)
    assert imc == -1

#Verifica se de fato os erros previstos estão sendo considerados
def test_altura_negativa():
    imc = calculo(70, -1.75)
    assert imc == -1
    
#Verifica se de fato os erros previstos estão sendo considerados
def test_altura_invalida():
    imc = calculo(70, 3.6)
    assert imc == -1