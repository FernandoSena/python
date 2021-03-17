produtos = {1: ["Teclado", 300, 166.71],
             2: ["Mouse", 125, 80.57],
             3: ["Processador", 25, 875.64],
             4: ["Cooler", 70, 35.14]}

for codigo in produtos:
    print(codigo, ' - ', produtos[codigo][0], ' - ', produtos[codigo][1], ' - ', produtos[codigo][2])

while True:
    acao = int(input("Digite (1) para acrecentar ao esque (2) para tirar do estoque e (3) para sair: "))
    if acao == 3:
        break
    else:
        codigo = int(input("Informe o código do produto: "))
        if acao == 1:
            qtd = int(input("Informe a quantidade do produto: "))
            produtos[codigo][1] += qtd
        elif acao == 2:
            qtd = int(input("Informe a quantidade do produto de retirada: "))
            if qtd <= produtos[codigo][1]:
                produtos[codigo][1] -= qtd
            else:
                print("Quantidade insuficiente em estoque!")

print(f"Estoque atualizado: ")
print("Codigo - Descrição - Qtd. - Valor unitário")
for codigo in produtos:
    print(codigo, ' - ', produtos[codigo][0], ' - ', produtos[codigo][1], ' - ', produtos[codigo][2])

