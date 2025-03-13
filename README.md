# Agent LLM para o Maven Pixar Challenge

Este projeto implementa um **agente LLM** que recebe perguntas em linguagem natural, converte essas perguntas em queries SQL, executa as queries num banco de dados local (utilizando DuckDB) e gera insights a partir dos resultados. A aplicação foi desenvolvida para participar do [Maven Pixar Challenge](#), utilizando o dataset de filmes da Pixar mantido pelo engenheiro Eric Leung.

## Descrição

O agente LLM foi projetado para:
- **Validar** a pergunta do usuário (guard rails), garantindo que ela seja apenas de consulta e esteja em conformidade com o schema do banco.
- **Converter** a pergunta para SQL utilizando um modelo de linguagem (LLM).
- **Executar** a query no banco de dados (DuckDB) e, em caso de erro, solicitar nova entrada do usuário.
- **Gerar insights** a partir dos resultados e exibi-los de forma clara e interativa.
- **Interface** amigável construída com [Streamlit](https://streamlit.io/).

O dataset utilizado contém informações detalhadas sobre cada filme da Pixar, abrangendo desde "Toy Story" (1995) até "Inside Out 2" (2024). Ele inclui dados sobre criadores (roteiristas, diretores, produtores, etc.), métricas financeiras, desempenho crítico, indicações ao Oscar e muito mais.

## Funcionalidades

- **Conversão Natural → SQL:** Transforma perguntas em linguagem natural em queries SQL.
- **Validação e Segurança:** Verifica a sintaxe e bloqueia operações que possam modificar o banco (ex.: INSERT, UPDATE, DELETE).
- **Execução Local:** Integração com DuckDB para execução de queries localmente.
- **Interface Interativa:** Desenvolvida com Streamlit para facilitar a interação com o usuário.
- **Geração de Insights:** Análise dos resultados das queries e apresentação de insights de forma clara.

## Estrutura do Projeto

- `data/pixar_films_db.csv`: Arquivo CSV contendo o dataset de filmes da Pixar.
- `src/app.py`: Código principal da aplicação, que orquestra o fluxo:
  - Recebe a pergunta do usuário.
  - Valida a pergunta conforme o schema do banco.
  - Converte a pergunta em uma query SQL.
  - Executa a query no DuckDB.
  - Gera e exibe insights.
- `src/utils.py`: Funções auxiliares para validação, conversão e análise dos dados.
- `requirements.txt`: Dependências necessárias para rodar o projeto.
- `LICENSE`: Informações de licença para o projeto.
