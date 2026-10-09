from flask import Blueprint

participantes_bp = Blueprint("participantes", __name__)
@participantes_bp.route("/")
def index():
    return "Quiz funcionando"