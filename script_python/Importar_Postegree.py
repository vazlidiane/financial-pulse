import psycopg2
import pandas as pd

# Conexão com o banco de dados
con = psycopg2.connect(
    host="localhost",
    database="financial_pulse",
    user="postgres",
    password="123456"  # <- sua senha do PostgreSQL
)

cur = con.cursor()

# Importar clientes
clientes = pd.read_csv('dados_excel/clientes.csv')
for _, row in clientes.iterrows():
    cur.execute("""
        INSERT INTO clientes (id_cliente, nome, cidade, data_cadastro)
        VALUES (%s, %s, %s, %s)
    """, tuple(row))

# Importar produtos
produtos = pd.read_csv('dados_excel/produtos.csv')
for _, row in produtos.iterrows():
    cur.execute("""
        INSERT INTO produtos (id_produto, nome_produto, categoria, preco_unitario)
        VALUES (%s, %s, %s, %s)
    """, tuple(row))

# Importar vendas
vendas = pd.read_csv('dados_excel/vendas.csv')
for _, row in vendas.iterrows():
    cur.execute("""
        INSERT INTO vendas (id_venda, id_cliente, id_produto, data_venda, quantidade)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

# Importar pagamentos
pagamentos = pd.read_csv('dados_excel/pagamentos.csv')
for _, row in pagamentos.iterrows():
    cur.execute("""
        INSERT INTO pagamentos (id_venda, data_pagamento, valor_pago)
        VALUES (%s, %s, %s)
    """, tuple(row))

# Importar despesas
despesas = pd.read_csv('dados_excel/despesas.csv')
for _, row in despesas.iterrows():
    cur.execute("""
        INSERT INTO despesas (data, tipo_despesa, valor)
        VALUES (%s, %s, %s)
    """, tuple(row))

# Confirmar alterações
con.commit()
cur.close()
con.close()

print("Dados importados com sucesso!")
