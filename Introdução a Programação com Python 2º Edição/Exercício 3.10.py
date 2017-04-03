"""
Exercício 3.10

Faça um programaque calcule o aumento de um salário. Ele deve solicitar
o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.

"""


salario = int(input("Digite o valor do seu salário: "))
aumento = int(input("Digite o valor porcentual do seu aumento: "))



x = salario * aumento / 100
salarioatu = salario + x

print ("O valor do seu aumento é de", x)
print ("Seu salário agora é de :", salarioatu)
