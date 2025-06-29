#!/usr/bin/env python
# coding: utf-8

# # Insights sobre os prestadores de serviço turístico (Restaurantes, Cafeterias e Bares) com situação regular no ano de 2023.
Uma instituição financeira pretende disponibilizar uma linha de crédito diferenciada para estabelecimentos que pertencem ao grupo de atividade econômica referente a serviços de alimentação. Visando entender com mais profundidade o setor, foi determinado que se realizasse uma análise preliminar sobre os dados disponibilizados pelo Governo Federal.

Esse projeto tem por objetivo realizar uma análise descritiva a fim de se obter insights de um conjunto de dados que trata do cadastro de pessoas físicas e jurídicas que atuam no setor de turismo, específicamente referente a restaurantes, cafeterias e bares com situação ativa no ano de 2023 no Brasil.

Esse dataset traz informações sobre os serviços de alimentação (alimentos e bebidas) que atuam na cadeia produtiva do turismo. Entram nessa modalidade os restaurantes, cafeterias, bares, churrascarias, sorveterias, casas de suco, casas de chá, pizzarias, pastelarias, entre outros, segundo a Lei nº 11.771, de 17 de setembro de 2008, e Decreto nº 7.381, de 2 de dezembro de 2010.

O desenvolvimento desse projeto segue as seguintes etapas:

1. Preparação dos dados
2. Análise univariada
3. Análise bivariada
4. Visualização de dados
5. Resumo e interpretação

Algumas questões iniciais podem ser levantadas a fim de nortear o trabalho e que serão testadas ao longo do projeto. No entanto, outras podem ser verificadas durante a análise exploratória dos dados. As questões são:

1. Quais estados têm a maior concentração de estabelecimentos cadastrados?
2. Qual é a proporção de estabelecimentos em relação ao seu tipo?
3. Quais são as especialidades predominantes?
# # Importando as bibliotecas

# In[378]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

get_ipython().system('pip install xlrd')
#Colocar demais bibliotecas
#Colocar palheta de cores


# # Entendendo os dados

# In[379]:


df1 = pd.read_excel('dados_csv/restaurante-bares-cafeterias-e-similares(1).xls.')
df2 = pd.read_excel('dados_csv/restaurante-cafeteria-bar-e-similares (2).xls')
df3 = pd.read_excel('dados_csv/restaurante-cafeteria-bar-e-similares (3).xls')
df4 = pd.read_excel('dados_csv/restaurante-cafeteria-bar-e-similares(4).xls')


# In[380]:


# Existe diferença entre os colunas dos Datafrmaes? 

def compara():
    colunas = [df1.columns, df2.columns, df3.columns, df4.columns]
    posicao_rigida = 0
    while posicao_rigida <= 2:
        posicao = 3
        while posicao != posicao_rigida:
            print(f"As colunas do df{posicao_rigida + 1} comparadas com as colunas do df{posicao + 1} é igual a {colunas[posicao_rigida].equals(colunas[posicao])}" )
            print('---------------------------------------------------------------------')
            posicao -= 1
        posicao_rigida += 1
        
compara()


# In[381]:


# Podemos observar que apenas os dataframes 3 e 4 são iguais 


# In[382]:


df1.columns


# In[383]:


df2.columns


# In[384]:


df3.columns


# In[385]:


df4.columns


# In[386]:


#Podemos reparar que em relação ao df1, os df3 e df4 possuem todas as colunas e na mesma ordem com a exceção da coluna 'porte'
# O df2 não possui a coluna 'Atividade Turística',
# O df2 possui as colunas 'CNAE(S) relacionados à atividade' e 'Unnamed: 18' não presente nos demais dataframes


# In[387]:


# concatenando
df = pd.concat([df1,df2,df3,df4])


# In[388]:


df.head(5)


# # Dicionário de dados
1. Atividade Turística: Resume-se aos restaurantes, cafeterias, bares e similares.
2. Número de Inscrição do CNPJ: Cadastro Nacional da Pessoa Jurídica.
3. Nome Fantasia: nome popular de uma empresa, ou seja, como ela é conhecida pelo público.
4. Tipo de Estabelecimento: Se o cadastro pertence à matriz ou à filial.
5. Natureza Jurídica: regime jurídico que define a estrutura de uma empresa, ou seja, como ela será reconhecida perante a lei (Sociedade Empresarial Limitada, etc.).
6. Porte: tamanho do negócio, com base em dados financeiros e de capacidade produtiva.
7. Endereço Completo Receita Federal: endereço cadastrado na Receita Federal.
8. UF: estado de atuação de cada número de inscrição.
9. Município: município de atuação de cada número de inscrição.
10. Data de Abertura: data de abertura do estabelecimento.
11. Telefone Comercial.
12. E-mail Comercial.
13. Website.
14. Número do Certificado: para cada estabelecimento é atribuído um certificado do qual está atrelado um número.
15. Validade do Certificado: cada certificado tem um prazo determinado de validade, necessitando de sua renovação.
16. Idiomas: alguns estabelecimentos oferecem atendimento em mais de um idioma.
# # Limpeza e manipulação
Ao olhar para o dataframe, é possível perceber que algumas colunas não serão necessárias para o desenvolvimento do projeto, pois não contêm informações relevantes para essa finalidade. As colunas ["Atividade Turística", "Número de Inscrição do CNPJ", "Endereço Completo Receita Federal", "Telefone Comercial", "E-mail Comercial", "CNAE(S) relacionados à atividade", "Website" e "Número do Certificado"] serão retiradas por não trazerem peso significativo.

Etapa: Análise Exploratória

Como se trata de dados trimestrais, devemos verificar se a mesma empresa que esteja presente nos dataframes anteriores ao df4 renovou ou não seus contratos e novas empresas incluídas. Também será verificado se existe duplicidade de linhas ou dados faltantes.

As colunas ("Data de Abertura" e "Validade do Certificado") são importantes e apresentam o formato de data que precisa ser formatado antes de ser realizada a visualização dos dados.
# In[389]:


df.head(5)


# In[390]:


