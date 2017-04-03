print("Helo word")
print("Esta mensagem curta nao pode conter nenhum numero")

#atribuição a 'mensagem'.
mensagem = input("Gigite uma frase curta: ")

print("Sua mensagem em minusculo")
#transforma o texto de 'mensagem' em um texto escrito em minusculo.
print(mensagem.lower())


print("Sua mensagem em MAIUSCULO")
#transforma o texto de 'mensagem' em um texto escrito em MAIUSCULO.
print(mensagem.upper())


print("Invertendo MaIuScUlAs e MiNuScUlAs")
#Ele pega o texto de 'mensagem' e faz com que as letras MAIUSCULAS fiquem minusculas e vice versa.
print(mensagem.swapcase())