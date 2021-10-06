from IPython.display import display
import pandas as pd

def analiseExploratoria():
    # Mostrando todos os dados de um Cliente Específico
    cliente_especifico = base_dados["ID_CLIENTE"] == 0

    # Selecionado quais dados desejo ver de um Cliente Específico
    cliente_especifico2 = base_dados.loc[base_dados['ID_CLIENTE'] == 337763, [  
    "LOJA", "QTD_SKU", "VALOR"]]

    # Calculando a media de produtos que cada cliente compra
    mediaProdutos = base_dados[["ID_CLIENTE", "QTD_SKU"]
                           ].groupby("ID_CLIENTE").mean()

    # Calculando o valor total que cada cliente gastou durante esse período
    valorTotal = base_dados[["ID_CLIENTE", "VALOR"]
                        ].groupby("ID_CLIENTE").sum()

    valorTotal_df = pd.DataFrame(valorTotal)
    # Calculando a media de valor que geralmente cada cliente gasta
    mediaValorGasto = base_dados[["ID_CLIENTE", "VALOR"]
                                ].groupby("ID_CLIENTE").mean()

    
    # Calculando quantos produtos no total cada cliente comprou
    produtosTotais = base_dados[["ID_CLIENTE", "QTD_SKU"]].groupby(
    "ID_CLIENTE").sum()

    # display(base_dados.loc[cliente_especifico])
    # display(cliente_especifico2)
    # display(valorTotal)
    # display(mediaProdutos)
    # display(mediaValorGasto)
    # display(produtosTotais)
    return None


# PROGRAMA PRINCIPAL
# Importando os dados dos arquivos .csv em DataFrames
base_dados = pd.read_csv(
    './sales_20_21_train.csv')
prev_dados = pd.read_csv(
    './sample_submission.csv')

analiseExploratoria()

# Criando um DataFrame com base no base_dados que filtrando apenas os clientes dos quais devemos mostrar o LTV
# ou seja, mescla os dois com base no ID_CLIENTE
df_mesclado = pd.merge(base_dados, prev_dados, how="inner", on=["ID_CLIENTE"])
#display(df_mesclado.sort_values(by="ID_CLIENTE"))

# Criando uma nova série apenas com dados de um período de vendas específico (no momento, corresponde ao período total)
selecao_periodo = (df_mesclado["DT_VENDA"] >= '2020-01-02') & (df_mesclado["DT_VENDA"]
                                                      <= '2021-02-24')

# Criando um DataFrame com os dados selecionados do período
df_filtrado = df_mesclado[selecao_periodo]
#display(df_filtrado)

# Calculando a qtd de compras no período de um cliente, caso selecionado um cliente (no momento, não é útil)
qtd_compras, colunas = df_filtrado.shape

# Criando uma série com a quantidade de compras de cada cliente no período de "selecao", na qual o index é o ID_CLIENTE (?)
freq_periodo = df_filtrado['ID_CLIENTE'].value_counts()
#display(freq_periodo)

# Criando uma série com a quantidade de compras de cada cliente no período total, na qual o index é o ID_CLIENTE (?)
freq_total = df_mesclado['ID_CLIENTE'].value_counts()
#display(freq_total)

# Criando uma série com a média do valor das compras de um cliente, na qual o index é o ID_CLIENTE
mediaValorGasto = df_filtrado[["ID_CLIENTE", "VALOR_x"]
                             ].groupby("ID_CLIENTE").mean()

# Criando um novo DataFrame com as colunas de frequência, média do valor das compras e ID do cliente
df_final = pd.DataFrame()
df_final['FREQ PERIODO'] = freq_periodo
df_final['FREQ TOTAL'] = freq_total
df_final['MEDIA VALOR'] = mediaValorGasto
df_final['ID_CLIENTE'] = df_final.index
#display(df_final)

# Fazendo o cálculo do LTV em uma nova coluna "VALOR"
df_final["VALOR"] = df_final["FREQ PERIODO"] * df_final['MEDIA VALOR'] / 4
#display(df_final)

# Excluindo as colunas de frequência e média do valor das compras para combinar com o arquivo de submissão
df_final = df_final.drop('FREQ PERIODO', axis=1)
df_final = df_final.drop('FREQ TOTAL', axis=1)
df_final = df_final.drop('MEDIA VALOR', axis=1)

# Ordenando o df com base no ID_CLIENTE
df_final = df_final.sort_values(by="ID_CLIENTE")
display(df_final)

#display(base_dados)
#display(dados_prev)

# Transformando o DataFrame em um arquivo .csv (sem index)
df_final.to_csv("previsao.csv", index=False)
