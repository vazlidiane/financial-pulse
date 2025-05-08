import pandas as pd
import random
from faker import Faker

# Inicializar faker
fake = Faker('pt_BR')

# Tipos de despesa comuns
tipos_despesa = ['Aluguel', 'Salários', 'Marketing', 'Manutenção', 'Serviços']

# Gerar 30 registros de despesa
despesas = []
for _ in range(30):
    data = fake.date_between(start_date='-1y', end_date='today')
    tipo = random.choice(tipos_despesa)
    valor = round(random.uniform(500, 8000), 2)
    despesas.append([data, tipo, valor])

# Criar DataFrame
despesas_df = pd.DataFrame(despesas, columns=['data', 'tipo_despesa', 'valor'])

# Salvar como CSV
despesas_df.to_csv('despesas.csv', index=False)

# Mostrar os 5 primeiros
print(despesas_df.head())
