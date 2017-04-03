"""
Faça um programa que leia três númeors e mostre o maior o menor e o do meio.
"""



num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 >= num2 >= num3:
    print ("O maior é", num1, ", o do meio é", num2, ", e o menor é", num3)

elif num1 >= num3 >= num2:
    print ("O maior é", num1, ", o do meio é", num3, ", e o menor é", num2)

elif num2 >= num1 >= num3:
    print ("O maior é", num2, ", o do meio é", num1, ", e o menor é", num3)

elif num2 >= num3 >= num1:
    print ("O maior é", num2, ", o do meio é", num3, ", e o menor é", num1)

elif num3 >= num1 >= num2:
    print ("O maior é", num3, ", o do meio é", num1, ", e o menor é", num2)

else:
    print ("O maior é", num3, ", o do meio é", num2, ", e o menor é", num1)

# Fim
