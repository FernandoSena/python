n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
r = float(input(f"Informe o o resultado da operação {n1}+{n2}: "))
acertos = 0
erros = 0
if (n1+n2)==r:
    print("Você acertou!!!")
    acertos += 1
else:
    print("Você errou!!!")
    erros += 1

r = float(input(f"Informe o o resultado da operação {n1}-{n2}: "))
if (n1 - n2) == r:
    print("Você acertou!!!")
    acertos += 1
else:
    print("Você errou!!!")
    erros += 1

r = float(input(f"Informe o o resultado da operação {n1}*{n2}: "))
if (n1 * n2) == r:
    print("Você acertou!!!")
    acertos += 1
else:
    print("Você errou!!!")
    erros += 1

r = float(input(f"Informe o o resultado da operação {n1}/{n2}: "))
if (n1 / n2) == r:
    print("Você acertou!!!")
    acertos += 1
else:
    print("Você errou!!!")
    erros += 1