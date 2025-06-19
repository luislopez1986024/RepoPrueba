from flask import Blueprint, request, jsonify
from Controllers.votantes_controller import VotantesController

votantes_bp = Blueprint('votantes', __name__)


@votantes_bp.route('/voters', methods=['POST'])
def crear_votante():
    data = request.json
    try:
        id_votante = VotantesController.crear(data['nombre'], data['email'])
        return jsonify({'id': id_votante}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@votantes_bp.route('/voters', methods=['GET'])
def obtener_votantes():
    votantes = VotantesController.obtener_todos()
    return jsonify([{
        'id': v[0],
        'nombre': v[1],
        'email': v[2],
        'ha_votado': bool(v[3])
    } for v in votantes])


@votantes_bp.route('/voters/<int:id_votante>', methods=['GET'])
def obtener_votante(id_votante):
    votante = VotantesController.obtener_por_id(id_votante)
    if not votante:
        return jsonify({'error': 'Votante no encontrado'}), 404
    return jsonify({
        'id': votante[0],
        'nombre': votante[1],
        'email': votante[2],
        'ha_votado': bool(votante[3])
    })


@votantes_bp.route('/voters/<int:id_votante>', methods=['DELETE'])
def eliminar_votante(id_votante):
    try:
        VotantesController.eliminar(id_votante)
        return jsonify({'mensaje': 'Votante eliminado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400