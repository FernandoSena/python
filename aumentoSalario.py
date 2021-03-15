salario = float(input("Salario atual: "))
percentual = float(input("prcentual de almento: "))

salario_atual = salario+(salario*percentual)/100

print(f"O Seu salario atual é de: {salario_atual:,.2f}")