#Campeonato Brasileiro de LOL 

class Times:
  def __init__(self,nomedotime, pontuacao):
    self.nomedotime = nomedotime
    self.pontuacao = pontuacao
  def placar(self):
    print("O Time da " + self.nomedotime + " está com o placar de " + str(self.pontuacao) + " pontos")
  def __add__(self, time2):
    r = self.pontuacao + time2.pontuacao
    return r
  def __sub__(self, time2):
    h = self.pontuacao - time2.pontuacao
    return h 
  def __gt__(self, time2):
    return (self.pontuacao > time2.pontuacao)
  def __It__(self, time2):
    return (self.pontuacao < time2.pontuacao)  
  def __eq__(self, time2):
    return (self.pontuacao == time2.pontuacao)  
  def __ne__(self, time2):
    return (self.pontuacao != time2.pontuacao)      
  def __repr__(self):
    n = "{}".format(self.nomedotime)
    return n 


class Participante:
  def __init__(self, time, nome, abates, mortes):
     self.time = time
     self.nome = nome
     self.abates = abates
     self.mortes = mortes
  def __repr__(self):
    j = "O jogador {} do time {} está com {} abates e {} mortes".format(self.nome,self.time,self.abates,self.mortes)
    return j 
  def __add__(self, participante2):
    p = self.abates + participante2.abates
    return p
  def __sub__(self, participante2):
    o = self.abates - participante2.abates
    return o  
  def __gt__(self, participante2):
    return (self.abates > participante2.abates)
  def __It__(self, participante2):
    return (self.abates < participante2.abates)
  def __eq__(self, participante2):
    return (self.abates == participante2.abates)  
  def __ne__(self, participante2):
    return (self.abates != participante2.abates)        



time1 = Times("PainGaming", 2)
participante1 = Participante("PainGaming", "Tinowns", 10, 2)
participante2 = Participante("PainGaming", "brTT", 5, 5)


time1.placar()
print(participante1)
print(participante2)
print("\n")

time2 = Times("Furia", 1)
participante3 = Participante("Furia", "Envy", 7, 3)
participante4 = Participante("Furia", "Ranger", 10, 5)

#lembrando que acho até que eles já mudaram de times, mas como não estou acompanhando vai assim mesmo kk

time2.placar()
print(participante3)
print(participante4)
print("\n")

print(time1 + time2)
print(time1 - time2)
print(time1 > time2)
print(time1 < time2)         # comparações pelo numero de pontos dos times
print(time1 == time2)
print(time1 != time2)

lista1 = [time1, time2]
lista1.sort()

print(lista1)                # lista ordenada pelo numero de pontos


print(participante2 + participante3)

lista2 = [participante1, participante2, participante3, participante4]  # lista ordenada pelo numero de abates de cada jogador
lista2.sort()

print(lista2)