import json
import traceback
from config.logging_config import logger
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config.settings import OPENAI_API_KEY, TABLE_INFO, OPENAI_MODEL
from models.prompts.static_prompt_str import INSIGHTS_GENERATOR_TEMPLATE

class GenerateInsight:
    """Class to handle generation of insights using LLM."""

    def __init__(self):
        """Initialize the insight generator with LLM and prompt chain."""
        self.function_name = self.__class__.__name__

        logger.debug(f"[{self.function_name}] Initializing insight generator")

        self.llm = ChatOpenAI(
            model=OPENAI_MODEL,
            temperature=1,
            openai_api_key=OPENAI_API_KEY,
            model_kwargs={"response_format": {"type": "json_object"}}
        )

        self.prompt = ChatPromptTemplate.from_template(INSIGHTS_GENERATOR_TEMPLATE)
        self.chain = self.prompt | self.llm

        logger.info(f"[{self.function_name}] Insight generator initialized successfully")

    def generate_insight(self, user_query: str, sql_query: str, dataframe: str) -> str:
        """
        Generate insights based on the user's query, the executed SQL query, and the returned data.

        Args:
            user_query (str): The user's natural language question.
            sql_query (str): The executed SQL query.
            dataframe (str): The query result data as a string or JSON.

        Returns:
            str: Generated insights.
        """
        if not user_query or not sql_query or not dataframe:
            logger.warning(f"[{self.function_name}] Missing required input for insight generation")
            raise ValueError("Todos os parâmetros (user_query, sql_query, dataframe) devem ser fornecidos")

        try:
            logger.debug(f"[{self.function_name}] Processing insight generation for query: '{user_query}'")
            response = self.chain.invoke({
                "db_schema": TABLE_INFO,
                "user_query": user_query,
                "sql_query": sql_query,
                "dataframe": dataframe
            })

            logger.debug(f"[{self.function_name}] Raw LLM response: {response}")

            # Parse response content
            try:
                response_content = json.loads(response.content)
                insights = response_content.get("insights")
            except (json.JSONDecodeError, AttributeError) as e:
                logger.error(f"[{self.function_name}] Error decoding JSON: {e}")
                raise ValueError(f"Falha ao decodificar a resposta JSON: {e}")

            if not insights:
                raise ValueError("Insights not generated")

            logger.info(f"[{self.function_name}] Insight generation completed")
            logger.debug(f"[{self.function_name}] Generated insights: {insights}")

            return insights

        except Exception as e:
            logger.error(f"[{self.function_name}] Error during insight generation: {str(e)}")
            logger.error(f"[{self.function_name}] Stacktrace: {traceback.format_exc()}")
            raise Exception(f"Erro na geração de insights: {str(e)}")