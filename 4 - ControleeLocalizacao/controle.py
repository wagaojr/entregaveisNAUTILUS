# -*- coding: utf-8 -*-
#PID Kp*(erro) + Kd*(erro_derivativo) + Ki*(erro_integral)
#erro derivativo = erro - erro_passado
#erro integral = erro + soma_dos_erros_passados
#Constantes PID --> Kp = 3 ; Ki = 1 ; Kd = 0.1 || Outputs: saída do PID para erro = 30, após 10 loops

erro = 30
errointegral = 0
erroderivativo = 0
pid = 0
pid2 = 0
somadoserrospassados = 0

for i in range(10): 
   pid += 3*erro + 1*errointegral + 0.1*erroderivativo
   erropassado = erro
   erroderivativo = erro - erropassado
   somadoserrospassados += erropassado
   errointegral = erro + somadoserrospassados

print(pid)                                                         #Aqui eu achei dois resultados, calculei o pid acumulado ao longo dos 10 loops,
                                                                   # e também o último valor de pid no décimo loop que equivale a 690
for i in range(10): 
   pid2 = 3*erro + 1*errointegral + 0.1*erroderivativo
   erropassado = erro
   erroderivativo = erro - erropassado
   somadoserrospassados += erropassado
   errointegral = erro + somadoserrospassados

print(pid2)