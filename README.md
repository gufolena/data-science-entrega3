# data-science-entrega3

# Nome
data-science-entrega3

# Descrição
Este é um projeto da disciplina de Data Science dividido em dois momentos distintos:

Primeiro Momento: Análise Exploratória de Dados

No primeiro momento, estaremos focados na limpeza, processamento e análise dos dados. Este estágio incluirá:

- Limpeza de Dados: Tratamento de dados ausentes, correção de formatos, etc.
- Processamento de Dados: Transformação e preparação dos dados para análise.
- Análise Descritiva: Exploração estatística básica para entender a distribuição e características dos dados.
- Estudo de Correlações: Identificação e análise das correlações entre as variáveis.



Segundo Momento: Dashboard Interativo e Relatório de Insights

No segundo momento do projeto, focaremos na criação de um dashboard interativo e na elaboração de um relatório que destacará os principais insights obtidos durante a análise dos dados. Este estágio incluirá:

- Desenvolvimento do Dashboard: Utilização de ferramentas como Streamlit para criar um ambiente interativo que permita visualizações dinâmicas dos dados.
- Visualizações Interativas: Implementação de gráficos e tabelas que facilitam a compreensão das informações pelos usuários.
- Relatório de Insights: Documentação dos principais achados do estudo, destacando padrões identificados, tendências observadas e recomendações baseadas nos dados analisados.


# Instalação
Existem duas formas de realizar a instalação, pelo pipenv ou pelo requirements.txt

1. Pelo primeiro caso:
    - pip install pipenv (caso o usuário não possua ele instalado)
    - Vá até o diretório raiz do projeto
    - pipenv install
     
2. Pelo segundo caso : 
    - pip install -r requirements.txt 



# Como Usar

Execute o arquivo analise_pessoas_vacinadas_2022.py para ele realizar todo o primeiro momento descrito acima, gerando na raiz do seu projeto:
- Pasta Graficos, que contém as imagens salvas dos gráficos criados e um arquivo html para ser aberto
- Arquivo csv "vacinas_2022.csv", que é o arquivo baixado após a realização do primeiro momento. *É obrigatório o usuário possuir esse arquivo na raiz do projeto, pois o arquivo app.py usa ele para a criação dos dashboards*
- Execute o arquivo app.py com o comando no terminal do projeto:
    - streamlit run app.py



# Autores
Gustavo Folena Araújo, Hugo Jorge e Maria Júlia 

# Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

# Tempo de execução
O arquivo analise_pessoas_vacindas_2022.py executa em 30 segundos
O arquivo app.py executa entre 10 - 13 segundos