# Refatorar a solução do exercicio anterior de forma que ele qfique mais organizado usando funções.
import os
import time


def obter_opcao():
    os.system("cls")
    print("Cadastro de Produtos")
    print("-" * 20)
    print("1) Cadastrar Produto")
    print("2) Listar Produtos")
    print("3) Sair")
    return int(input("Opção desejada: "))

def validar_dados_produto(nome, preco, estoque) -> bool:
    # nome: ser string e ter pelo menos 2 caracteres
    # preco: ser float e ser maior que zero
    # estoque: ser inteiro e ser maior ou igual a zero
    # if type(x) == int:
    erros = []
    if type(nome) != str:
        erros.append("Nome deve ser um texto.")
    elif len(nome) < 2:
        erros.append("Nome deve ter pelo menos 2 caracteres.")
    if type(preco) != float:
        erros.append("Preço deve ser um valor decimal.")
    elif preco <= 0:
        erros.append("Preço deve ser maior que zero.")
    if type(estoque) != int:
        erros.append("Estoque deve ser um valor inteiro.")
    elif estoque < 0:
        erros.append("Estoque deve ser maior ou igual a zero.")
    if len(erros) > 0:
        for erro in erros:
            print(erro)
        return False
    else:
        return True
        
def cadastrar_produto(produtos: dict):
    codigo, nome, preco, estoque = ler_dados_produtos()
    validar_dados_produto
    produtos[codigo] = (nome, preco, estoque)
    
    print("Produto cadastrado com sucesso!")
    time.sleep(2)

def ler_dados_produtos():
    os.system("cls")
    print("Cadastrar Produto")
    print("-" * 17)
    codigo = int(input("Código: "))
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    return codigo,nome,preco,estoque

def listar_produtos(produtos: dict):
    os.system("cls")
    print("Listar Produtos")
    print("-" * 47)
    print(f" {'Codigo'} {'Produto':15} {'Preço':>10} {'Estoque':>10}")
    print("-" * 47)
    for codigo, (nome, preco, estoque) in produtos.items():
        print(f"{codigo:06d} {nome:15} {preco:>10.2f} {estoque:>10d}")
    print("-" * 47)
    print("Pressione ENTER para voltar ao menu...", end="")
    input()
    print("Voltando ao menu...")
    time.sleep(2)

def sair():
        print("Saindo do sistema...")
        time.sleep(2)
        os.system("cls") 

def main():
    produtos = {}

    while True:
        opcao = obter_opcao()
        match opcao:
            case 1:
                cadastrar_produto(produtos)
            case 2:
                listar_produtos(produtos)
            case 3:
                sair()
                break

            case _:
                print("Opção inválida. Voltando ao menu...")
                time.sleep(2)

if __name__ == "__main__":
    main()