import pandas as pd

# Filtrar os dados
dados = pd.read_csv('product_data.csv')
df_product = dados.filter(items=['Product type', 'Price'])

# Função para calcular as estatísticas
def cent_stats(foo):
    avg = foo.mean()
    median = foo.median()
    mode = foo.mode()[0] if not foo.mode().empty else None
    quartil = foo.quantile([0.25, 0.5, 0.75])
    amplitude = foo.max() - foo.min()
    variancia = foo.var()
    desvio_padrao = foo.std()
    coef_variacao = desvio_padrao / foo.mean()
    assimetria = foo.skew()
    curtose = foo.kurtosis()

    return {
        'avg': avg,
        'median': median,
        'mode': mode,
        'quartil': quartil,
        'amplitude': amplitude,
        'variancia': variancia,
        'desvio_padrao': desvio_padrao,
        'coef_variacao': coef_variacao,
        'assimetria': assimetria,
        'curtose': curtose
    }

# Separando os dados por tipo de produto
df_hairstyle = df_product[df_product['Product type'] == 'haircare'].copy()
df_skin_care = df_product[df_product['Product type'] == 'skincare'].copy()
df_cosmetics = df_product[df_product['Product type'] == 'cosmetics'].copy()

# Aplicando a função e adicionando as novas colunas
for df in [df_hairstyle, df_skin_care, df_cosmetics]:
    stats = cent_stats(df['Price'])
    for stat_name, stat_value in stats.items():
        df[stat_name] = stat_value

# Exibindo os DataFrames resultantes (opcional)
print(df_hairstyle.head())
print(df_skin_care.head())
print(df_cosmetics.head())

# Retornando os DataFrames modificados
df_hairstyle, df_skin_care, df_cosmetics
