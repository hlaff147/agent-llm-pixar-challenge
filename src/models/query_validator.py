import json
import traceback
from typing import Dict, Any
from config.logging_config import logger
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config.settings import OPENAI_API_KEY, TABLE_INFO, TABLE_NAME, OPENAI_MODEL
from models.prompts.static_prompt_str import QUERY_VALIDATOR_TEMPLATE

class QueryValidator:
    """Class to handle validation of user queries using LLM."""
    
    def __init__(self):
        """Initialize the validator with LLM and prompt chain."""
        self.function_name = self.__class__.__name__
        
        logger.debug(f"[{self.function_name}] Initializing validator")
        
        self.llm = ChatOpenAI(
            model=OPENAI_MODEL,
            temperature=0,
            openai_api_key=OPENAI_API_KEY,
            model_kwargs={"response_format": {"type": "json_object"}}
        )
        
        self.prompt = ChatPromptTemplate.from_template(QUERY_VALIDATOR_TEMPLATE)
        self.chain = self.prompt | self.llm
        
        logger.info(f"[{self.function_name}] Validator initialized successfully")

    def validate_user_input(self, user_input: str) -> str:
        """
        Validate if user input matches database schema.
        
        Args:
            user_input (str): User's question or query
            
        Returns:
            str: JSON string with validation result
        """
        if not user_input:
            logger.warning(f"[{self.function_name}] Empty input received")
            return json.dumps({
                "valido": False,
                "racional": "Input não pode estar vazio",
                "campos_analisados": [],
                "operacoes": []
            })
            
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
                
            # Map the response to the expected format
            validation_result = {
                "valido": response_content.get("is_valid", False),
                "racional": response_content.get("reason", "Erro na validação"),
                "campos_analisados": response_content.get("analyzed_fields", []),
                "operacoes": response_content.get("operations", [])
            }
            
            logger.info(f"[{self.function_name}] Validation completed")
            logger.debug(f"[{self.function_name}] Validation result: {validation_result}")
            
            return json.dumps(validation_result)
            
        except Exception as e:
            logger.error(f"[{self.function_name}] Error during validation: {str(e)}")
            logger.error(f"[{self.function_name}] Stacktrace: {traceback.format_exc()}")
            
            return json.dumps({
                "valido": False,
                "racional": f"Erro na validação: {str(e)}",
                "campos_analisados": [],
                "operacoes": []
            })