
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "automated_testing"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD")
    )
    return connection



def save_test_result(test_name, status):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
        INSERT INTO test_results (test_name, status)
        VALUES (%s, %s)
    """

    cursor.execute(query, (test_name, status))

    connection.commit()

    cursor.close()
    connection.close()