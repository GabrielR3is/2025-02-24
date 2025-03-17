numero = input("Digite um número inteiro: ")
try:
    numero_int = int(numero)
except ValueError:
    print("")
print(f"o posterior é {numero_int+1}")