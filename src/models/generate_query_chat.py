import json
import traceback
from typing import Dict, Any
from config.logging_config import logger
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config.settings import OPENAI_API_KEY, TABLE_INFO, TABLE_NAME, OPENAI_MODEL
from models.prompts.static_prompt_str import SQL_GENERATOR_TEMPLATE

class GenerateQuery:
    """Class to handle SQL query generation using LLM."""
    
    def __init__(self):
        """Initialize the generator with LLM and prompt chain."""
        self.function_name = self.__class__.__name__
        
        logger.debug(f"[{self.function_name}] Initializing query generator")
        
        self.llm = ChatOpenAI(
            model=OPENAI_MODEL,
            temperature=0,
            openai_api_key=OPENAI_API_KEY,
            model_kwargs={"response_format": {"type": "json_object"}}
        )
        
        self.prompt = ChatPromptTemplate.from_template(SQL_GENERATOR_TEMPLATE)
        self.chain = self.prompt | self.llm
        
        logger.info(f"[{self.function_name}] Generator initialized successfully")

    def generate_query(self, user_input: str) -> str:
        """
        Generate SQL query from user input using Pixar films specific template.
        
        Args:
            user_input (str): User's natural language question
            
        Returns:
            str: Generated SQL query
        """
        if not user_input:
            logger.warning(f"[{self.function_name}] Empty input received")
            raise ValueError("Input não pode estar vazio")
            
        try:
            logger.debug(f"[{self.function_name}] Processing input: '{user_input}'")
            
            response = self.chain.invoke({
                "db_schema": TABLE_INFO,
                "table_name": TABLE_NAME,
                "user_input": user_input
            })
            
            logger.debug(f"[{self.function_name}] Raw LLM response: {response}")
            
            # Parse response content
            if isinstance(response.content, str):
                response_content = json.loads(response.content)
            else:
                response_content = response.content
                
            sql_query = response_content.get("sql_query", "")
            if not sql_query:
                raise ValueError("SQL query not generated")
                
            logger.info(f"[{self.function_name}] Query generation completed")
            logger.debug(f"[{self.function_name}] Generated query: {sql_query}")
            
            return sql_query
            
        except Exception as e:
            logger.error(f"[{self.function_name}] Error during query generation: {str(e)}")
            logger.error(f"[{self.function_name}] Stacktrace: {traceback.format_exc()}")
            raise Exception(f"Erro na geração da query: {str(e)}")

generator = GenerateQuery()

def generate_query(user_input: str) -> str:
    """
    Function wrapper for generator class.
    """
    return generator.generate_query(user_input)