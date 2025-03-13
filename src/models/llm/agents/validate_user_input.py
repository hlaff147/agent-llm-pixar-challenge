import json
import traceback
from config.logging_config import logger
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from config.settings import OPENAI_API_KEY, TABLE_INFO, TABLE_NAME
from models.prompts.static_prompt_str import QUERY_VALIDATOR_TEMPLATE
from models.query_validator import QueryValidator

validator = QueryValidator()

def validate_user_input(user_input: str) -> str:
    """
    Function wrapper for validator class.
    """
    return validator.validate_user_input(user_input)