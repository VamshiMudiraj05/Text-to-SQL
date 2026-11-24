import pytest
from src.engine.window_functions import WindowFunctionGenerator

def test_window_function_generation():
    gen = WindowFunctionGenerator()
    sql = gen.generate_ranking_sql("sales", "category", "DESC", "RANK")
    assert "RANK() OVER (PARTITION BY category ORDER BY sales DESC)" in sql

def test_validation_rules():
    gen = WindowFunctionGenerator()
    # Invalid: No partition or order
    assert gen.validate_query("SELECT RANK() OVER () FROM table") is False
    # Valid: Has order
    assert gen.validate_query("SELECT RANK() OVER (ORDER BY id) FROM table") is True

def test_unsupported_function():
    with pytest.raises(ValueError):
        WindowFunctionGenerator.generate_ranking_sql("col", func="INVALID_FUNC")