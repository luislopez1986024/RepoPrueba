from flask import Blueprint, request, jsonify
from Models.candidato import Candidato

candidatos_bp = Blueprint('candidatos', __name__)

@candidatos_bp.route('/candidates', methods=['POST'])
def registrar_candidato():
    data = request.json
    if not data.get('nombre'):
        return jsonify({'error': 'El nombre es obligatorio'}), 400
    try:
        Candidato.crear(data['nombre'], data.get('partido'))
        return jsonify({'mensaje': 'Candidato registrado'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@candidatos_bp.route('/candidates', methods=['GET'])
def listar_candidatos():
    candidatos = Candidato.obtener_todos()
    return jsonify([dict(zip([col[0] for col in candidatos[0].cursor_description], row)) for row in candidatos])

@candidatos_bp.route('/candidates/<int:candidato_id>', methods=['GET'])
def obtener_candidato(candidato_id):
    candidato = Candidato.obtener_por_id(candidato_id)
    if not candidato:
        return jsonify({'error': 'Candidato no encontrado'}), 404
    return jsonify(dict(zip([col[0] for col in candidato.cursor_description], candidato)))

@candidatos_bp.route('/candidates/<int:candidato_id>', methods=['DELETE'])
def eliminar_candidato(candidato_id):
    Candidato.eliminar(candidato_id)
    return jsonify({'mensaje': 'Candidato eliminado'}), 200