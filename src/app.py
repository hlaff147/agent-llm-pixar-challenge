import streamlit as st
import pandas as pd
import json
import os
from config.settings import CSV_PATH, DATA_DIR
from executors.duckdb_query_executor import DuckDBQueryExecutor
from models import generate_query_chat
from models.query_validator import QueryValidator
from models.generate_insight_chat import GenerateInsight

# Validate CSV file exists
if not os.path.exists(CSV_PATH):
    st.error(f"CSV file not found at: {CSV_PATH}")
    st.write(f"Please ensure the Pixar films dataset is placed in: {DATA_DIR}")
    st.stop()

# Load dataset
try:
    df = pd.read_csv(CSV_PATH)
except Exception as e:
    st.error(f"Error loading CSV file: {str(e)}")
    st.stop()

st.title("Chatbot de Análise de Dados SQL")
st.subheader("Interaja com seu dataset de forma intuitiva!")

user_input = st.text_input("Digite sua pergunta:", placeholder="Exemplo: Qual a média de idade por UF?")

if st.button("Executar"):
    retries = 0
    success = False
    query = ""
    error_response = ""
    st.write("**Validando entrada...**")
    validator = QueryValidator()
    validation_result = validator.validate_user_input(user_input)
    validation_result_dict = json.loads(validation_result)

    while retries < 5 and not success:
        if not validation_result_dict["valido"]:
            st.error(f"Entrada inválida: {validation_result_dict['racional']}")
            retries = 5
        else:
            st.write("**Gerando query SQL...**")
            query_generator = generate_query_chat.GenerateQuery()

            if retries > 0:
                sql_response = query_generator.generate_query(user_input, query, error_response)
            else:
                sql_response = query_generator.generate_query(user_input)

            # Altere o nome da tabela para o nome correto do dataset
            st.code(f"Query SQL Gerada:\n{sql_response}", language="sql")


            st.success("Query SQL validada com sucesso!")

            st.write("**Executando query no DuckDB**")
            executor = DuckDBQueryExecutor(df)
            df_result = executor.execute_query(sql_response)

            if isinstance(df_result, pd.DataFrame):
              st.write("**Resultado da Query:**")
              st.dataframe(df_result)
              success = True

              st.write("**Gerando análise explicativa...**")
              insight_generator = GenerateInsight()
              analysis = insight_generator.generate_insight(user_input, sql_response, df_result.to_json())
              st.write("**Resposta reformulada:**")
              st.write(analysis)
            else:
                st.error(f"Erro ao executar a query: {df_result}")
                query = sql_response
                error_response = df_result
                retries += 1
                if retries < 5:
                    st.write(f"**Tentando novamente...**")

