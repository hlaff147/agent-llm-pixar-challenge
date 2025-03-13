from models import generate_query_chat


def generate_query(user_input: str) -> str:
    """
    Function wrapper for generator class.
    """
    return generate_query_chat.generate_query(user_input)