#Retirando colunas
#Arrumar nome melhor para o df_um
df_um = df.drop(['Atividade Turística', 'Endereço Completo Receita Federal', 'CNAE(S) relacionados à atividade', 'Telefone Comercial', 'E-mail Comercial', 'Website', 'Número do Certificado'], axis=1)


# In[391]:


print(df_um['Unnamed: 18'].isnull().sum())


# In[392]:


# podemos comprovar que a coluna não nomeada ('Unnamed: 18') é desnecessária, por isso também vamos remove-la.
df_um = df_um.drop(['Unnamed: 18'], axis=1)


# In[393]:


df_um.describe()


# In[394]:


#Verificando dados faltantes
faltantes = df_um.isnull().sum()
print(faltantes)


# In[395]:


#Verificando se existe duplicidades
duplicados = df_um.duplicated().sum()
print(duplicados)

. Visando manter a qualidade do dataframe e pensando na etapa da analise explorátoria dos dados, alguns questionamentos devem ser feitos e ações devem ser tomadas. 

. O dataframe tem 20761 dados duplicados que deverão ser removidos. 

. Temos a coluna 'porte' que pode ser relevante, porém possui 53130 dados faltantes, qual seria a melhor forma de preencher esses dados sem que o dataframe perca em qualidade de informação? Deve-se considerar que esse número devera cair depois da remoção das linhas duplicadas. Tmbém sera necessario transformar essa variavel categorica? 

. A coluna idiomas não apresenta dados faltantes por informações ausentes estarem preenchidas apenas com '-'. Devemos descobrir quantos dados realmente faltam nessa coluna. 

. Datas da coluna 'Validade do Certificado' devem ser ajsutadas.

. Não deveremos retirar os números de inscrição vencidos, pois esses dados podem ser importantes para análises de tendências e padrões de renovação. Também podem ser útil para identificar empresas que renovaram sua inscrição após o vencimento (número de empresas regulares x irregulares). 

. Existem números de inscrição iguais? Se sim isso pode significar que as empresas renovaram sua inscrição, também abre a possibilidade para criação de uma nova coluna indicando renovação de inscrição. 
# In[396]:


#Removendo as duplicadas
df_um = df_um.drop_duplicates()
df_dois = df_um.copy(deep=True)


# In[397]:


df_dois.shape


# In[398]:


df_dois.head(5)


# In[399]:


faltantes = df_dois.isnull().sum()
print(faltantes)


# In[400]:


#Verificando o tipo de dado da coluna 'Validade do Certificado'
print(type(df_dois['Validade do Certificado'].iloc[0]))
print(df_dois['Validade do Certificado'].dtype)

#Convertendo a coluna para datetime
df_dois['Validade do Certificado'] = pd.to_datetime(df_dois['Validade do Certificado'], errors='coerce')


# In[401]:


df_dois['Validade do Certificado'] = df_dois['Validade do Certificado'].dt.date


# In[402]:


#ATENÇÃO COLUNA 'Validade do Certificado' TRATADA


# In[403]:


unicos_idiomas = df_dois['Idiomas'].unique()
print(unicos_idiomas)


# In[404]:


#confirmando o tipod e dados presente na séries
print(type(df_dois['Idiomas'].iloc[0]))

#contando a ocorrência de "-" presentes na coluna
total_registros = df_dois['Idiomas'].size
total_faltantes = df_dois['Idiomas'].str.count('-').sum()
total_preenchidas = df_dois['Idiomas'].size - df_dois['Idiomas'].str.count('-').sum()
percentual = round((total_faltantes) * 100/ (total_registros),2)

print(f"quantidade total de registros - {total_registros}")
print(f"quantidade de registros faltantes - {total_faltantes}")
print(f"quantidade de registros preenchidos - {total_preenchidas}")
print(f"percentual de registros não preenchidos {percentual}%")

A coluna Idiomas aparentemente não possuiu dados ausentes, porém quando levamos em consideração o caracter "-", percebemos
que existem 65178 linhas com informação não preenchida. Pela quantidade de dados que faltam, também por aparentemente não ser uma informação tão relevante para a analise, já que a coluna ' Especialidade' também pode refletir na língua e na cultura de origem do restaurante, optei por retira-la.
# In[405]:


df_dois = df_dois.drop(['Idiomas'], axis=1)


# In[406]:


#Verificando se existem números de inscrição iguais
df_dois['Número de Inscrição do CNPJ'].duplicated().sum()


# In[407]:


#Eliminando registros com números de inscrições e Validade do Certificado
#Esses registros precisam ser eliminados, pois indicam uma duplicidade de informação que provavelmente não foi retirada
#devido a forma diferentes que as demais colunas foram preenchidas ao longos dos demais trimestres
df_dois = df_dois.drop_duplicates(subset=['Número de Inscrição do CNPJ','Validade do Certificado'])
df_dois.shape


# In[408]:


#Descobrindo os valores únicos da coluna 'porte'
#Para as empresas descritas como 'DEMAIS', iremos adotar que podem ser de médio ou grande porte
unicos_porte = df_dois['Porte'].unique()
print(unicos_porte)


# In[409]:


#Descobrindo o tipo de dado da coluna 'Porte'
tipo_de_dado = df_dois['Porte'].dtypes
print(type(df_dois['Porte'].iloc[0]))
print(tipo_de_dado)


# In[410]:


df_dois['Porte'] = df_dois['Porte'].map(
    { 'MICROEMPRESA': 'MICROEMPRESA', 'EMPRESA DE PEQUENO PORTE': 'PEQUENO PORTE', 'DEMAIS': 'MÉDIO E GRANDE' })

#Alterando para númerico para depois realizar a conversão dos dados categoricos 



# In[411]:


df_dois['Porte'].value_counts()


# In[412]:


