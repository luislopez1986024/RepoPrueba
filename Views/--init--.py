from .votantes_view import votantes_bp
from .candidatos_view import candidatos_bp
from .votos_view import votos_bp

def register_views(app):
    app.register_blueprint(votantes_bp)
    app.register_blueprint(candidatos_bp)
    app.register_blueprint(votos_bp)