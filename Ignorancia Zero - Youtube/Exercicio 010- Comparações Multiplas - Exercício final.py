
saque = int(input("Digite o valor do saque: "))

if 10 <= saque <= 600:

    notas_100 = saque // 100
    saque = saque % 100

    notas_50 = saque // 50
    saque = saque % 50

    notas_10 = saque // 10
    saque = saque % 10

    notas_5 = saque // 5
    saque = saque % 5

    notas_1 = saque // 1

    if notas_100 > 0:
        print (notas_100, "Notas de R$ 100")
    if notas_50 > 0:
        print (notas_50, "notas de R$ 50")
    if notas_10 > 0:
        print (notas_10, "notas de R$ 10")
    if notas_5 > 0:
        print (notas_5, "notas de R$ 5")
    if notas_1 > 0:
        print (notas_1, "notas de R$ 1")

else:
           print("não é possivel fazer o maldito saque")
           
