p1 = input("Informe a primeira palavra: ")
p2 = input("Informe a segunda palavra: ")

print(f"Texto 1: {p1}")
print(f"Texto 2: {p2}")

print(f"Quantidade de caracteres de \'{p1}\': {len(p1)}")
print(f"Quantidade de caracteres de \'{p2}\': {len(p2)}")

print("As strings possuem a mesma quantidade de caracteres? ", len(p1)==len(p2))
print("As strings são iguais? ", p1==p2)