#Agora podemos empregar algum metodo para preencher a coluna port_num
contagem_port_num = df_dois['Porte'].value_counts()
soma_faltantes = df_dois['Porte'].isna().sum()
total = len(df_dois['Porte'])
frequencia = df_dois['Porte'].value_counts(normalize=True)
print(f"Total  {total}")
print('--------------------------')
print(f"Nulos  {soma_faltantes}")
print('--------------------------')
print('Contagem de linhas preenchidas')
print(contagem_port_num)
print('--------------------------')
print("Frequência relativa")
print(f"{frequencia.apply(lambda x: f'{x * 100:.2f}%')}")


# In[413]:


#Preenchendo os dados faltantes com imputação aleatória baseada nas proporções observadas
np.random.seed(42)
faltantes = df_dois['Porte'].isna()
df_dois.loc[faltantes,'Porte'] = np.random.choice(frequencia.index, size=faltantes.sum(), p=frequencia.values)
print('Contagem de linhas preenchidas')
print(contagem_port_num)
print("Frequência relativa")
print(f"{frequencia.apply(lambda x: f'{x * 100:.2f}%')}")


# In[414]:


contagem_port_num = df_dois['Porte'].value_counts()
soma_faltantes = df_dois['Porte'].isna().sum()
total = len(df_dois['Porte'])
frequencia = df_dois['Porte'].value_counts(normalize=True).sort_index()
print(f"Total  {total}")
print('--------------------------')
print(f"Nulos  {soma_faltantes}")
print('--------------------------')
print('Contagem de linhas preenchidas')
print(contagem_port_num)
print('--------------------------')
print("Frequência relativa")
print(f"{frequencia.apply(lambda x: f'{x * 100:.2f}%')}")


# In[415]:


#Vamos criar uma coluna chamada "Validade"
#Pelo fato dos Dados terem como referência o ano de 2023, vamos considerar que para uma data inferior a dezembro do
#referido ano o cadastro esteja vencido atribuindo o número 0, caso contrário atrubiremos 1.
df_dois['Validade do Certificado'] = pd.to_datetime(df_dois['Validade do Certificado'], errors='coerce')
data_comparacao = pd.to_datetime('2023-12-31')
df_dois['Validade 2023-12-31'] = (df_dois['Validade do Certificado'] >= data_comparacao).astype(int)


# In[416]:


df_dois['Ano de Abertura'] = df_dois['Data de Abertura'].dt.year


# In[417]:


#Retirando as demais colunas desnecessarias
df_dois = df_dois.drop(['Número de Inscrição do CNPJ','Validade do Certificado','Data de Abertura'], axis=1)


# In[418]:


df_dois.head(5)


# # Analise exploratória 

# In[419]:


# Verificando a atividade pelo tipo de estabelecimento

plt.figure(figsize=(6,3))
frequencia_tipo = df_dois['Tipo de Estabelecimento'].value_counts(normalize=True)*10000
plt.bar(frequencia_tipo.index, frequencia_tipo.values, width=0.7)  # Diminui o valor do width
plt.title('Proporção de matrizes e filiais')
plt.xlabel('Tipo de Estabelecimento')
plt.ylabel('Quantidade')
plt.xticks(frequencia_tipo.index)
plt.yticks()

plt.gca().spines['top'].set_visible(False)  # Retirar o contorno superior
plt.gca().spines['right'].set_visible(False)  # Retirar o contorno direito

plt.show()


# In[420]:


# Verificando o porte das empresas


plt.figure(figsize=(6, 3))
frequencia = frequencia.sort_values(ascending=False)*100  # Ordenar a série por índice
plt.bar(frequencia.index, frequencia.values, width=0.7)
plt.title('Proporção de empresas pelo seu porte')
plt.xlabel('Tamanho da empresa')
plt.ylabel('Quantidade')
plt.xticks(frequencia.index)

plt.gca().spines['top'].set_visible(False)  # Retirar o contorno superior
plt.gca().spines['right'].set_visible(False)  # Retirar o contorno direito


plt.show()


# In[421]:


frequencia_natureza = df_dois['Natureza Jurídica'].value_counts(normalize=True)*100
print(frequencia_natureza.round(3))


# In[422]:


#Vamos ter que fazer um tratamento nos dados dessa coluna
#primeiramente vamos unificar os registros da Empresário Individual que contém a mesma informação
df_dois['Natureza Jurídica'] = df_dois['Natureza Jurídica'].replace('Empresário (Individual)', 'Empresário Individual')
frequencia_natureza = df_dois['Natureza Jurídica'].value_counts(normalize=True)*100
print(frequencia_natureza.round(3))


# In[423]:


# Agora vamos retirar as categorias que não possuem valor significativo para o estudo
#Sociedade Simples Limitada, Cooperativa, Serviço Social Autônomo, Sociedade Simples Pura,
#Empresa Individual de Responsabilidade Limitada (de Natureza Simples),                                                                   

df_dois = df_dois.drop(df_dois[df_dois['Natureza Jurídica'] == 'Sociedade Simples Limitada'].index)
df_dois = df_dois.drop(df_dois[df_dois['Natureza Jurídica'] == 'Cooperativa'].index)
df_dois = df_dois.drop(df_dois[df_dois['Natureza Jurídica'] == 'Serviço Social Autônomo'].index)
df_dois = df_dois.drop(df_dois[df_dois['Natureza Jurídica'] == 'Sociedade Simples Pura'].index)
df_dois = df_dois.drop(df_dois[df_dois['Natureza Jurídica'] == 'Empresa Individual de Responsabilidade Limitada (de Natureza Simples)'].index)


# In[424]:


frequencia_natureza = df_dois['Natureza Jurídica'].value_counts(normalize=True)*100
print(frequencia_natureza.round(3))


# In[425]:


df_dois['Natureza Jurídica'] = df_dois['Natureza Jurídica'].replace('Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)', 'Empresa Individual de Responsabilidade Limitada')
frequencia_natureza = df_dois['Natureza Jurídica'].value_counts(normalize=True)*100
print(frequencia_natureza.round(3))


# In[426]:


# Verificando a proporção em relação a Natureza Jurídica


frequencia_natureza = df_dois['Natureza Jurídica'].value_counts(ascending=True)
frequencia_natureza.plot(kind='barh')

# Adicionar título e rótulos

