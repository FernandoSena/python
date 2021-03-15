valor_parcela = float(input("Valor das parcelas: "))
quantidade_parcelas = int(input("A quantidade de parcelas a ser pagas: "))
resultado = valor_parcela * quantidade_parcelas
print(f"O seu produto custa {resultado:,.2f} {quantidade_parcelas} parcelas de {valor_parcela:,.2f}")