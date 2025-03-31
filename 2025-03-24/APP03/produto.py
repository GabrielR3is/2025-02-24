from dataclasses import dataclass

@dataclass
class Produto:
    id: int
    nome: str
    preco: float
    estoque: int