import streamlit as st
import pandas as pd
import plotly.express as px
import os

# config da página

st.set_page_config(
    page_title="Dashboard ETL - Carros",
    layout="wide"
)

# header and description

st.title(" Dashboard de Análise de Preços de Carros")
st.markdown(
    """
    Dashboard interativa desenvolvida com Streamlit para análise
    de preços de veículos com base em dados tratados via pipeline ETL.
    """
)

# reading data

@st.cache_data
def carregar_dados():

    caminho_csv = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data-frame",
        "modified",
        "car_price_dataset_mod.csv"
    )

    df = pd.read_csv(caminho_csv)

    return df


df = carregar_dados()

# sidebar filters - Aqui tem alguns dados rápidos pra filtro que a gente pode usar pra deixar o dashboard mais interativo, mas a gente pode deixar isso pra depois, o importante é ter os gráficos e os KPIs funcionando, aí depois a gente vai incrementando com mais filtros e mais gráficos, beleza?

st.sidebar.header("Filtros")

# Marca
marcas = sorted(df["brand"].dropna().unique())

marca_selecionada = st.sidebar.multiselect(
    "Selecione a marca:",
    marcas,
    default=marcas
)

# fuel type
combustiveis = sorted(df["fuel_type"].dropna().unique())

combustivel_selecionado = st.sidebar.multiselect(
    "Tipo de combustível:",
    combustiveis,
    default=combustiveis
)

# transmission
transmissoes = sorted(df["transmission"].dropna().unique())

transmissao_selecionada = st.sidebar.multiselect(
    "Transmissão:",
    transmissoes,
    default=transmissoes
)

# year
ano_min = int(df["year"].min())
ano_max = int(df["year"].max())

ano_selecionado = st.sidebar.slider(
    "Ano de fabricação:",
    min_value=ano_min,
    max_value=ano_max,
    value=(ano_min, ano_max)
)

# filtering data

df_filtrado = df[
    (df["brand"].isin(marca_selecionada)) &
    (df["fuel_type"].isin(combustivel_selecionado)) &
    (df["transmission"].isin(transmissao_selecionada)) &
    (df["year"].between(ano_selecionado[0], ano_selecionado[1]))
]

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado. Por favor, ajuste os filtros.")
    st.stop()

# kpis

st.subheader("Indicadores Gerais")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total de carros",
        len(df_filtrado)
    )

with col2:
    st.metric(
        "Preço médio",
        f"${df_filtrado['price'].mean():,.2f}"
    )

with col3:
    st.metric(
        "Maior preço",
        f"${df_filtrado['price'].max():,.2f}"
    )

with col4:
    st.metric(
        "Média de quilometragem",
        f"{df_filtrado['mileage'].mean():,.0f} km"
    )

# charts

st.subheader("Visualizações")

# price by brand

preco_marca = (
    df_filtrado
    .groupby("brand")["price"]
    .mean()
    .reset_index()
    .sort_values(by="price", ascending=False)
)

grafico_marca = px.bar(
    preco_marca,
    x="brand",
    y="price",
    title="Preço Médio por Marca",
    labels={
        "brand": "Marca",
        "price": "Preço Médio"
    }
)

st.plotly_chart(
    grafico_marca,
    use_container_width=True
)

# price x mileage

grafico_scatter = px.scatter(
    df_filtrado,
    x="mileage",
    y="price",
    color="fuel_type",
    hover_data=["brand", "model"],
    title="Preço x Quilometragem"
)

st.plotly_chart(
    grafico_scatter,
    use_container_width=True
)

# combustível

combustivel_count = (
    df_filtrado["fuel_type"]
    .value_counts()
    .reset_index()
)

combustivel_count.columns = [
    "fuel_type",
    "count"
]

grafico_pizza = px.pie(
    combustivel_count,
    names="fuel_type",
    values="count",
    title="Distribuição por Tipo de Combustível"
)

st.plotly_chart(
    grafico_pizza,
    use_container_width=True
)

# price by year

grafico_ano = px.box(
    df_filtrado,
    x="year",
    y="price",
    title="Distribuição de Preços por Ano"
)

st.plotly_chart(
    grafico_ano,
    use_container_width=True
)

# table, aqui a gente não manter essa parte, mas costuma ser interessante ter uma tabela com os dados filtrados caso o usuário queira explorar mais a fundo

st.subheader("Dados Filtrados")

st.dataframe(
    df_filtrado,
    use_container_width=True
)

# footer
# aqui a gente pode colocar um rodapé com informações sobre o projeto, o autor, ou links para o repositório do código, etc mas só se quiser kkkkkk
st.markdown("---")

st.markdown(
    """
    Projeto de ETL desenvolvido com Python, Pandas e Streamlit.
    """
)