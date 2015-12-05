'''
Created on 5 de dez de 2015

@author: gilvonaldo
'''
NOME = input("")

SALARIO_FIXO = float(input())

TOTAL_VENDAS_MES = float(input())

TOTAL_RECEBER = SALARIO_FIXO + (TOTAL_VENDAS_MES * 0.15)

print ("TOTAL = R$ %.2f"%TOTAL_RECEBER)