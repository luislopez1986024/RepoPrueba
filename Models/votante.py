from .database import db

class Votante:
    @staticmethod
    def crear(nombre, email):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO Votantes (nombre, email) OUTPUT INSERTED.id VALUES (?, ?)",
                    (nombre, email)
                )
                result = cursor.fetchone()
                conn.commit()  
                return result[0]
            except Exception as e:
                conn.rollback() # Rollback en caso de error
                raise ValueError(f"Error al crear votante: {str(e)}")

    @staticmethod
    def obtener_todos():
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, email, ha_votado FROM Votantes")
            return cursor.fetchall()

    @staticmethod
    def obtener_por_id(id_votante):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, email, ha_votado FROM Votantes WHERE id = ?", (id_votante,))
            return cursor.fetchone()

    @staticmethod
    def marcar_como_votado(id_votante):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Votantes SET ha_votado = 1 WHERE id = ?", (id_votante,))
            conn.commit()

    @staticmethod
    def eliminar(id_votante):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Votantes WHERE id = ?", (id_votante,))
            conn.commit()