numero = int(input("Informe um número para você treinar a tabuada: "))
acertos = 0
erros = 0
for x in range(11):
    r = int(input(f'Quando é {numero} X {x}: '))
    resultado = numero*x
    if r == resultado:
        print("Correto!!!")
        acertos += 1
    else:
        print("Que pena você errou, o valor corretor é ", resultado)
        erros += 1

print(f"Você teve {acertos} de acertos e {erros} de erros")