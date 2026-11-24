import re
from typing import List, Dict, Any

class WindowFunctionGenerator:
    """Generates SQL window functions and validates them for safety."""
    
    SUPPORTED_FUNCTIONS = {"ROW_NUMBER", "RANK", "DENSE_RANK"}

    @staticmethod
    def validate_query(sql: str) -> bool:
        """Ensures window functions include PARTITION BY or ORDER BY to prevent unbounded memory."""
        if "OVER" in sql.upper():
            if "PARTITION BY" not in sql.upper() and "ORDER BY" not in sql.upper():
                return False
        return True

    @staticmethod
    def generate_ranking_sql(column: str, partition_by: str = None, order_by: str = "DESC", func: str = "RANK") -> str:
        if func not in WindowFunctionGenerator.SUPPORTED_FUNCTIONS:
            raise ValueError(f"Unsupported window function: {func}")
        
        partition = f"PARTITION BY {partition_by}" if partition_by else ""
        return f"{func}() OVER ({partition} ORDER BY {column} {order_by})"

    @staticmethod
    def get_few_shot_examples() -> List[Dict[str, str]]:
        return [
            {
                "question": "Rank products by sales within each category",
                "sql": "SELECT product_name, category, RANK() OVER (PARTITION BY category ORDER BY sales DESC) as rank FROM products"
            },
            {
                "question": "Assign a row number to customers ordered by signup date",
                "sql": "SELECT customer_id, ROW_NUMBER() OVER (ORDER BY signup_date ASC) as row_num FROM customers"
            }
        ]