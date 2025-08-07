import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head()

renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

#atribuindo as alterações as colunas da base (renomear)
df.rename(columns=renomear_colunas, inplace=True)

#calcula a frequencia de uma categoria
frequencia = df['senioridade'].value_counts()

tipo_contrato = df['cargo'].value_counts()

remoto = df['remoto'].value_counts()

tamanho_empresa = df['tamanho_empresa'].value_counts()

substituir_senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df['senioridade'] = df['senioridade'].replace(substituir_senioridade)
nova_senioridade = df['senioridade'].value_counts()

contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Tempo Parcial',
    'FL': 'Freela',
    'CT': 'Contrato'
}
df['contrato'] = df['contrato'].replace(contrato)
nova_coluna_contrato = df['contrato'].value_counts()

tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Media',
    'L': 'Grande'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
nova_coluna_tam_empresa = df['tamanho_empresa'].value_counts()

remoto = {
    0: 'Presencial',
    50: 'Hibrido',
    100: 'Remoto'
}
df['remoto'] = df['remoto'] = df['remoto'].replace(remoto)
novo_remoto = df['remoto'].value_counts()

df_limpo = df.dropna()
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('int64'))

#Pltando gráficos
df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de Senioridade')
#exibe o grafico
plt.xlabel('Senioridade')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()

#Grafico com Saborn
plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd') 
plt.title('Media Mensal de Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salario Médio Anual (USD)')
plt.tight_layout()
plt.show()

ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
plt.title("Média Mensal de Senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário Médio Anual (USD)")
plt.tight_layout()
plt.show()

#Histograma
plt.figure(figsize=(10, 5))
sns.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title('Distribuição dos Salários Anuais')
plt.xlabel('Salário em USD')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

#BoxPLOT
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['usd'])
plt.title('Boxplot Salário')
plt.xlabel('Salário em USD')
plt.tight_layout()
plt.show()

ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']

plt.figure(figsize=(8, 5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.title('Distiubuição por Senioridade')
plt.xlabel('Salário em USD')
plt.tight_layout()
plt.show()

#Gráficos Interativos
senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()
fig = px.bar(senioridade_media_salario,
             x='senioridade',
             y='usd',
             title='Média Salarial por Senioridade',
             labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})
fig.show()

#Grafico de pizza
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos Tipos de Trabalho',
            )
fig.show()

#Grafico de rosca
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos Tipos de Trabalho',
             hole=0.5
            )
fig.update_traces(textinfo='percent+label')
fig.show()

