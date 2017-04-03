AbrirArquivo = open("Teste.txt", "r")

##Para ler a primeira Linha
#LerPrimeiraLinha = AbrirArquivo.readline()
#print(LerPrimeiraLinha)
##Para ler a segunda Linha
#LerSegundaLinha = AbrirArquivo.readline()
#print(LerSegundaLinha)

#Para ler o arquivo todo
LerAquivoTodo = AbrirArquivo.read()
print(LerAquivoTodo)