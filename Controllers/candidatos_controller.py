from Models.candidato import Candidato
from Models.votante import Votante

class CandidatosController:
    @staticmethod
    def crear(nombre, partido=None):
        # Verificar que no sea votante
        votantes = Votante.obtener_todos()
        if any(nombre.lower() == v[1].lower() for v in votantes):
            raise ValueError("Un votante no puede ser candidato")
        return Candidato.crear(nombre, partido)

    @staticmethod
    def obtener_todos():
        return Candidato.obtener_todos()

    @staticmethod
    def obtener_por_id(id_candidato):
        return Candidato.obtener_por_id(id_candidato)

    @staticmethod
    def eliminar(id_candidato):
        return Candidato.eliminar(id_candidato)