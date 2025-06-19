from Models.voto import Voto

class VotosController:
    @staticmethod
    def emitir(votante_id, candidato_id):
        return Voto.emitir(votante_id, candidato_id)

    @staticmethod
    def obtener_todos():
        return Voto.obtener_todos()

    @staticmethod
    def obtener_estadisticas():
        return Voto.obtener_estadisticas()