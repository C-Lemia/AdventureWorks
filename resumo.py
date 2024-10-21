import plotly.express as px
import pandas as pd
import streamlit as st

######## Caminho da imagem
image_path = "hexagon.png"

##### Organizar o layout
col1, col2 = st.columns([3, 1])

with col1:
    #####Importar o arquivo bd.py
    from bd import carregar_dados  

    ##### Carregar os dados do banco de dados
    df = carregar_dados()

    ##### Formato de data
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])

    ##### Criar colunas de ano e mês a partir da data do pedido
    df['Ano'] = df['OrderDate'].dt.year
    df['Mes'] = df['OrderDate'].dt.month

    ##### Adicionar widgets de filtro no Streamlit
    st.sidebar.header("Filtros")

    # Filtro por intervalo de datas ####
    data_inicio = st.sidebar.date_input("Data Inicial", value=df['OrderDate'].min())
    data_fim = st.sidebar.date_input("Data Final", value=df['OrderDate'].max())

    # Filtro por região ####
    regioes_selecionadas = st.sidebar.multiselect("Selecione as Regiões", options=df['StateProvinceID'].unique(), default=df['StateProvinceID'].unique())

    # Filtro por valor total (slider) ####
    valor_min, valor_max = int(df['TotalDue'].min()), int(df['TotalDue'].max())
    valor_selecionado = st.sidebar.slider("Valor Total (Filtro)", min_value=valor_min, max_value=valor_max, value=(valor_min, valor_max))

    # Aplicar os filtros aos dados####
    df_filtrado = df[
        (df['OrderDate'] >= pd.to_datetime(data_inicio)) & 
        (df['OrderDate'] <= pd.to_datetime(data_fim)) & 
        (df['StateProvinceID'].isin(regioes_selecionadas)) & 
        (df['TotalDue'] >= valor_selecionado[0]) & 
        (df['TotalDue'] <= valor_selecionado[1])
    ]

    #####Gráfico de Barras: Vendas por Região
    vendas_por_regiao = df_filtrado.groupby('StateProvinceID')['TotalDue'].sum().reset_index()
    vendas_por_regiao.columns = ['Regiao', 'VendasTotais']

    fig_barras = px.bar(
        vendas_por_regiao, 
        x='Regiao', 
        y='VendasTotais', 
        title="Vendas por Região",
        labels={'Regiao': 'Região', 'VendasTotais': 'Vendas Totais'},
        color_discrete_sequence=px.colors.qualitative.Bold  # Escolhe uma paleta de cores
    )

    st.plotly_chart(fig_barras)

    #####Gráfico de Linhas: Vendas ao Longo do Tempo (Ano e Mês, após filtro)
    vendas_por_tempo = df_filtrado.groupby(['Ano', 'Mes'])['TotalDue'].sum().reset_index()

    # Ajuste para criar uma data válida 
    vendas_por_tempo['Data'] = pd.to_datetime(vendas_por_tempo['Ano'].astype(str) + '-' + vendas_por_tempo['Mes'].astype(str) + '-01')

    fig_linhas = px.line(
        vendas_por_tempo, 
        x='Data', 
        y='TotalDue', 
        title="Vendas ao Longo do Tempo",
        labels={'Data': 'Data', 'TotalDue': 'Vendas Totais'},
        markers=True
    )

    st.plotly_chart(fig_linhas)

    st.subheader("Dados Filtrados")
    st.dataframe(df_filtrado)

with col2:
    st.image(image_path, use_column_width=True)
