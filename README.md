# Agent LLM para o Maven Pixar Challenge
![diagrama_uml_llm_agent_pixar](https://github.com/user-attachments/assets/280b5403-8861-4792-9b61-598e46820de9)

# Agent LLM para o Maven Pixar Challenge

Este projeto implementa um **agente LLM** que recebe perguntas em linguagem natural sobre filmes da Pixar, converte essas perguntas em queries SQL, executa as queries num banco de dados local (utilizando DuckDB) e gera insights a partir dos resultados.

## Estrutura do Projeto

```
agent-llm-pixar-challenge/
├── data/
│   └── pixar_films_db.csv       # Dataset dos filmes da Pixar
├── src/
│   ├── app.py                   # Aplicação principal Streamlit
│   ├── config/                  # Configurações do projeto
│   │   ├── settings.py          # Configurações gerais e schema
│   │   └── logging_config.py    # Configurações de logging
│   ├── executors/              
│   │   └── duckdb_query_executor.py  # Executor de queries DuckDB
│   └── models/
│       ├── llm/
│       │   └── agents/          # Agentes LLM
│       │       ├── generate_query.py
│       │       └── validate_user_input.py
│       ├── prompts/             # Templates de prompts
│       │   └── static_prompt_str.py
│       ├── generate_query_chat.py
│       └── query_validator.py
└── requirements.txt
```

## Funcionalidades

### 1. Validação de Entrada
- Implementado em [`models/query_validator.py`](src/models/query_validator.py)
- Valida se a pergunta está de acordo com o schema do banco
- Verifica permissões e restrições de segurança
- Retorna feedback detalhado sobre a validação

### 2. Geração de Queries SQL
- Implementado em [`models/generate_query_chat.py`](src/models/generate_query_chat.py)
- Converte perguntas em linguagem natural para SQL
- Utiliza o GPT-3.5-turbo para geração precisa
- Respeita o schema definido em [`config/settings.py`](src/config/settings.py)

### 3. Execução de Queries
- Implementado em [`executors/duckdb_query_executor.py`](src/executors/duckdb_query_executor.py)
- Executa queries SQL no DuckDB
- Gerencia conexão com o banco de dados
- Trata erros de execução

### 4. Interface Web
- Implementado em [`app.py`](src/app.py)
- Interface interativa com Streamlit
- Exibição de resultados em tabelas
- Feedback visual do processo

## Dataset

O dataset contém informações detalhadas sobre filmes da Pixar, incluindo:
- Título e data de lançamento
- Diretor, produtor e equipe criativa
- Métricas financeiras (orçamento e bilheteria)
- Avaliações da crítica
- Indicações e prêmios do Oscar
- Informações técnicas (duração, gênero)

## Configuração

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd agent-llm-pixar-challenge
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
- Crie um arquivo `.env` na raiz do projeto
- Adicione sua chave da API OpenAI:
```
OPENAI_API_KEY=sua_chave_aqui
```

4. Coloque o dataset na pasta correta:
- Baixe o arquivo CSV do dataset Pixar
- Coloque em `data/pixar_films_db.csv`

5. Execute a aplicação:
```bash
streamlit run src/app.py
```

## Tecnologias Utilizadas

- **LangChain**: Framework para desenvolvimento com LLMs
- **OpenAI GPT-3.5**: Modelo de linguagem para geração de queries
- **DuckDB**: Banco de dados analítico em memória
- **Streamlit**: Framework para interface web
- **Pandas**: Manipulação e análise de dados
