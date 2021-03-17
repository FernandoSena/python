palavras = []
while True:
    palavra = input("Digite a plavra ou 0 para sair do sistema: ")
    if palavra == "0":
        break
    palavras.append(palavra)
print(set(palavras))