from IPython.display import display
from collections import Counter
import pandas as pd

base_dados = pd.read_csv(
    './sales_20_21_train.csv')
dados_prev = pd.read_csv('./sample_submission.csv')

# Mostrando todos os dados de um Cliente Específico
cliente_especifico = base_dados["ID_CLIENTE"] == 0

# Selecionado quais dados desejo ver de um Cliente Específico
cliente_especifico3 = base_dados.loc[base_dados['ID_CLIENTE'] == 337763, [
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

int_df = pd.merge(base_dados, dados_prev, how="inner", on=["ID_CLIENTE"])

# Mostrar compras de um cliente especifico dentro de um intervalo de tempo
selecao = (int_df["DT_VENDA"] >= '2020-01-02') & (int_df["DT_VENDA"]
                                                      <= '2021-02-24')

dt_filtrado = int_df[selecao]
display(dt_filtrado)
qtd_compras, colunas = dt_filtrado.shape
#print(qtd_compras)

freq_periodo = dt_filtrado['ID_CLIENTE'].value_counts()
#display(freq_periodo)

freq_total = int_df['ID_CLIENTE'].value_counts()
#display(freq_total)

df = pd.DataFrame()
df['FREQ PERÍODO'] = freq_periodo
# df['FREQ TOTAL'] = freq_total

mediaValorGasto = dt_filtrado[["ID_CLIENTE", "VALOR_x"]
                             ].groupby("ID_CLIENTE").mean()
df['MEDIA VALOR'] = mediaValorGasto
df['ID_CLIENTE'] = df.index
df["VALOR"] = df["FREQ PERÍODO"] * df['MEDIA VALOR'] / 4

#display(df)

df = df.drop('MEDIA VALOR', axis=1)
df = df.drop('FREQ PERÍODO', axis=1)
df = df.sort_values(by="ID_CLIENTE")
display(df)

#display(int_df.sort_values(by="ID_CLIENTE"))

#display(base_dados)
#display(dados_prev)
#display(ordenado)

df.to_csv("previsao.csv", index=False)


# display(base_dados.loc[cliente_especifico])
# display(cliente_especifico2)
# display(valorTotal)
# display(mediaProdutos)
# display(mediaValorGasto)
# display(produtosTotais)
