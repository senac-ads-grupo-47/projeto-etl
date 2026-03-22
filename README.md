# projeto-etl

Projeto de ETL (Extract, Transform, Load) utilizando base de dados públicos do Kaggle
Uso da biblioteca pandas para tratamento, e Streamlit para publicação do dashboard

O desenvolvimento deste projeto de ETL se justifica pela crescente necessidade de transformar
grandes volumes de dados brutos em informações úteis para apoio à tomada de decisão

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
- Pedro: escrever arquivo [`extract.py`](source/extract.py)
- Karen, Rodrigo e Isabelle: escrever arquivo [`transform.py`](source/transform.py)
- Mateus: escrever arquivo [`load.py`](source/load.py)
- Denis: escrever arquivo [`dashboard.py`](app/dashboard.py)

## Cronograma

Cronograma 1ª etapa:
- Até final de fevereiro/2026:
  - Criação do repositório no github
  - Definição do banco de dados no kaggle 
- Até terceira semana de março/2026:
  - Criar estrutura de pastas no repositório
  - Definir objetivo e transformações

## Tema

[Base](data-frame/dados.md) utilizada:  [**Conjunto de dados de preços de carros**](https://www.kaggle.com/datasets/mos3santos/conjunto-de-dados-de-preos-de-carros) do Kaggle.
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

### Objetivo

O objetivo do projeto é desenvolver um **pipeline completo de ETL (Extract, Transform, Load)** utilizando Python e Pandas,
armazenando os dados tratados em um banco estruturado e criando uma dashboard interativa com Streamlit para análise dos dados

Esse tipo de base possibilita explorar variáveis relevantes, como marca, ano, tipo de combustível e quilometragem,
e identificar como elas influenciam diretamente na precificação de veículos

O uso da biblioteca Pandas viabiliza a manipulação eficiente dos dados, enquanto a biblioteca Streamlit permite
a criação de visualizações interativas acessíveis, facilitando a interpretação dos resultados por diferentes usuários

O projeto também contribui para o desenvolvimento de habilidades técnicas fundamentais, como organização de código,
versionamento com GitHub, trabalho em equipe e divisão de responsabilidades, simulando um ambiente real

### Ideia Inicial

Possíveis transformações necessárias:
- Normalização: ajustar os valores numéricos para uma escala comum/padrão
- Convrsão de variáveis: converter variáveis em formatos que possam ser mais facilmente manipulados
- Conversão de tipos: transformar tipos `strings`, que representam datas, em tipos numéricos
- Reestruturação: renomear ou concatenar colunas de dados
- Agrupamento: organizar dados duplicados ou similares em uma só coluna

Utilizar a base de dados com preços de carros para responder perguntas como:
- Quais fatores que mais influenciam o preço dos carros?
- Qual a tendência dos preços com o passar dos anos?
- Quais técnicas são as mais eficientes para manter o preço de um carro, com o passar dos anos?

A dashboard deve permitir:
- Filtros por: marca, ano de fabricação, tipo de combustível, transmissão, e quilometragem rodada
- Gráficos interativos: preço x variável
- Tabelas filtradas
- Ordenação personalizada: menor para maior, maior para menor, mais populares, etc.

## Planejamento do Projeto

### Etapa 1: Setup

- Criar repositório no Github
- Definir dataset
- Definir tarefas
- Criar README

### Etapa 2: [Extract](source/extract.py)

- Baixar dataset do Kaggle
- Ler com Pandas
- Validar colunas

### Etapa 3: [Transform](source/transform.py)

- Limpar dados
- Tratar valores nulos
- Padronizar colunas

### Etapa 4: [Load](source/load.py)

- Salvar dados tratados
- Inserir em banco estruturado

### Etapa 5: [Dashboard](app/dashboard.py)

- Criar app com Streamlit
- Conectar com base tratada
- Criar gráficos interativos
