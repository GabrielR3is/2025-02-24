while True:
    texto = input("Digite uma frase com 5 palavras: ")
    frase = texto.split
    quantidade = len(frase)

    if quantidade != 5:
        print("Digite a frase novamente: ")
    else:
        break
