#Limpeza e preparação de dados
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

#ler a base
leitura = df.head()

#Verifica se existem colunas nulas
valor_nulo = df.isnull()

#mostra a quantidade de valores nulos
soma = df.isnull().sum()

#valores unicos
unico = df['work_year'].unique()

#exibir linhas com nan
nan = df[df.isnull().any(axis=1)]

#excluir os valores nulos
df_limpo = df.dropna()
limpo = df_limpo.isnull().sum()
data = df_limpo.head()
info = df_limpo.info()
#transforma o tipo da coluna para inteiro, pois estava em float64
transformar = df_limpo = df_limpo.assign(work_year = df_limpo['work_year'].astype('int64'))
info2 = df_limpo.info()

print(transformar)

#---------------------------------------------------------------------------------------------------------------------
#Criando um dataframe
df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})

#preenchendo os valores nulos com as medias do salario arredondando
media = df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

#mediana
mediana = df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

#print(df_salarios)

df_temperatura = pd.DataFrame({
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

ffill = df_temperatura['preenchimento_ffill'] = df_temperatura['temperatura'].ffill()

bfill = df_temperatura['preenchimento_bfill'] = df_temperatura['temperatura'].bfill()

#print(df_temperatura)

df_cidades = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'Cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']
})
#substituir por um valor fixo
df_cidades['cidade_preenchida'] = df_cidades['Cidade'].fillna('Não informado')

#print(df_cidades)