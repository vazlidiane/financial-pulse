import pandas as pd
import random
from faker import Faker

# Inicializar faker
fake = Faker('pt_BR')

# Carregar o arquivo de vendas
vendas = pd.read_csv('vendas.csv')

# Gerar pagamentos com base nas vendas
pagamentos = []
for _, row in vendas.iterrows():
    if random.random() > 0.1:  # 90% chance de ter sido paga
        id_venda = row['id_venda']
        data_inicio = pd.to_datetime(row['data_venda']).date()
        data_pagamento = fake.date_between(start_date=data_inicio, end_date='today')
        preco_unitario = random.uniform(50, 1000)  # Simulação de preço (ou usar o produto real)
        valor_pago = round(preco_unitario * row['quantidade'], 2)
        pagamentos.append([id_venda, data_pagamento, valor_pago])

# Criar DataFrame
pagamentos_df = pd.DataFrame(pagamentos, columns=['id_venda', 'data_pagamento', 'valor_pago'])

# Salvar como CSV
pagamentos_df.to_csv('pagamentos.csv', index=False)

# Mostrar os 5 primeiros registros
print(pagamentos_df.head())
