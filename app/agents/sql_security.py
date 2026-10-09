
import sqlglot
from sqlglot import exp


def validate_sql(sql_query: str) -> str:
    """Allow exactly one read-only SELECT statement."""

    if not sql_query or not sql_query.strip():
        raise ValueError("SQL query cannot be empty.")

    try:
        statements = sqlglot.parse(sql_query, read="postgres")
    except Exception as exc:
        raise ValueError("Invalid SQL syntax.") from exc

    # Reject empty input and multiple statements.
    if len(statements) != 1 or statements[0] is None:
        raise ValueError("Only one SQL statement is allowed.")

    statement = statements[0]

    # Reject DELETE, UPDATE, INSERT, DROP, ALTER, and other non-SELECT statements.
    if not isinstance(statement, exp.Select):
        raise ValueError("Only SELECT queries are allowed.")

    # SELECT INTO can create a table, so reject it too.
    if statement.find(exp.Into):
        raise ValueError("SELECT INTO is not allowed.")

    return sql_query.strip()