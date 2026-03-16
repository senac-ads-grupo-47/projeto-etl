# projeto-etl
Projeto de ETL (Extract, Transform, Load) utilizando base de dados públicos do Kraggle. Uso da biblioteca pandas para tratamento, e Streamlit para publicação do dashboard.

## Tema

Análise de dados de restaurantes e pedidos utilizando processo ETL com visualização interativa.

Base utilizada:  **Conjunto de dados de preços de carros** do Kaggle.

## Integrantes

- Integrante 1
- Integrante 2
- Integrante 3
- Integrante 4
- Integrante 5

## Objetivo

O objetivo do projeto é desenvolver um **pipeline completo de ETL (Extract, Transform, Load)** utilizando Python e Pandas, armazenando os dados tratados em um banco estruturado e criando uma dashboard interativa com Streamlit para análise dos dados.

O projeto deve conter:

- Extração de dados do Kaggle
- Tratamento com Pandas
- Transformação dos dados
- Armazenamento em banco estruturado
- Dashboard interativa com Streamlit
- Versionamento no GitHub
- Documentação no README

## Ideia Inicial

Utilizar a base de dados do iFood para responder perguntas como:

- Quais restaurantes têm melhor avaliação?
- Quais categorias vendem mais?
- Qual cidade tem mais pedidos?
- Qual faixa de preço é mais comum?
- Relação entre avaliação e preço

A dashboard deve permitir:

- Filtros por cidade
- Filtros por categoria
- Filtros por preço
- Gráficos interativos
- Tabelas filtradas

## 🧠 Planejamento do Projeto

Etapas do projeto:

### Etapa 1 — Setup

- Criar repositório no Github
- Definir dataset
- Definir tarefas
- Criar README

### Etapa 2 — Extract

- Baixar dataset do Kaggle
- Ler com Pandas
- Validar colunas

### Etapa 3 — Transform

- Limpar dados
- Tratar valores nulos
- Padronizar colunas
- Criar novas colunas

### Etapa 4 — Load

- Salvar dados tratados
- Inserir em banco estruturado (SQLite / PostgreSQL / MySQL)

### Etapa 5 — Dashboard

- Criar app com Streamlit
- Conectar com base tratada
- Criar gráficos interativos

### Etapa 6 — Finalização

- Ajustar README
- Testar projeto
- Publicar no GitHub

---

## Divisão de tarefas

### 👤 Pessoa 1 — GitHub + README + Planejamento

Responsável por:

- Criar repositório
- Criar README.md
- Organizar pastas
- Escrever documentação

Estrutura de pastas:

project/
data/
etl/
database/
dashboard/
README.md

Também escreve:

- Tema
- Objetivo
- Planejamento
- Ideia inicial

---

### 👤 Pessoa 2 — Extract (Extração)

Responsável por:

- Baixar dataset
- Ler com Pandas
- Validar dados
- Salvar dados brutos

Arquivo: etl/extract.py

Exemplo:

```python
import pandas as pd

df = pd.read_csv("data/raw/ifood.csv")

print(df.head())

```

👤 Pessoa 3 — Transform (Pandas)

Responsável por:

- Limpar dados
- Tratar valores nulos
- Criar colunas
- Converter tipos

Arquivo: etl/transform.py

Exemplo:

```python
df = df.dropna()

df["price"] = df["price"].astype(float)
```

👤 Pessoa 4 — Load (Banco de dados)

Responsável por:

- Criar banco SQLite / MySQL / PostgreSQL
- Criar tabela
- Inserir dados tratados

Arquivo: etl/load.py

Exemplo:

```python
import sqlite3

conn = sqlite3.connect("database.db")

df.to_sql("restaurants", conn, if_exists="replace")
```

👤 Pessoa 5 — Dashboard Streamlit

Responsável por:

- Criar app.py
- Conectar no banco
- Criar gráficos
- Criar filtros
