from flask import Flask

app = Flask(__name__)


@app.route('/calcular/<operacion>/<int:a>/<int:b>')
def calcular(operacion, a, b):
    operaciones = {
        'suma': lambda x, y: x + y,
        'resta': lambda x, y: x + y,
        'producto': lambda x, y: x + y,
        'cociente': lambda x, y: x + y,
    }
    return str(operaciones[operacion](a, b))

app.run(debug=True)
