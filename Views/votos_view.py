from flask import Blueprint, request, jsonify
from Models.voto import Voto

votos_bp = Blueprint('votos', __name__)

@votos_bp.route('/votes', methods=['POST'])
def emitir_voto():
    data = request.json
    try:
        Voto.emitir_voto(data['votante_id'], data['candidato_id'])
        return jsonify({'mensaje': 'Voto emitido correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@votos_bp.route('/votes', methods=['GET'])
def listar_votos():
    votos = Voto.obtener_todos()
    return jsonify([dict(zip([col[0] for col in votos[0].cursor_description], row)) for row in votos])

@votos_bp.route('/votes/statistics', methods=['GET'])
def obtener_estadisticas():
    try:
        estadisticas, total_votantes = Voto.obtener_estadisticas()
        resultado = [
            {
                'nombre': row[0],
                'votos': row[1],
                'porcentaje': round(row[2], 2) if row[2] is not None else 0.0
            } for row in estadisticas
        ]
        return jsonify({
            'estadisticas': resultado,
            'total_votantes_que_votaron': total_votantes
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500