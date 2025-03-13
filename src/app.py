import streamlit as st
import pandas as pd
import json
import os
from config.settings import CSV_PATH
from executors.duckdb_query_executor import DuckDBQueryExecutor
from models.llm.agents import generate_query, validate_user_input

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
    st.write("**Validando entrada...**")
    validation_result = validate_user_input.validate_user_input(user_input)
    validation_result_dict = json.loads(validation_result)

    if not validation_result_dict["valido"]:
        st.error(f"Entrada inválida: {validation_result_dict['racional']}")
    else:
        st.write("**Gerando query SQL...**")
        sql_response = generate_query.generate_query(user_input)

        # Altere o nome da tabela para o nome correto do dataset
        st.code(f"Query SQL Gerada:\n{sql_response}", language="sql")


        st.success("Query SQL validada com sucesso!")

        st.write("**Executando query no DuckDB**")
        executor = DuckDBQueryExecutor(df)
        df_result = executor.execute_query(sql_response)

        if isinstance(df_result, pd.DataFrame):
            st.write("**Resultado da Query:**")
            st.dataframe(df_result)

            # st.write("**Gerando análise explicativa...**")
            # analysis = analyse_response_query(df_result)
            # st.write("**Resposta reformulada:**")
            # st.write(analysis["analise"])
        else:
            st.error(f"Erro ao executar a query: {df_result}")
