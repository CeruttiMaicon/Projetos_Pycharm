print ("EXERÍCIO 009 - ESTRUTURA DE DECISSÕES - 04")
print ("Programa para uma loja de tintas")

area = int(input("Valor em metros quadrados a ser pintado: "))

litros = area//6
if area % 6 > 0:
    litros = litros + 1

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

galões = litros//4
if galões % 4 > 0:
    galões = galões + 1

galões_latas = galões + latas 

print ("Comprando apenas", latas, "latas você gastaria R$", latas*80)
print ("Ou então poderia comprar somente", galões, "galões e gastar", galões*25)
