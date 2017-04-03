area = int(input("Digite a area em metros quadrados a ser pintada: "))

#Litros de tinta para cada 3 metros

litros = area//3
if area % 3 > 0:
    litros = litros + 1


#Em cada Lata há 18 litros

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

#print ("Litros: ", litros)
#print ("Latas: ", latas)
#print ("Soma de litros por lata: ", latas*18)

print ("Você precisara de", latas, "latas")
print ("Você vai pagar R$", latas*80, )
       
