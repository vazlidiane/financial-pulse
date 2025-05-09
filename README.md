## Financial Pulse – Análise Financeira Inteligente 
# com Python, PostgreSQL e Power BI

Este projeto apresenta um dashboard completo e interativo desenvolvido para simular a gestão financeira de uma empresa, utilizando uma stack poderosa de **Excel + Python + PostgreSQL + Power BI + GitHub**.  
O objetivo é demonstrar domínio no processo de análise de dados de ponta a ponta, da simulação à visualização.

---

## 🔍 Visão Geral

**Financial Pulse** é um painel financeiro dinâmico e elegante, que permite:

- 📈 Analisar faturamento total e mensal  
- 💳 Monitorar inadimplência e ticket médio  
- 🛒 Avaliar produtos mais vendidos e clientes mais lucrativos  
- 📊 Acompanhar despesas por categoria  
- 🔍 Navegar pelos dados com filtros inteligentes  

---

## 🚀 Tecnologias Utilizadas

| Etapa                 | Ferramenta               |
|-----------------------|--------------------------|
| Simulação de dados    | Python (Faker, Pandas)   |
| Banco de Dados        | PostgreSQL + PgAdmin     |
| Visualização          | Power BI Desktop         |
| Versionamento         | Git + GitHub             |

---

## 🧩 Estrutura dos Dados

Foram geradas e tratadas 5 tabelas principais:

- **clientes** (id, nome, cidade, data_cadastro)  
- **produtos** (id, nome, categoria, preço)  
- **vendas** (id, cliente, produto, data, quantidade)  
- **pagamentos** (venda, data_pagamento, valor_pago)  
- **despesas** (data, tipo_despesa, valor)  

---

## 🔗 Conexões

- As tabelas foram inseridas no PostgreSQL e integradas ao Power BI.
- Foram criados relacionamentos entre tabelas (`1:N`) e uma **tabela calendário** para filtros temporais.

---

## 📐 Métricas DAX

O dashboard conta com medidas como:

```DAX
Faturamento = SUM(pagamentos[valor_pago])
Total de Vendas = COUNT(vendas[id_venda])
Ticket Médio = DIVIDE([Faturamento], [Total de Vendas])
Faturamento YTD = TOTALYTD([Faturamento], Calendario[Date])
Total Esperado = SUMX(vendas, RELATED(produtos[preco_unitario]) * vendas[quantidade])
Inadimplência = [Total Esperado] - [Faturamento]
% Inadimplência = DIVIDE([Inadimplência], [Total Esperado], 0)
```

---

## 🖼️ Layout do Dashboard


KPIs no topo com ícones (faturamento, ticket médio, inadimplência)

Gráficos de linha e coluna com evolução mensal

Tabelas com ranking de produtos e clientes

Pizza com distribuição de despesas

Filtros por data, cidade e categoria

---

## 📁 Estrutura de Pastas

financial-pulse/
├── dados_excel/
│   └── clientes.csv, produtos.csv...
├── script_python/
│   └── criar_dados.py, importar_sql.py...
├── sql/
│   └── criar_tabelas.sql
├── power_bi/
│   └── dashboard.pbix
├── imagens/
│   └── preview_dashboard.png
├── README.md

---

## 📘 Aprendizados
Criação e manipulação de dados realistas

Automatização de ETL com Python

Modelagem relacional no PostgreSQL

Criação de dashboard profissional no Power BI

Publicação e versionamento no GitHub

---

## 🤝 Conecte-se comigo

🔗 [LinkedIn](https://www.linkedin.com/in/lidiane-vaz)  

📬 [lidiane.vaz.ti@gmail.com](mailto:lidiane.vaz.ti@gmail.com) 

🐙 [GitHub](https://github.com/vazlidiane)
