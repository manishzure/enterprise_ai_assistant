import os

from dotenv import load_dotenv
from urllib.parse import quote_plus

from langchain_community.utilities import SQLDatabase


load_dotenv()


DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")


database_uri = (
    f"postgresql+psycopg://{DB_USER}:"
    f"{quote_plus(DB_PASSWORD)}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


db = SQLDatabase.from_uri(database_uri)


print("Database connected successfully!")

print("\nTables:")
print(db.get_usable_table_names())


print("\nRunning SQL query...")

result = db.run(
    "SELECT COUNT(*) FROM employees;"
)

print("Result:")
print(result)