plt.title('Distribuição em relação a natureza jurídica')
plt.xlabel('Frequência')
plt.ylabel('Categoria')
#plt.gca().yaxis.tick_right()
plt.yticks([])
plt.gca().spines['top'].set_visible(False)  # Retirar o contorno superior
plt.gca().spines['right'].set_visible(False)  # Retirar o contorno direito
#plt.gca().spines['bottom'].set_visible(False)  # Retirar o contorno inferior
plt.gca().spines['left'].set_visible(False)  # Retirar o contorno esquerdo
for i, (nome, valor) in enumerate(frequencia_natureza.items()):
    plt.annotate(nome, (valor, i), xytext=(10, 0), textcoords='offset points', ha='left')

plt.show()


# In[427]:


# Verificando a concetralção em relação aos estados

frequencia_estados = df_dois['UF'].value_counts(ascending=False)
plt.figure(figsize=(10,3))
plt.bar(frequencia_estados.index, frequencia_estados.values, width=0.6)
plt.title('Proporção de empresas por estado')
plt.xlabel('Estado')
plt.ylabel('Proporção')
plt.xticks(frequencia_estados.index)
plt.gca().spines['top'].set_visible(False)  # Retirar o contorno superior
plt.gca().spines['right'].set_visible(False)  # Retirar o contorno direito
plt.yticks()
plt.show()


# In[428]:


# Talvez fosse melhor criar uma coluna e observar esse comportamente em relação as regiões do Brasil do que por estado

regioes = {
    'Sudeste': ['SP', 'RJ', 'MG', 'ES'],
    'Sul': ['PR', 'SC', 'RS'],
    'Norte': ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO'],
    'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Centro-Oeste': ['DF', 'GO', 'MT', 'MS']
}

def converte_regiao(UF):
    for regiao, estados in regioes.items():
        if UF in estados:
            return regiao
    return np.nan

df_dois['Regiões'] = df_dois['UF'].apply(converte_regiao)


# In[429]:


df_dois.head(5)


# In[430]:


# Realizando um novo gráfico para as concentração da atividade gastronomica em relação as regiões

frequencia_regioes = df_dois['Regiões'].value_counts(ascending=True)

frequencia_regioes.plot(kind='barh', figsize=(6, 3.5))

# Adicionar título e rótulos

plt.title('Distribuição das empresas por região')
plt.xlabel('Proporção')
plt.ylabel('Região')
#plt.gca().yaxis.tick_right()
plt.yticks([])
plt.gca().spines['top'].set_visible(False)  # Retirar o contorno superior
plt.gca().spines['right'].set_visible(False)  # Retirar o contorno direito
#plt.gca().spines['bottom'].set_visible(False)  # Retirar o contorno inferior
plt.gca().spines['left'].set_visible(False)  # Retirar o contorno esquerdo
for i, (nome, valor) in enumerate(frequencia_regioes.items()):
    plt.annotate(nome, (valor, i), xytext=(10, 0), textcoords='offset points', ha='left')

plt.show()


# In[431]:


frequencia_tipo = df_dois['Tipo'].value_counts(ascending=True)
print(frequencia_tipo)


# In[432]:


df_dois = df_dois[~df_dois['Tipo'].isin(['092.821.516-46','-'])]


# In[433]:


frequencia_tipo = df_dois['Tipo'].value_counts(ascending=True)
frequencia_tipo.plot(kind='barh', figsize=(6, 4))

# Adicionar título e rótulos

plt.title('Distribuição das empresas por tipo de estabelecimento')
plt.xlabel('Proporção')
plt.ylabel('Tipo de estabelecimento')
#plt.gca().yaxis.tick_right()
plt.yticks([])
plt.gca().spines['top'].set_visible(False)  # Retirar o contorno superior
plt.gca().spines['right'].set_visible(False)  # Retirar o contorno direito
#plt.gca().spines['bottom'].set_visible(False)  # Retirar o contorno inferior
plt.gca().spines['left'].set_visible(False)  # Retirar o contorno esquerdo
for i, (nome, valor) in enumerate(frequencia_tipo.items()):
    plt.annotate(nome, (valor, i), xytext=(10, 0), textcoords='offset points', ha='left')

plt.show()


# In[434]:


# Analise em relação a validade

frequencia_validade = df_dois['Validade 2023-12-31'].value_counts()
frequencia_validade = frequencia_validade.sort_values(ascending=False)
plt.figure(figsize=(6, 3))

plt.bar(frequencia_validade.index, frequencia_validade.values, width=0.7)
plt.title('Proporção de empresas em relação ao certificado de atuação')
plt.xlabel('Validade')
plt.ylabel('Proporção')
plt.xticks(frequencia_validade.index)

plt.gca().spines['top'].set_visible(False)  # Retirar o contorno superior
plt.gca().spines['right'].set_visible(False)  # Retirar o contorno direito

plt.show()


# In[435]:


#Ano de Abertura

