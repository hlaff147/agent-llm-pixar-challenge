import duckdb
import pandas as pd

class DuckDBQueryExecutor:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.conn = duckdb.connect(database=':memory:')
        self.conn.register("pixar_films", df)

    def execute_query(self, sql_query: str):
        try:
            result = self.conn.execute(sql_query).fetchdf()
            return result
        except Exception as e:
            return str(e)
