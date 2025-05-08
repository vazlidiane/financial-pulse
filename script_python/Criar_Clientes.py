import pandas as pd
from faker import Faker

# Criar gerador de dados brasileiros
fake = Faker('pt_BR')

# Gerar 20 clientes
clientes = pd.DataFrame({
    'id_cliente': range(1, 21),
    'nome': [fake.name() for _ in range(20)],
    'cidade': [fake.city() for _ in range(20)],
    'data_cadastro': [fake.date_between(start_date='-3y', end_date='today') for _ in range(20)]
})

# Salvar como CSV
clientes.to_csv('clientes.csv', index=False)

# Exibir os 5 primeiros para confirmar
print(clientes.head())
