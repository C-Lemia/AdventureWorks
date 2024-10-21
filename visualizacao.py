import streamlit as st
import pandas as pd
import plotly.express as px

# Caminho da imagem
image_path = "C:/Users/camil/hexagon/hexagon.png"

# Usar colunas para organizar o layout --------------------------
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Análise de Vendas - AdventureWorks2022")

# Aumentar o logo ------------------------------
with col2:
    st.image(image_path, use_column_width=False, width=200)  

# Importar o arquivo bd.py-----------------------------
from bd import carregar_dados

# Carregar os dados do banco de dados-----------------------
df = carregar_dados()

df['OrderDate'] = pd.to_datetime(df['OrderDate'])

df['Ano'] = df['OrderDate'].dt.year
df['Mes'] = df['OrderDate'].dt.month

vendas_por_regiao = df.groupby('StateProvinceID')['TotalDue'].sum().reset_index()
vendas_por_regiao.columns = ['Regiao', 'VendasTotais']

vendas_por_produto = df.groupby('ProductName')['TotalDue'].sum().reset_index()
vendas_por_produto.columns = ['Produto', 'VendasTotais']

# Filtrar os 5 produtos mais vendidos------------
top5_produtos = vendas_por_produto.nlargest(5, 'VendasTotais')

# Filtrar as 5 regiões com mais vendas----------------
top5_regioes = vendas_por_regiao.nlargest(5, 'VendasTotais')

# Converta 'Regiao' para string para garantir que o eixo x seja categórico
top5_regioes['Regiao'] = top5_regioes['Regiao'].astype(str)

# Gráfico de Barras - Vendas por Produto (Top 5)
st.subheader("Top 5 Produtos Mais Vendidos")
fig_produto = px.bar(
    top5_produtos, 
    x='Produto', 
    y='VendasTotais', 
    title="Vendas por Produto (Top 5)",
    color_discrete_sequence=["#00AEEF", "#007A87", "#7AC943", "#39B54A", "#007A87"]  # Cores personalizadas
)
st.plotly_chart(fig_produto)

# Gráfico de Barras - Vendas por Região (Top 5)
st.subheader("Top 5 Regiões com Mais Vendas")
# Aqui garantimos que o eixo x trate 'Regiao' como uma categoria (categórico)
fig_regiao = px.bar(
    top5_regioes, 
    x='Regiao',  # Agora 'Regiao' está como string, categórico
    y='VendasTotais', 
    title="Vendas por Região (Top 5)",
    labels={'Regiao': 'Região', 'VendasTotais': 'Vendas Totais'},
    color_discrete_sequence=["#7AC943", "#00AEEF", "#39B54A", "#007A87", "#00AEEF"],  # Cores personalizadas
    category_orders={"Regiao": top5_regioes['Regiao']}  # Ordenação categórica explícita
)
st.plotly_chart(fig_regiao)

# Exibir todos os dados na tabela (completo)
st.subheader("Vendas por Produto - Todos")
st.dataframe(vendas_por_produto)

st.subheader("Vendas por Região - Todos")
st.dataframe(vendas_por_regiao)