df_dois['Ano de Abertura'].hist(bins=10, figsize=(6, 4))
plt.title('Quantidade de empresas ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('Frequência')
plt.show()


# A quantidade de matrizes é muito superior à de filiais, o que indica que a maioria das empresas nesse ramo de atividade não expande para filiais. Talvez seja uma oportunidade de negócios fornecer crédito para que essas empresas possam expandir seus negócios, abrindo outras filiais ou franquias.
# 
# A maior parte dos estabelecimentos é constituída por microempresas, seguidas por empresas de médio e grande porte. Isso explica a grande quantidade de estabelecimentos com uma única unidade (matriz). Seria interessante o fornecimento de crédito para o microempreendedor.
# 
# Podemos ver que as duas categorias que predominam quanto à sua natureza jurídica são Sociedade Empresária Limitada e Empresário Individual. A primeira corresponde a uma empresa que possui um número limitado de sócios, cuja dívida individual não ultrapassa o valor de sua participação. Já a segunda corresponde ao tipo de empresa cujo proprietário é uma única pessoa. Esse tipo de participação no mercado vai de encontro com a ideia de que uma grande fatia do mercado é constituída por microempresas. Poderia ser criada uma linha de crédito correspondente a esses dois tipos de perfis empresariais.
# 
# Quanto aos estados, toda a região Sudeste possui uma boa representatividade no setor, com exceção do Espírito Santo, e São Paulo é o estado com maior atividade em todo o Brasil. Os estados da região Sul possuem uma boa representatividade no setor, apresentando uma proporção equilibrada. Os estados da região Norte não possuem uma boa representatividade. No Nordeste, os estados de Alagoas, Bahia e Ceará são aqueles que elevam o nível de atividade nessa região do país, talvez por serem mais turísticos que os demais. Na região Centro-Oeste, o estado de Goiás eleva o nível de atividade na região.
# 
# Ao observar a proporção de empresas por estados e posteriormente as regiões, conseguimos observar que, embora a região Nordeste seja a segunda maior em atividade, podemos perceber que isso se deve ao bom desempenho dos estados de Alagoas, Bahia e Ceará e pela quantidade de estados que a região possui. Porém, a região Sul consegue manter um terceiro lugar em nível de atividade, mesmo possuindo apenas 4 estados, o que nos leva a crer que seja uma região muito mais interessante de se observar para esse propósito.
# 
# Os restaurantes são o tipo de estabelecimento predominante, seguidos de estabelecimentos reconhecidos como similares (lanchonetes, quiosques, etc.). Uma pequena parcela trabalha com a validade do certificado já vencida. Quantos desses são microempreendedores? Em qual região se concentra a maior parcela de certificados vencidos? Será que valeria a pena uma linha de crédito para que essas pessoas se regularizem?. A seguir realizaremos uma nalise bivariada para responder tais questionamentos
# 
# 
# 

# # Analise Bivariada

# In[436]:


#Vamos criar uma matriz de correlação para estudar o relacionamento entre as variaveis
#Para isso deveremos fazer mais algumas alterações no Dataset

#Retirando a coluna Nome Fantasia
df_dois = df_dois.drop(['Nome Fantasia'], axis=1)


# In[437]:


df_tres = df_dois.copy()


# In[438]:


df_dois.head(5)


# In[439]:


#Atribuindo valores númericos para representar as categorias na coluna Tipo de Estabelecimento	

df_tres['Tipo de Estabelecimento'] = df_tres['Tipo de Estabelecimento'].map({
    'Matriz':0,
    'Filial':1
})


# In[440]:


df_tres['Natureza Jurídica'] = df_tres['Natureza Jurídica'].map({
    'Sociedade Empresária Limitada':0,
    'Empresário Individual':1,
    'Empresa Individual de Responsabilidade Limitada':2,
    'Sociedade Anônima Aberta':3,
    'Sociedade Anônima Fechada':4
})


# In[441]:


df_tres['Porte'] = df_tres['Porte'].map({
    'MICROEMPRESA':0,
    'PEQUENO PORTE':1,
    'MÉDIO E GRANDE':2
})


# In[442]:


##Atribuindo valores númericos para representar as categorias na coluna 'UF', mediante aos padrões determinados pelo IBGE
df_tres['UF'] = df_tres['UF'].map({
    'SP':35,
    'RJ':33,
    'SC':42,
    'AL':27,
    'MG':31,
    'GO':52,
    'PR':41,
    'RS':43,
    'BA':29,
    'PA':15,
    'CE':23,
    'ES':32,
    'DF':53,
    'PE':26,
    'RN':24,
    'AM':13,
    'PB':24,
    'TO':17,
    'MT':51,
    'MA':21,
    'PI':21,
    'MS':50,
    'SE':28,
    'AC':12,
    'RO':11,
    'AP':16,
    'RR':14
})


# In[443]:


df_tres['Tipo'] = df_tres['Tipo'].map({
    'Restaurante':0,
    'Similar':1,
    'Bar':2,
    'Cafeteria':3
})


# In[444]:


df_tres['Regiões'] = df_tres['Regiões'].map({
    'Sudeste':0,
    'Nordeste':1,
    'Sul':2,
    'Centro-Oeste':3,
    'Norte':4
})


# In[445]:


df_tres['Município'].unique().sum()


# In[446]:


df_tres['Especialidade'].unique().sum()


# In[447]:


# Por possuir muitos valores unicos a coluna 'Município' e 'Especialidade' serão retirada afim de melhorr a interpretação dos dados
#Uma vez que as colunas UF e Região ja podem trazer muito fda informação necessaria.

df_tres = df_tres.drop(['Município','Especialidade'], axis=1)


# In[448]:


df_tres.head(5)


# In[449]:


correlacao = df_tres.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlacao, annot=True, cmap='coolwarm')


# In[450]:


#Correlações muito fortes (Tipo de estabelecimento x Regiões, Porte x Regiões, Porte x Tipo)
#Correlações fortes (Tipo de estabelecimento x Tipo, Natureza Juridica x UF, UF X Validade
# UF x Ano de abertura, tipo x validde, ano de abertura x porte)


# In[451]:


ordem_regioes = df_dois[df_dois['Tipo de Estabelecimento'] == 'Matriz']['Regiões'].value_counts().index

plt.figure(figsize=(6, 4))
sns.countplot(x='Regiões', hue='Tipo de Estabelecimento', data=df_dois, order=ordem_regioes)

# Adicione título e rótulos
plt.title('Distribuição de matrizes e filiais por Região')
plt.xlabel('Região')
plt.ylabel('Contagem')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


# In[452]:


df_tres['Porte'].value_counts()


# In[ ]:





# In[453]:


#porte_regioes = df_tres[df_tres['Porte'] = 'MICROEMPRESA']['Regiões'].value_counts()
#ordem_porte = porte_regioes.index

ordem_regioes = df_dois.groupby('Regiões')['Porte'].count().sort_values(ascending=True).index

# Reindexa os arrays
pequena = df_dois[(df_dois['Porte'] == 'MICROEMPRESA')].groupby('Regiões')['Porte'].count().reindex(ordem_regioes, fill_value=0)
media = df_dois[(df_dois['Porte'] == 'MÉDIO E GRANDE')].groupby('Regiões')['Porte'].count().reindex(ordem_regioes, fill_value=0)
grande = df_dois[(df_dois['Porte'] == 'PEQUENO PORTE')].groupby('Regiões')['Porte'].count().reindex(ordem_regioes, fill_value=0)

