import pyodbc
import pandas as pd

def carregar_dados():
    # Conectar ao banco de dados SQL Server----------------------------
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-HMUNGS7;'  # Nome do servidor conforme a sua configuração
        'DATABASE=AdventureWorks2022;'  # Nome do banco de dados 
        'Trusted_Connection=yes;'  # Usa a autenticação do Windows
    )

    # Criar a consulta SQL
    query = """
        SELECT 
            soh.OrderDate,                       -- Data do pedido
            soh.TotalDue,                        -- Valor total do pedido
            addr.StateProvinceID,                -- Região via StateProvinceID
            prod.Name AS ProductName             -- Nome do produto
        FROM 
            Sales.SalesOrderHeader AS soh        -- Tabela de cabeçalho de pedidos
        JOIN 
            Sales.SalesOrderDetail AS sod ON soh.SalesOrderID = sod.SalesOrderID   -- Relaciona com detalhes do pedido
        JOIN 
            Production.Product AS prod ON sod.ProductID = prod.ProductID           -- Relaciona com a tabela de produtos
        JOIN 
            Person.Address AS addr ON soh.ShipToAddressID = addr.AddressID         -- Relaciona com a tabela de endereço
    """

    # Executar a consulta SQL e carregar os dados em um DataFrame pandas---------------------------------------
    df = pd.read_sql(query, conn)

    # Fechar a conexão---------------------------
    conn.close()

    # Retornar o DataFrame com os dados para ser utilizado no plot---------------------------------------
    return df
