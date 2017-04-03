"""
Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse
110 km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso,
exiba o valor a multa, cobrando R$ 5,00 por km acima de 110.



"""


vel = int(input("Qual a velocidade do veiculo: "))



if vel > 110:

    multa = vel - 110
    multatot = multa * 5

    
    
    print ("Você foi multado \n")
    print ("O valor da multa é de R$ %d" %multatot)
    
