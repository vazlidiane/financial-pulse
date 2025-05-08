import pandas as pd 
import random
from faker import Faker # biblioteca que gera dados falsos (nomes, datas, endereços, etc)

# Inicializa faker
fake = Faker("pt_Br") # cria uma instância do Faker configurada para gerar dados no formato brasileiro

# Gerar vendas com 50 registros
vendas = []
for id_venda in range(1,51):  # identificador único da venda
    id_cliente = random.randint(1,20)  # número aleatório entre 1 e 20 clientes
    id_produto = random.randint(1,10)  # número aleatório entre 1 e 10 produtos
    data_venda = fake.date_time_between(start_date="1y", end_date="today")  # data aleatória entre um ano atrás e hoje
    quantidade = random.randint(1,5)  # quantidade vendida
    vendas.append([id_venda, id_produto, data_venda, quantidade])

# Criar DataFrame (transforma a lista de listas vendas em um DataFrame com colunas nomeadas)
vendas_df = pd.DataFrame(vendas, columns=["id_venda", "id_cliente", "id_produto", "data_venda", "quantidade"])

# Salvar como CSV (salva os dados do DataFrame no arquivo vendas.csv sem incluir a coluna de índice)
vendas_df.to_csv("vendas.csv", index=False)

# Visualizar os 5 primeiros registros (exibe os 5 primeiros registros do DataFrame no console)
print(vendas_df.head())

