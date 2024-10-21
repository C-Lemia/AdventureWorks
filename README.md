# Mini painel de controle de vendas baseado nos dados da base AdventureWorks

![image](https://github.com/user-attachments/assets/951641e8-c48d-4383-a275-d67ccce6af7a)


O objetivo é criar um painel interativo utilizando Streamlit, onde o usuários possam filtrar e visualizar informações relevantes sobre as vendas.

### 1º passo > banco de Dados:
- baixar e instalar o SQL : https://www.microsoft.com/pt-br/sql-server/sql-server-downloads
- baixar o Baixar o SSMS : https://learn.microsoft.com/pt-br/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16
- Fazer a instalação de ambos, esse vídeo mostra passo a passo para instalação e uso do SQL : https://www.youtube.com/watch?v=QOXiRS1yWhE
- baixar o AdventureWorks sample databases :https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms
- após a instalação do SQL e SSMS e após ter baixado do AdventureWorks > abrir o SQL > clicar com o botão direito em databases > restore database
- general > device > três pontos > add > copiar o caminho da pasta que vai abrir e colocar o arquivo baixado do AdventureWorks sample databases nesse caminho.

![image](https://github.com/user-attachments/assets/f93dfbca-b189-497f-a20d-7126b05f3636)

![image](https://github.com/user-attachments/assets/dc1e2331-e2b0-40de-a4a4-46c459365f7c)

![image](https://github.com/user-attachments/assets/8bc6b29e-25b7-4475-80cc-aa326c0d373a)

### 2º passo > Inicializando o Código:
- Vá até o diretório onde pretende clobnar o diretório no CMD
- Clonar o diretório : git clone https://github.com/C-Lemia/AdventureWorks
- No código db.py , fazer a conecção com o banco de dados de acordo com a tela de login do SQL, conforme imagem abaixo.

![image](https://github.com/user-attachments/assets/f36cafa1-893a-4a99-a0fa-7319184563ca)

### 3º Passo > Explicando o código:

#### bd.py : 
- usa pyodbc para conectar-se a um banco de dados SQL Server e executar uma consulta SQL que extrai informações relacionadas a vendas. Em seguida, os dados são carregados em um DataFrame do pandas, o que facilita a manipulação e análise dos dados.
- função usa pyodbc.connect para criar uma conexão com o banco de dados AdventureWorks2022 que está sendo executado no servidor DESKTOP-HMUNGS7 usando autenticação do Windows (Trusted_Connection).
- consulta é executada e os resultados são carregados em um DataFrame pandas usando o método pd.read_sql().
- função retorna o DataFrame df, que contém os dados resultantes da consulta. Este DataFrame pode ser usado para os outros códigos.

#### visualizacao.py:
- utiliza Streamlit para criar uma aplicação web interativa de análise de vendas.
- O layout da aplicação é dividido em duas colunas: Coluna 1 (col1): Exibe o título da análise de vendas. Coluna 2 (col2): Exibe o logo (imagem) no canto direito da aplicação.
- certifique-se de que o arquivo bd.py contém a função carregar_dados() que conecta ao banco de dados SQL Server AdventureWorks e retorna os dados de vendas.
- rode o código normalmente e depois rode o streamlit: streamlit run visualizacao.py

![image](https://github.com/user-attachments/assets/44aeb9c8-8b22-40ad-99b5-9b3d4d0edb89)
![image](https://github.com/user-attachments/assets/a977eacd-22e7-44f7-8149-0b8ad336650d)

#### resumo.py:
- o código utiliza Streamlit, Pandas e Plotly Express para criar uma aplicação web interativa de análise de vendas.
- plotly.express: Usado para criar gráficos interativos. pandas: Usado para manipulação de dados. streamlit: Usado para criar a interface web interativa.
- o código agrupa as vendas por região (StateProvinceID) e cria um gráfico de barras interativo, que exibe o total de vendas por região filtrada.
- o código cria um gráfico de linhas que mostra as vendas ao longo do tempo, agrupadas por ano e mês, a partir dos dados filtrados.
- certifique-se de que você tenha o Streamlit, Pandas, e Plotly instalados. Você pode instalar essas bibliotecas usando:pip install streamlit pandas plotly
- execute o streamlit : streamlit run resumo.py

  ![image](https://github.com/user-attachments/assets/3bbdd63b-9db1-48e9-8584-b629fc9f30ed)















