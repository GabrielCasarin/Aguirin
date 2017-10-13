# Esse arquivo gera o no com a caracteristica que vc quer


# Imports
import pandas as pd
import math


def nodes_gen(inputs, topo, outputs):
    """
    Nessa funcao inputs eh o numero de inputs que eu quero
    topo tem o formato [n,m,k, ... , z] com a topologia da rede
    outputs eh a quantidade de saidas que temos
    
    Aqui eu pego essas informacoes e monto a topologia, para depois
    serem definidos os pesos.
    """
    
    input_list = {}
    for i in range(1, inputs):
        # Gero tambem uma lista com os nomes das entradas
        inputs_list.append('input_%s' %i)
        
        
        
    for layer in range(len(topo)):
        # Gero cada camada da topologia
        layer_nodes = topo[layer]
        for node in range(layer_nodes):
        
    
   
