# -*- coding: utf-8 -*-
'''
4-
A série, 11 + 22 + 33 + ... + 1010 = 10405071317.

Encontre os últimos dez dígitos da série, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

soma = 0
for i in range(1000):
  soma += i**i

lista = list(str(soma))
resposta = []

for i in range(11):
   ultimo = lista[-i]
   resposta.append(ultimo)

del(resposta[0]) 

print(resposta[::-1])