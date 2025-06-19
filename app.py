from flask import Flask, jsonify
from Views.votantes_view import votantes_bp
from Views.candidatos_view import candidatos_bp
from Views.votos_view import votos_bp


app = Flask(__name__)

app.register_blueprint(votantes_bp, url_prefix='/api/v1')  
app.register_blueprint(candidatos_bp, url_prefix='/api/v1')  
app.register_blueprint(votos_bp, url_prefix='/api/v1')       


@app.route('/')
def status():
    return jsonify({"status": "API Electoral Operativa"})


if __name__ == '__main__':
    app.run(debug=True)