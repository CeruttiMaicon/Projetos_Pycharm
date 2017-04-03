n = int(input("Digite o valor de n :"))

cont = 0
soma = 0

while cont < n:
    num = int(input("digite um número da sequencia: "))
    if num > 0:
        soma = soma + n
    cont = cont + 1
print ("Resultado", soma)
