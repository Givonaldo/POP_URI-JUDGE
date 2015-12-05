'''
Created on 5 de dez de 2015

@author: gilvonaldo
'''
import string

#Quantidade de casos de testes
n = int(input())

#quantidade de linhas que vem a seguir
l = int(input())

#Lista de letras do alfabeto
a = list(string.ascii_uppercase)
hash = 0
cont = 0

#Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento)

for i in range(l):
    valor = input("")
    for j in a:
        print(a)
        if (string(j) == valor[j]):
            hash = j + cont + i
        cont += cont
        
print (hash)
    
    
    
    
    
    
    