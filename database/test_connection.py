
from database.db import connect_db

try:
    connection = connect_db()
    print("Database connection successful!")
    connection.close()
except Exception as e:
    print("Database connection failed:", e)
