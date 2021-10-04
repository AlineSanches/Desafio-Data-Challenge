# como usar o pandas
from IPython.display import display
import pandas as pd

# dataframe = pd.DataFrame()

# Criando um dataframe a partir de um dicionário
""""venda = {"data": ['15/02/2021', '16/02/2021'],
         "valor": [500, 300],
         "produto": ['Feijão', 'Arroz'],
         "qtde": [50, 70]}

venda_df = pd.DataFrame(venda)

display(venda_df)"""

vendas_df = pd.read_csv(
    'C:/Users/fredm/OneDrive/Área de Trabalho/Data-Challenge/sales_20_21_train.csv')

# Visualizar as primeiras 5 linhas do meu arquivo: .head(), se eu quiser aumentar o número de linhas, só fazer head(10)
display(vendas_df.head(2))

# Para saber quantas linhas e colunas tem na tabela: .shape
display(vendas_df.shape)

# Para ter uma descrição da tabela: .describe()
display(vendas_df.describe())

# pegar uma coluna: lojas = vendas_df['Loja']
lojas = vendas_df['LOJA']
display(lojas)

# pegar uma linhas: vendas_df.loc[1] [1:5]
display(vendas_df.loc[1])

# pegar linhas que correspondem a uma condição: lojas == 37
display(vendas_df.loc[vendas_df['LOJA'] == 37])

# pegar várias linhas e colunas usando o Loc: .loc[linhas, colunas]
cliente_especifico = vendas_df.loc[vendas_df['ID_CLIENTE'] == 337763, [
    "QTD_SKU", "LOJA", "VALOR"]]
display(cliente_especifico)

# pegar um valor especifico: vendas_df.loc[linha, coluna]

''' criar 1 coluna nova
  #! a partir de uma valor que já existe
  vendas_df['COMISSÃO'] = vendas_df['VALOR'] * 0.05

  #! criar uma coluna com valor padrão
  vendas_df.loc[:, "IMPOSTO] = 0
'''

# adicionar uma linha
vendas_df = vendas_df.append("Linha nova ou um arquivo novo")

# excluir linhas e colunas
# coluna axis = 1, linha axis = 0
vendas_df = vendas_df.drop("Imposto", axis=1)

""" Tratar Valores Vazios
  #! deletar linhas e colunas completamente Vazios
    vendas_df = vendas_df.dropna(how='all') posso usar axis também
  #! deletar linhas que possuem pelo menos um valor vazios
    vendas_df = vendas_df.dropna()
  #! preencher valores vazios
  #! preencher com a média da coluna
    vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
  #! preencher com o ultimo valor
    vendas_df = vendas_df.ffill()
"""

# Calcular quantidades
vendas_df['QTD_SKU'].value_counts()

# agrupar e somar
faturamento_produto = vendas_df.groupby(
    'Produto').sum()  # aqui faço isso na tabela toda
faturamento_produto = vendas_df[["Produto", 'Valor Final']].groupby(
    'Produto').sum()  # vai somar só valor final

# Mesclar duas tabelas
vendas_df = vendas_df.merge("Nome da outra tabela")
