import pyodbc
from config import get_connection_string

try:
    conn = pyodbc.connect(get_connection_string())
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 1 nombre FROM Votantes")
    print("✅ Conexión exitosa. Primer votante:", cursor.fetchone()[0])
except Exception as e:
    print(f"❌ Error de conexión: {str(e)}")