# Cria o gráfico
fig, ax = plt.subplots(figsize=(6, 4))
bar1 = ax.barh(ordem_regioes, pequena.values, label='MICROEMPRESA')
bar2 = ax.barh(ordem_regioes, media.values, left=pequena.values, label='MÉDIO E GRANDE')
bar3 = ax.barh(ordem_regioes, grande.values, left=[i + j for i, j in zip(pequena.values, media.values)], label='PEQUENO PORTE')

#ax.set_title('Distribuição das empresas por região e porte', fontsize=14, fontweight='bold', color='black')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend([bar1, bar2, bar3], ['MICROEMPRESA', 'MÉDIO E GRANDE', 'PEQUENO PORTE'], loc='center left', bbox_to_anchor=(0.0, 1.1), ncol=3, borderaxespad=0)


# Criada a matriz de correlação, vamos estudar o relacionamento entre as variaveis que possuam uma forte correlação 

# In[454]:


ordem_tipo = df_dois.groupby('Tipo')['Porte'].count().sort_values(ascending=True).index

microempresa = df_dois[df_dois['Porte'] == 'MICROEMPRESA'].groupby('Tipo')['Porte'].count().reindex(ordem_tipo, fill_value=0)
pequena = df_dois[df_dois['Porte'] == 'PEQUENO PORTE'].groupby('Tipo')['Porte'].count().reindex(ordem_tipo, fill_value=0)
demais = df_dois[df_dois['Porte'] == 'MÉDIO E GRANDE'].groupby('Tipo')['Porte'].count().reindex(ordem_tipo, fill_value=0)


fig, ax = plt.subplots(figsize=(6, 4))
bar1 = ax.barh(ordem_tipo, microempresa.values, label='MICROEMPRESA')
bar2 = ax.barh(ordem_tipo, demais.values, left=microempresa.values + pequena.values, label='MÉDIO E GRANDE')
bar3 = ax.barh(ordem_tipo, pequena.values, left=microempresa.values, label='PEQUENO PORTE')

plt.xlabel('Quantidade de Empresas')
plt.ylabel('Tipo de estabelecimento')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend([bar1, bar3, bar2], ['MICROEMPRESA', 'PEQUENO PORTE', 'MÉDIO E GRANDE'], loc='center left', bbox_to_anchor=(0.0, 1.1), ncol=3, borderaxespad=0)


# Reindexa os arrays


# In[455]:


df_dois.head(5)


# In[456]:


#Tipo de estabelecimento x Tipo


ordem_tipo = df_dois.groupby('Tipo')['Tipo de Estabelecimento'].count().sort_values(ascending=False).index

plt.figure(figsize=(6, 4))
sns.countplot(x='Tipo', hue='Tipo de Estabelecimento', data=df_dois, order=ordem_tipo)

# Adicione título e rótulos
plt.title('Distribuição do tipo de estabelecimento em relação a estrutura')
plt.xlabel('Tipo de Estabelecimento')
plt.ylabel('Contagem')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


# In[457]:


#Natureza Juridica x Região



plt.figure(figsize=(16, 14))
#df_dois.groupby('Região')['Natureza Jurídica'].value_counts().unstack().plot(kind='bar', stacked=True, width=0.8)
df_dois.groupby('Regiões')['Natureza Jurídica'].value_counts().unstack().plot(kind='bar', width=0.8)
plt.title('Distribuição das Categorias de Natureza Jurídica por Região')
plt.xlabel('Região')
plt.xticks(rotation=0)
plt.ylabel('Contagem')
plt.legend(title='Natureza Jurídica')

plt.legend(title='Natureza Jurídica', loc='upper left', bbox_to_anchor=(1, 1))
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)



plt.show()


# In[458]:


#Validade x Regiões

pivot_table = df_dois.pivot_table(index='Regiões', columns='Validade 2023-12-31', aggfunc='size', fill_value=0)

# Ordene a tabela pivot com base nos valores da coluna "1" em ordem decrescente
pivot_table = pivot_table.sort_values(by=1, ascending=False)

# Reverta a ordem das colunas da tabela pivot
pivot_table = pivot_table[[1, 0]]

# Crie um gráfico de barras
pivot_table.plot(kind='bar', width=0.8)


# Adicione título e rótulos
plt.title('Distribuição de estabelecimentos por região conforme o prazo de validade do certificado')
plt.xlabel('Região')
plt.xticks(rotation=0)
plt.ylabel('Contagem')

plt.legend(labels=['Válido', 'Vencido'])


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


# Exiba o gráfico
plt.show()



# In[ ]:





# In[459]:


#Região x Ano de abertura

# Crie uma figura com 5 subplots
fig, axs = plt.subplots(1, 5, figsize=(18, 6))

# Para cada região um gráfico de caixa
for i, regiões in enumerate(df_dois['Regiões'].unique()):
    axs[i].boxplot(df_dois[df_dois['Regiões'] == regiões]['Ano de Abertura'])
    axs[i].set_title(regiões)
    axs[i].set_xlabel('Ano de Abertura')


plt.tight_layout()


plt.show()


# In[460]:


# Crie um gráfico de dispersão
plt.figure(figsize=(6, 4))
plt.scatter(df_dois['Regiões'].astype('category').cat.codes, df_dois['Ano de Abertura'])
plt.xticks(range(len(df_dois['Regiões'].astype('category').cat.categories)), df_dois['Regiões'].astype('category').cat.categories)
plt.title('Relação entre Região e Ano de Abertura')
plt.xlabel('Região')
plt.ylabel('Ano de Abertura')
plt.show()


# In[461]:


#tipo x validde

#

pivot_table = df_dois.pivot_table(index='Tipo', columns='Validade 2023-12-31', aggfunc='size', fill_value=0)

