"""
Exercício 3.9

Escreva um programa  que leia a quantidade de dias, horas, minutos e
segundos do usuario. Calcule  total em segundos.

"""

x = int(input("Escreva uma quantidade de dias: "))

dias = x
horas = 24 * x
minutos = 60 * horas
segundos =  60 * minutos


print ("São ", dias, "dias, ", horas,  "horas, com ", segundos, "segundos")
