import pandas as pd

#Lendo a base de dados com o pandas, em csv
#Base de salarios nas áreas de dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
#Le a base inteira
df.head()
#Visualiza os detalhes da base de dados
#df.info()
#Descrição mais aprofundada (mostra mais sobre dados numericos)
#df.describe()
#Quantidade de linhas e colunas (dimenssao)
df.shape

linhas, colunas = df.shape[0], df.shape[1]

df.columns

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

desc = df.describe(include='object')

print(desc)

# print('Linhas: ', linhas)
# print('Colunas: ', colunas)