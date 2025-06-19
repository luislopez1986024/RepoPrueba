from .database import db

class Candidato:
    @staticmethod
    def crear(nombre, partido=None):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Candidatos (nombre, partido) OUTPUT INSERTED.id VALUES (?, ?)",
                (nombre, partido)
            )
            return cursor.fetchone()[0]

    @staticmethod
    def obtener_todos():
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, partido, votos FROM Candidatos")
            return cursor.fetchall()

    @staticmethod
    def obtener_por_id(id_candidato):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, partido, votos FROM Candidatos WHERE id = ?", (id_candidato,))
            return cursor.fetchone()

    @staticmethod
    def incrementar_votos(id_candidato):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Candidatos SET votos = votos + 1 WHERE id = ?", (id_candidato,))
            conn.commit()

    @staticmethod
    def eliminar(id_candidato):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Candidatos WHERE id = ?", (id_candidato,))
            conn.commit()