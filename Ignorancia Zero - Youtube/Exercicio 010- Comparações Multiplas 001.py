idade = int(input("Digite sua idade: "))

"""
if idade >= 18:
    if idade < 70 :
        print ("Você pode receber o beneficio")
    else:
       print ("Você não esta encaixado dentro da idade correta para receber o beneficio")
else:
    print ("Você não esta encaixado dentro da idade correta para receber o beneficio")
"""

# Usando comparações Multiplas:

if 18 <= idade < 70:
    print ("Você pode receber beneficio")
else:
    print ("Você não pode receber beneficio")
    
    
