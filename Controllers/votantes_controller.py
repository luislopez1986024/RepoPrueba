from Models.votante import Votante
from Models.candidato import Candidato

class VotantesController:
    @staticmethod
    def crear(nombre, email):
        # Verificar que no sea candidato
        candidatos = Candidato.obtener_todos()
        if any(nombre.lower() == c[1].lower() for c in candidatos):
            raise ValueError("Un candidato no puede ser votante")
        return Votante.crear(nombre, email)

    @staticmethod
    def obtener_todos():
        return Votante.obtener_todos()

    @staticmethod
    def obtener_por_id(id_votante):
        return Votante.obtener_por_id(id_votante)

    @staticmethod
    def eliminar(id_votante):
        return Votante.eliminar(id_votante)