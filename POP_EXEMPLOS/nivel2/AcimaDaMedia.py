# -*- coding: UTF-8 -*-

'''
Created on 5 de dez de 2015
    URI Online Judge 
    Acima da Média - 1214

Sabe-se que 90% dos calouros tem sempre a expectativa de serem acima da média no início de 
suas graduações. Você deve checar a realidade para ver se isso procede.

Entrada

A entrada contém muitos casos de teste. A primeira linha da entrada contém um inteiro C, 
indicando o número de casos de teste. Seguem C casos de teste ou instâncias. Cada caso de 
teste inicia com um inteiro N, que é o número de pessoas de uma turma (1 ≤ N ≤ 1000). Seguem 
N inteiros, separados por espaços, cada um indicando a média final (um inteiro entre 0 e 100) 
de cada um dos estudantes desta turma.

Saída

Para cada caso de teste imprima uma linha dando o percentual de estudantes que estão acima da 
média da turma, com o valor arredondado e com 3 casas decimais.


@author: Gilvonaldo
'''
# Número de casos de testes
C = int(input())

N = ""
cont = 0
result = 0
acimaDaMedia = 0
for i in range(C):
    # Número de pessoas de uma turma
    N = input()
    for i in N:
        if N[cont] != ' ': 
            result += int(N[cont])
            #cont+=cont
            cont+=cont
    
            if int([i]) >= 70:
                acimaDaMedia += acimaDaMedia
    
    print(len(N) * acimaDaMedia / 100)





