import pandas as pd

# Importar os arquivos CSV a partir da pasta 'dados_excel'
clientes = pd.read_csv('dados_excel/clientes.csv')
produtos = pd.read_csv('dados_excel/produtos.csv')
vendas = pd.read_csv('dados_excel/vendas.csv')
pagamentos = pd.read_csv('dados_excel/pagamentos.csv')
despesas = pd.read_csv('dados_excel/despesas.csv')

# Conferir os tipos de dados
print(clientes.dtypes)
print(produtos.dtypes)
print(vendas.dtypes)
print(pagamentos.dtypes)
print(despesas.dtypes)

# Corrigir Formatos de Data
clientes['data_cadastro'] = pd.to_datetime(clientes['data_cadastro'])
vendas['data_venda'] = pd.to_datetime(vendas['data_venda'])
pagamentos['data_pagamento'] = pd.to_datetime(pagamentos['data_pagamento'])
despesas['data'] = pd.to_datetime(despesas['data'])

# Verificar valores ausentes
print(clientes.isnull().sum())
print(produtos.isnull().sum())
print(vendas.isnull().sum())
print(pagamentos.isnull().sum())
print(despesas.isnull().sum())

# Preenhcer dados faltantes
clientes.dropna(inplace=True)
produtos.dropna(inplace=True)
vendas.dropna(inplace=True)
pagamentos.dropna(inplace=True)
despesas.dropna(inplace=True)

# Salvar os dados limpos em novos arquivos
clientes.to_csv('clientes_limpo.csv', index=False)
produtos.to_csv('produtos_limpo.csv', index=False)
vendas.to_csv('vendas_limpo.csv', index=False)
pagamentos.to_csv('pagamentos_limpo.csv', index=False)
despesas.to_csv('despesas_limpo.csv', index=False)

