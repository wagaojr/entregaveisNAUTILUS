# -*- coding: utf-8 -*-
'''
2-
Escreva uma função que receba um inteiro como entrada e retorne o número de bits que são iguais a um no binário
representação desse número. Você pode garantir que a entrada não seja negativa.

Exemplo: A representação binária de 1234 é 10011010010, então a função deve retornar 5 neste caso
'''

def qntdeuns(a):
  binario = bin(a)
  lista = list(str(binario))
  del(lista[0])
  del(lista[0])
  print(lista)
  contagem = 0

  for i in lista:
    if ( i.find ( "1" ) != - 1):
      contagem += 1

  print(contagem) 
  
   
qntdeuns(16)