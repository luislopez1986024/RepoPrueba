import pyodbc
from .database import db
from .votante import Votante
from .candidato import Candidato

class Voto:
    @staticmethod
    def emitir(votante_id, candidato_id):
        # Validaciones
        votante = Votante.obtener_por_id(votante_id)
        if not votante:
            raise ValueError("Votante no encontrado")
        if votante.ha_votado:
            raise ValueError("Este votante ya ha votado")
        
        if not Candidato.obtener_por_id(candidato_id):
            raise ValueError("Candidato no encontrado")

        with db.get_connection() as conn:
            cursor = conn.cursor()
            try:
                # Registrar voto
                cursor.execute(
                    "INSERT INTO Votos (votante_id, candidato_id) VALUES (?, ?)",
                    (votante_id, candidato_id)
                )
                # Actualizar estados
                Votante.marcar_como_votado(votante_id)
                Candidato.incrementar_votos(candidato_id)
                conn.commit()
            except pyodbc.IntegrityError:
                raise ValueError("Este votante ya ha emitido un voto")

    @staticmethod
    def obtener_todos():
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT v.id, vt.nombre as votante, c.nombre as candidato, v.timestamp 
                FROM Votos v
                JOIN Votantes vt ON v.votante_id = vt.id
                JOIN Candidatos c ON v.candidato_id = c.id
            """)
            return cursor.fetchall()

    @staticmethod
    def obtener_estadisticas():
        with db.get_connection() as conn:
            cursor = conn.cursor()
            
            # Votos por candidato
            cursor.execute("""
                SELECT c.id, c.nombre, c.partido, c.votos, 
                       (c.votos * 100.0 / NULLIF((SELECT COUNT(*) FROM Votos), 0)) as porcentaje
                FROM Candidatos c
                ORDER BY c.votos DESC
            """)
            stats = [dict(zip([column[0] for column in cursor.description], row)) 
                    for row in cursor.fetchall()]
            
            # Totales
            cursor.execute("SELECT COUNT(*) FROM Votantes WHERE ha_votado = 1")
            total_votantes = cursor.fetchone()[0]
            
            return {
                'votos_por_candidato': stats,
                'total_votantes': total_votantes
            }