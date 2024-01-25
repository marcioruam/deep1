
import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def Stepfuncition(soma):
    if (soma >= 1):
        return 1
    return 0

def calculadaSaida(registro):
    s = registro.dot(pesos)
    return Stepfuncition(s)
    
def treinar():
    
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        
        for i in range(len(saidas)):
            saidaCalculada = calculadaSaida(np.asarray(entradas[i]))
            erro = abs (saidas[i] - saidaCalculada)
            erroTotal += erro
            
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso ataulizado: ' + str(pesos[j]))
            print('Erro Toral: ' + str(erroTotal))
            
treinar()
        
    
        