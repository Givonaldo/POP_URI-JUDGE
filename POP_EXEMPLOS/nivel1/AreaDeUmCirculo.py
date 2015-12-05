'''
Created on 4 de dez de 2015
    URI Online Judge 
    Área de um Circulo - 1002
    
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando 
que para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de Raio ao quadrado e multiplicando por π.

Entrada

A entrada contém um valor de ponto flutuante (dupla precisão) no caso a variável raio.

Saída

Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, 
com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos 
os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você 
receberá "Presentation Error".

@author: Gilvonaldo
'''

raio = float(input())
area = float(3.14159 * (raio ** 2))

print("A=%.4f"%area)
