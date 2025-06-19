import pyodbc
from contextlib import contextmanager
from config import get_connection_string

class Database:
    @contextmanager
    def get_connection(self):
        conn = None
        try:
            conn = pyodbc.connect(get_connection_string())
            conn.autocommit = False  # Desactivar autocommit para manejar transacciones
            yield conn
            conn.commit()  # Hacer commit si no hubo excepciones
        except pyodbc.Error as e:
            if conn:
                conn.rollback()  # Rollback en caso de error
            print(f"Database connection error: {e}")
            raise
        finally:
            if conn:
                conn.close()

db = Database()