# Ordene a tabela pivot com base nos valores da coluna "1" em ordem decrescente
pivot_table = pivot_table.sort_values(by=1, ascending=False)

# Reverta a ordem das colunas da tabela pivot
pivot_table = pivot_table[[1, 0]]

# Crie um gráfico de barras
pivot_table.plot(kind='bar', width=0.8)

# Adicione título e rótulos
plt.title('Tipos de estabelecimentos conforme a validade do certificado')
plt.xlabel('Tipo')
plt.xticks(rotation=0)
plt.ylabel('Contagem')

plt.legend(labels=['Válido', 'Vencido'])


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


# Exiba o gráfico
plt.show()


# In[462]:


#ano de abertura x porte


# In[463]:


df_dois.head(5)


# In[464]:


df_dois['Porte'].value_counts()


# In[465]:


plt.figure(figsize=(6, 4))

for i, col in enumerate(df_dois.groupby('Ano de Abertura')['Porte'].value_counts().unstack().columns):
    plt.plot(df_dois.groupby('Ano de Abertura')['Porte'].value_counts().unstack()[col], linestyle=['-', '--', '-.'][i], label=col)

plt.title('Tendência da distribuição em função do porte das empresas')
plt.xlabel('Ano de Abertura')
plt.ylabel('Proporção de empresas')
plt.legend(title='Porte das Empresas')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()


# In[466]:


fig, axs = plt.subplots(1, 2, figsize=(11, 4))

# Gráfico 1
filtro_validade_porte = df_dois[df_dois['Validade 2023-12-31'] == 0]['Porte'].value_counts()
filtro_validade_porte.plot(kind='bar', ax=axs[0], width=0.7)
axs[0].set_title('Quantidade de empresas com validade de certificado vencido')
axs[0].set_xlabel('Porte da empresa')
axs[0].set_ylabel('Quantidade de certificados vencidos')
axs[0].tick_params(axis='x', rotation=0)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].spines['left'].set_visible(False)

# Gráfico 2
categorias = ['MICROEMPRESA', 'PEQUENO PORTE', 'MÉDIO E GRANDE']
porcentagens = [porcentagem_microempresa, porcentagem_pequena, porcentagem_medio_grande]
axs[1].bar(categorias, porcentagens)
axs[1].set_title('Porcentagem de certificados vencidos por porte da empresa')
axs[1].set_xlabel('Porte da empresa')
axs[1].set_ylabel('Proporção de certificados vencidos (%)')
axs[1].tick_params(axis='x', rotation=0)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(False)

# Mostrar os gráficos
plt.tight_layout()
plt.show()


# In[467]:


# Criar um gráfico com duas subplots
fig, axs = plt.subplots(1, 2, figsize=(11, 4))

# Gráfico 1
vencidos_região = df_dois[df_dois['Validade 2023-12-31'] == 0]['Regiões'].value_counts()
vencidos_região.plot(kind='bar', ax=axs[0], width=0.7)
axs[0].set_title('Quantidade de Certificados Vencidos por Região')
axs[0].set_xlabel('Região')
axs[0].set_ylabel('Quantidade de certificados vencidos')
axs[0].tick_params(axis='x', rotation=0)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].spines['left'].set_visible(False)

# Gráfico 2
valido_regiao = df_dois[df_dois['Validade 2023-12-31'] == 1]['Regiões'].value_counts().to_dict()
vencido_regiao = df_dois[df_dois['Validade 2023-12-31'] == 0]['Regiões'].value_counts().to_dict()

validos_sul = valido_regiao['Sul']
validos_sudeste = valido_regiao['Sudeste']
validos_nordeste = valido_regiao['Nordeste']
validos_centrooeste = valido_regiao['Centro-Oeste']
validos_norte = valido_regiao['Norte']

vencidos_sul = vencido_regiao['Sul']
vencidos_sudeste = vencido_regiao['Sudeste']
vencidos_nordeste = vencido_regiao['Nordeste']
vencidos_centrooeste = vencido_regiao['Centro-Oeste']
vencidos_norte = vencido_regiao['Norte']

total_validade_sul = validos_sul + vencidos_sul
total_validade_sudeste = validos_sudeste + vencidos_sudeste
total_validade_nordeste = validos_nordeste + vencidos_nordeste
total_validade_centrooeste = validos_centrooeste + vencidos_centrooeste
total_validade_norte = validos_norte + vencidos_norte

porcentagem_sul = (vencidos_sul * 100) / total_validade_sul
porcentagem_sudeste = (vencidos_sudeste * 100) / total_validade_sudeste
porcentagem_nordeste = (vencidos_nordeste * 100) / total_validade_nordeste
porcentagem_centrooeste = (vencidos_centrooeste * 100) / total_validade_centrooeste
porcentagem_norte = (vencidos_norte * 100) / total_validade_norte

porcentagens_regioes = [porcentagem_sul, porcentagem_sudeste, porcentagem_nordeste, porcentagem_centrooeste, porcentagem_norte]
categorais_regioes = ['Sul', 'Sudeste', 'Nordeste', 'Centro-Oeste', 'Norte']

porcentagens_regioes_sorted = sorted(porcentagens_regioes, reverse=True)
categorais_regioes_sorted = [x for _, x in sorted(zip(porcentagens_regioes, categorais_regioes), reverse=True)]

axs[1].bar(categorais_regioes_sorted, porcentagens_regioes_sorted)
axs[1].set_title('Proporção de Certificados Vencidos por Região')
axs[1].set_xlabel('Região')
axs[1].set_ylabel('Proporção de certificados vencidos (%)')
axs[1].tick_params(axis='x', rotation=0)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(False)

# Mostrar o gráfico
plt.tight_layout()
plt.show()


