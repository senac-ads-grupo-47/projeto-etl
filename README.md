# projeto-etl
Projeto de ETL (Extract, Transform, Load) utilizando base de dados públicos do Kaggle
Uso da biblioteca pandas para tratamento, e Streamlit para publicação do dashboard

## Integrantes

- Denis Neves da Silva
- Isabelle Julia da Silva Fonseca
- Karen Beatriz Mereti de Oliveira
- Mateus Oliveira Macedo
- Rodrigo dos Santos Matrangolo
- Wagner Rodrigues de Souza

## Divisão de tarefas

Divisão incial, com possibilidade de alteração se necessário:
- Mateus: criação/manutenção repositório github
- Karen, Denis e Mateus: definição das transformações e visualizações
- Pedro: escrever arquivo `extract.py`
- Karen, Rodrigo e Isabelle: escrever arquivo `transform.py`
- Mateus: escrever arquivo `load.py`
- Denis: escrever arquivo `dashboard.py`

## Cronograma

Cronograma 1ª etapa:
- Até final de fevereiro/2026:
 - Criação do repositório no github
 - Definição do banco de dados no kaggle 
- Até terceira semana de março/2026:
 - Criar estrutura de pastas no repositório
 - Definir objetivo e transformações

## Tema

Base utilizada:  [**Conjunto de dados de preços de carros**](https://www.kaggle.com/datasets/mos3santos/conjunto-de-dados-de-preos-de-carros) do Kaggle.
O banco de dados contém informações sobre carros à venda, incluindo os campos:
- Marca: Kia, Chevrolet, Mercedes, Audi, etc.
- Modelo: Rio, Malibu, Gla, Q5, etc.
- Ano de fabricação: 2020, 2012, 2020, 2023
- Tamanho do motor, em litros (L): 4.2, 2.0, 1.3, 1.0, etc.
- Tipo de combustível: gaolina, diesel, híbrido, elétrico
- Transmissão: manual, automática, semi-automática, cvt, etc.
- Quilometragem rodada
- Número de portas: 3, 2, 4, 5, etc.
- Contagem de donos: 5, 3, 2, 1, etc.
- Preço do carro

## Objetivo

O objetivo do projeto é desenvolver um **pipeline completo de ETL (Extract, Transform, Load)** utilizando Python e Pandas, armazenando os dados tratados em um banco estruturado e criando uma dashboard interativa com Streamlit para análise dos dados.

## Ideia Inicial

Utilizar a base de dados com preços de carros para responder perguntas como:

- Quais fatores influenciam o preço dos carros?

A dashboard deve permitir:

- Filtros por cidade
- Filtros por categoria
- Filtros por preço
- Gráficos interativos
- Tabelas filtradas

## Planejamento do Projeto

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
