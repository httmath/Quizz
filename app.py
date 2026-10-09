from flask import Flask
from routes.participantes import participantes_bp

app = Flask(__name__)

app.register_blueprint(participantes_bp)

# teste
if __name__ == "__main__":
    app.run(debug=True)