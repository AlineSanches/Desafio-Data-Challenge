from IPython.display import display
import pandas as pd
base_dados = pd.read_csv(
    './sales_20_21_train.csv')

# Mostrando todos os dados de um Cliente Específico
cliente_especifico = base_dados["ID_CLIENTE"] == 0

# Selecionado quais dados desejo ver de um Cliente Específico
cliente_especifico2 = base_dados.loc[base_dados['ID_CLIENTE'] == 337763, [
    "LOJA", "QTD_SKU", "VALOR"]]
# Calculando o valor total que cada cliente gastou durante esse período
valorTotal = base_dados[["ID_CLIENTE", "VALOR"]
                        ].groupby("ID_CLIENTE").sum()
valorTotal_df = pd.DataFrame(valorTotal)
# Calculando a media de valor que geralmente cada cliente gasta
mediaValorGasto = base_dados[["ID_CLIENTE", "VALOR"]
                             ].groupby("ID_CLIENTE").mean()
# Calculando a media de produtos que cada cliente compra
mediaProdutos = base_dados[["ID_CLIENTE", "QTD_SKU"]
                           ].groupby("ID_CLIENTE").mean()
# Calculando quantos produtos no total cada cliente comprou
produtosTotais = base_dados[["ID_CLIENTE", "QTD_SKU"]].groupby(
    "ID_CLIENTE").sum()


display(base_dados.loc[cliente_especifico])
# display(cliente_especifico2)
# display(valorTotal)
# display(mediaProdutos)
# display(mediaValorGasto)
# display(produtosTotais)
