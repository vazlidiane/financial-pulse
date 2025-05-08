import pandas as pd
import random

# Lista de nomes de produtos e categorias
nomes_produtos = ['Fone Bluetooth', 'Camiseta Polo', 'Liquidificador', 'Bicicleta', 'Abajur LED',
                  'Tênis Esportivo', 'Notebook', 'Moletom', 'Smartwatch', 'Cadeira Gamer']

categorias = ['Eletrônico', 'Vestuário', 'Casa', 'Esporte']

# Gerar os dados
produtos = pd.DataFrame({
    'id_produto': range(1, 11),
    'nome_produto': nomes_produtos,
    'categoria': [random.choice(categorias) for _ in range(10)],
    'preco_unitario': [round(random.uniform(50, 1000), 2) for _ in range(10)]
})

# Salvar como CSV
produtos.to_csv('produtos.csv', index=False)

# Mostrar os 5 primeiros
print(produtos.head())
