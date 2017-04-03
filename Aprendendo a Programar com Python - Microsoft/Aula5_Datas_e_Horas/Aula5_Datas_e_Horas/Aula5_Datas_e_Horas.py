
#apresentacao de DATAS
import datetime

#armazenar o valor em variavel chamada data atual
dataaaa = datetime.datetime.now()
print(dataaaa.minute)

##mostra a data em formato Ano Mes Dia
#print(dataaaa)
##mostra somente o Ano
#print(dataaaa.year)
##mostra somente o Mes
#print(dataaaa.month)
##mostra somente o Dia
#print(dataaaa.day)


# %d = Dia %B = Mes escrito por extenso %Y = Ano escrito por extenso
print(dataaaa.strftime('%d %B, %Y'))
# %d = Dia %b = Mes abreviado %y = Ano abreviado
print(dataaaa.strftime('%d %b %y'))
#%D = Dia e data inteira escrito em formato mes/dia/ano em númerico abreviado
print(dataaaa.strftime('%D'))


#print("Exemplo Didatico")
#print(dataaaa.strftime("Vocé pode comparecer ao evento no dia %d de %B de %Y"))

#userInput = input("Digite a data do seu aniversario (mm/dd/yyyy): ")
#birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
#print(birthday)

#dataaaa = datetime.date.today()

#dias = birthday - dataaaa

#print(dias.days)