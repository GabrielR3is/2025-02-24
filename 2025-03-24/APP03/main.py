from produto import Produto
import produto_repo

def main():
    # Criar a tabela
    produto_repo.criar_tabela()
    
    # Inserir 20 produtos fictícios
    produtos_ficticios = [
        Produto(0, f"Produto {i}", 10.0 + i * 2.5, 50 + i) 
        for i in range(1, 21)
    ]
    
    print("Inserindo 20 produtos...")
    for produto in produtos_ficticios:
        id_inserido = produto_repo.inserir(produto)
        print(f"Produto {produto.nome} inserido com ID {id_inserido}")
    
    # Configurar paginação
    pagina = 3
    itens_por_pagina = 5
    offset = (pagina - 1) * itens_por_pagina
    
    # Buscar produtos da página 3
    produtos_pagina = produto_repo.obter_por_pagina(itens_por_pagina, offset)
    
    print(f"\nPágina {pagina} (mostrando {itens_por_pagina} produtos por página):")
    print("-" * 60)
    print(f"{'ID':<5} {'Nome':<20} {'Preço':>10} {'Estoque':>10}")
    print("-" * 60)
    
    for produto in produtos_pagina:
        print(f"{produto.id:<5} {produto.nome:<20} {f'R$ {produto.preco:.2f}':>10} {produto.estoque:>10}")

if __name__ == "__main__":
    main()