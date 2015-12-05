'''
Created on 5 de dez de 2015
    URI Online Judge
    Diferença - 1007

Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença 
do produto de A e B pelo produto de C e D segundo a fórmula: 
DIFERENCA = (A * B - C * D).

Entrada

O arquivo de entrada contém 4 valores inteiros.

Saída

Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, 
com um espaço em branco antes e depois da igualdade.

@author: gilvonaldo
'''
A = int(input()) 

B = int(input())
 
C = int(input())

D = int(input()) 

DIFERENCA = (A * B - C * D)

print("DIFERENCA =", DIFERENCA)