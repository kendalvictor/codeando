from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/plantilla')
def plantilla():
    contexto = {
        'nombre': 'moises',
        'mayor': False,
        'productos': [
            {'nombre': 'papa', 'precio': 10.5},
            {'nombre': 'camote', 'precio': 5},
            {'nombre': 'cebolla', 'precio': 1.5},
        ]
    }
    return render_template('index.html', **contexto)


@app.route('/saludar/<nombre>')
def saludo(nombre):
    return 'Hola {}'.format(nombre)


@app.route('/saludar', methods=['GET', 'POST'])
def saludar():
    if request.method == 'POST':
        nombre = request.form['nombre']
    else:
        nombre = ''
    return render_template('saludar.html', nombre=nombre)


@app.route('/home')
def home():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
