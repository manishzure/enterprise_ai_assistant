
import pytest

from app.agents.sql_security import validate_sql


@pytest.mark.parametrize("query", [
    "SELECT * FROM employees;",
    "SELECT COUNT(*) FROM employees;",
    "SELECT name, salary FROM employees WHERE salary > 90000;",
])
def test_select_queries_are_allowed(query):
    result = validate_sql(query)
    assert result == query.strip()


@pytest.mark.parametrize("query", [
    "DELETE FROM employees;",
    "UPDATE employees SET salary = 100000;",
    "DROP TABLE employees;",
    "INSERT INTO employees (name) VALUES ('Test');",
    "SELECT * FROM employees; DELETE FROM employees;",
    "SELECT * INTO employee_backup FROM employees;",
])
def test_unsafe_queries_are_blocked(query):
    with pytest.raises(ValueError):
        validate_sql(query)