# A região Sudeste é a que tem o maior número de filiais, podemos considerar que seja uma região com boas condições para os microempresários expandirem seus negócios e proporcionar a necessidade de crédito para esse público.
# 
# As regiões Sul e Nordeste possuem poucas filiais abertas, seria necessário um estudo aprofundado para saber o porquê e se existe uma oportunidade de expansão se tratando dessas regiões ou se investimento em filiais pode não ser interessante para esse público.
# 
# A região Sudeste possui uma quantidade de empresas de médio e grande porte tão grande quanto microempresas. Infelizmente, por falta de dados, não sabemos a quantidade de médias e de grandes empresas de maneira individual. Porém, quando olhamos para a região Nordeste, podemos perceber que a quantidade de microempresas que ela possui é tão grande quanto a de São Paulo, o que nos dá a entender que o microempreendedorismo na região é bem forte, seguindo da região Sul.
# 
# A grande maioria dos empreendimentos está concentrada em restaurantes. Em todos os ramos de atividade, a grande maioria dos estabelecimentos tem um porte de microempresa.
# 
# Olhando para a distribuição do tipo de estabelecimento em relação ao tipo de estrutura, podemos observar que o ramo de restaurantes é o que possui a maior proporção de filiais, talvez seja por ser o tipo de atividade em maior número. Porém, olhando para os demais, a proporção segue muito baixa.
# 
# Se a instituição tiver interesse em criar uma linha de crédito para que o empresário venha abrir uma filial, segue sendo mais interessante olhar para a atividade dos restaurantes do que para os demais.
# 
# Devemos estudar uma relação de filiais e de expansão. A distribuição das categorias de natureza jurídica por região mostra que, na região Nordeste, o número de empresas individuais supera todas as demais, sendo que nas outras regiões os empresários preferem uma sociedade empresarial.
# 
# Quanto à distribuição de estabelecimentos conforme o prazo de validade do certificado, podemos verificar que a região Sul tem uma boa proporção de certificados que não foram renovados, o que nos leva a questionar se essas empresas estão trabalhando na informalidade ou se elas faliram.
# 
# Nas regiões Nordeste e Sudeste, a proporção é bem baixa se for levar em consideração os certificados válidos.
# 
# Ao analisar a região em função do ano de abertura, não achei nada de relevante.
# 
# A distribuição do tipo de estabelecimento conforme o prazo de validade do certificado não forneceu informações relevantes.
# 
# Percebemos que ao longo do tempo, não houve um aumento substancial de pequenas empresas, o que nos leva a crer que o microempresário talvez prefira continuar com o empreendimento nas mesmas condições ou criar novos microempreendimentos.
# 
# Houve um aumento de médias e grandes empresas, mas se levarmos em consideração que essa categoria está representando outras duas simultaneamente, provavelmente veremos uma condição semelhante ao que ocorre com as empresas de pequeno porte.
# 
# Os microempreendimentos são os que têm tido um aumento significativo ao longo dos anos, crescendo de forma bem significativa.

# In[ ]:





# # CONCLUSÃO

# A maioria são microempreendimentos, logo seria interessante crédito para esse público, principalmente para as empresas com natureza jurídica em Sociedade Empresária Limitada e Empresário Individual.
# 
# As regiões Sul e Sudeste são as maiores em nível de atividade; quanto às demais regiões, seria melhor focar em estados de maneira mais pontual (Alagoas, Bahia, Ceará, Goiás), por exemplo.
# 
# Percebemos que ao longo do tempo, não houve um aumento substancial de pequenas empresas, o que nos leva a crer que o microempresário talvez prefira continuar com o empreendimento nas mesmas condições ou criar novos microempreendimentos.
# 
# Houve um aumento de médias e grandes empresas, mas se levarmos em consideração que essa categoria está representando outras duas simultaneamente, provavelmente veremos uma condição semelhante ao que ocorre com as empresas de pequeno porte.
# 
# Os microempreendimentos são os que têm tido um aumento significativo ao longo dos anos, crescendo de forma bem significativa.
# 
# Então, uma linha de crédito interessante seria para o microempresário de todos os estados da região Sul e Sudeste, também para os estados de Alagoas, Bahia, Ceará, Goiás, que participem de Sociedade Empresária Limitada e Empresário Individual, como natureza jurídica, principalmente aqueles que empreendem com restaurantes ou similares (lanchonetes, quiosques, entre outros).
# 
# Se tratando de uma linha de crédito para expansão de filiais, a região Sudeste seria a mais interessante para esse propósito, já que se trata da localidade com o maior número de filiais. Porém, seria mais interessante olhar para a atividade dos restaurantes do que para os demais. Se for disponibilizar uma linha de crédito para os estados da região Nordeste, seria mais interessante focar nas empresas individuais, pois elas superam as de sociedade empresarial.
# 
# Quando verificamos a quantidade de empresas com certificado vencido em relação ao seu tamanho (porte), podemos verificar que a maior quantidade está relacionada às microempresas. As categorias de pequeno porte e médio e grande porte possuem números semelhantes. Porém, para se ter uma verdadeira profundidade, se faz necessário analisar a proporção de certificados vencidos em relação ao total de certificados para cada categoria. Sendo assim, conseguimos verificar que realmente as microempresas não renovam seu certificado, e isso pode estar associado a falências ou à não necessidade de trabalhar com esse registro, isso seguido das empresas de pequeno porte.
# 
# 
# Olhando para a quantidade de certificados vencidos por região, nos deparamos com a região Sul liderando nesse quesito, vencendo a região Sudeste, região da qual possui uma quantidade maior de estabelecimentos. Porém, ao analisar a proporção de certificados vencidos por região, percebemos que a condição se mantém alta na região Sul e cai de forma considerável para a região Sudeste e aumenta de forma considerável para a região Centro-Oeste.
# 
# Portanto levando em consideração essas questões, poderia ser interessante fornecer uma linha de crédito que o micro e pequeno empreendedor voltassem a formalizar os seus negócios ou até mesmo que conseguissem manter as suas empresas abertas.Se tratando de uma linha de crédito diferenciada para que empresas mantenham seu certificado ativo, reestruturando seu negócio para que não venham a falir ou operar de forma irregular, seria interessante focar nas regiões Sul e Centro-Oeste. Se tratando da região Sudeste, seria muito mais interessante disponibilizar crédito com o propósito de expandir os negócios.
# 

# In[ ]:





# In[ ]:




