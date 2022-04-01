# -*- coding: utf-8 -*-
'''
1-
CRIE UMA FUNÇÃO QUE REALIZE TANTO UMA PA  QUANTO UMA PG PARA VALORES INTEIROS
SE A RAZÃO FOR PAR DEVERÁ SER REALIZADA UMA P.A DE TERMO N1 ATÉ UM VALOR X QUE NÃO DEVE SER ULTRAPASSADO
SE O VALOR DA RAZÃO FOR ÍMPAR A FUNÇÃO REALIZARA UMA PG

cada termo tanto da PA quanto da PG devem ser armazenados em uma lista 

exemplo 
n1= 2
nx= 13
razão = 4

output = [2, 6, 10]
'''

def PAePG(a,b):
  
  if a>b:
    c = a//b
    maior = a
    menor = b
  else:
    c = b//a
    maior = b
    menor = a
    
  h = []  
  if c % 2 == 0:
    for i in range(menor, 40, c):     #Entrou como PA e não ultrapassa o numero 40 com uma razão de "c"
      h.append(i)
      
  else:
    for x in range(menor, 10, c):     #X não pode ultrapassar o numero 10, que é a quantidade de vezes que a razão vai ser aplicada
      h.append(x)
      
  print(h)    
  
#Alguns exemplos
PAePG(3,9)   #Razão 3
PAePG(3,30)  #Razão 10
PAePG(3,18)  #Razão 6
PAePG(3,60)  #razão 20 