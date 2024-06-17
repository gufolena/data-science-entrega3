import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_tags import st_tags

# Carregar os dados
df = pd.read_csv('vacinas_2022.csv')

st.title("Dashboard de Vacinação COVID-19 Pernambuco 2022")

# Selecionar o tipo de gráfico
option = st.selectbox(
    'Escolha o gráfico que deseja visualizar:',
    ('Contagem de Vacinados por Sexo', 'Distribuição de Doses por Faixa Etária', 'Vacinação ao Longo do Tempo', 'Comparação de Tipos de Vacinas')
)

if option == 'Contagem de Vacinados por Sexo':
    # Contagem de vacinados por sexo
    contagem_sexo = df['sexo'].value_counts().reset_index()
    contagem_sexo.columns = ['Sexo', 'Contagem']

    # Criar gráfico de barras
    fig = px.bar(contagem_sexo, x='Sexo', y='Contagem', color='Sexo',
                 labels={'Sexo': 'Sexo', 'Contagem': 'Número de Vacinados'},
                 title='Contagem de Vacinados por Sexo')

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

elif option == 'Distribuição de Doses por Faixa Etária':
    # Converter 'descricao_dose' para numérico
    df['descricao_dose'] = df['descricao_dose'].astype(str).str.extract('(\d+)').astype(int)

    # Adicionar filtro para selecionar as doses a serem visualizadas
    doses_disponiveis = df['descricao_dose'].unique()
    doses_disponiveis_str = [str(dose) for dose in doses_disponiveis]
    
    doses_selecionadas_str = st_tags(
        label='Selecione as doses que deseja visualizar:',
        text='Pressione enter para adicionar mais doses',
        value=doses_disponiveis_str,
        suggestions=doses_disponiveis_str,
        key='1'
    )

    # Converter doses selecionadas de volta para int
    doses_selecionadas = [int(dose) for dose in doses_selecionadas_str]

    # Filtrar os dados com base nas doses selecionadas
    df_filtrado = df[df['descricao_dose'].isin(doses_selecionadas)]
    
    # Contagem de doses por faixa etária
    contagem_doses = df_filtrado.groupby(['faixa_etaria', 'descricao_dose']).size().reset_index(name='Contagem')
    
    # Criar gráfico de barras empilhadas com cores distintas para cada dose
    fig = px.bar(contagem_doses, x='faixa_etaria', y='Contagem', color='descricao_dose',
                 labels={'faixa_etaria': 'Faixa Etária', 'Contagem': 'Número de Vacinados', 'descricao_dose': 'Descrição da Dose'},
                 title='Distribuição de Doses por Faixa Etária',
                 barmode='stack',
                 color_discrete_sequence=px.colors.qualitative.Safe)  # Usando paleta 'Safe' para cores distintas

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

    # Mostrar gráfico de pizza específico das pessoas que tomaram 5 doses
    if 5 in doses_selecionadas:
        df_5_doses = df[df['descricao_dose'] == 5]
        contagem_5_doses = df_5_doses.groupby('faixa_etaria').size().reset_index(name='Contagem')
        
        fig_pie = px.pie(contagem_5_doses, values='Contagem', names='faixa_etaria',
                         title='Distribuição de Pessoas que Tomaram 5 Doses por Faixa Etária',
                         labels={'faixa_etaria': 'Faixa Etária', 'Contagem': 'Número de Vacinados'})
        
        st.plotly_chart(fig_pie)


if option == 'Vacinação ao Longo do Tempo':
    df['data_vacinacao'] = pd.to_datetime(df['data_vacinacao'])
    df['mes_ano'] = df['data_vacinacao'].dt.to_period('M').astype(str)
    
    # Filtro de meses
    meses_disponiveis = df['mes_ano'].unique()
    meses_selecionados = st.sidebar.multiselect(
        'Selecione os meses:',
        options=meses_disponiveis,
        default=meses_disponiveis
    )
    
    # Filtrar dados pelos meses selecionados
    df_filtrado = df[df['mes_ano'].isin(meses_selecionados)]
    vacinacao_tempo = df_filtrado.groupby('data_vacinacao').size().reset_index(name='Contagem')
    
    # Criar gráfico de linha
    fig = px.line(vacinacao_tempo, x='data_vacinacao', y='Contagem',
                  labels={'data_vacinacao': 'Data de Vacinação', 'Contagem': 'Número de Vacinados'},
                  title='Vacinação ao Longo do Tempo')
    
    # Exibir gráfico no Streamlit
    st.plotly_chart(fig)



elif option == 'Comparação de Tipos de Vacinas':
    tipo_vacina = df['vacina_fabricante'].value_counts().reset_index()
    tipo_vacina.columns = ['Fabricante da Vacina', 'Contagem']
    
    fig = px.pie(tipo_vacina, values='Contagem', names='Fabricante da Vacina', 
             title='Distribuição de Tipos de Vacinas por Fabricante', hole=0.5)
    st.plotly_chart(fig)