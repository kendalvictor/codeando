from flask import Flask, render_template, request, redirect, jsonify
from models import *

app = Flask(__name__)
lista_tareas = ['Cocinar']


@app.route('/', methods=['GET', 'POST'])
@db_session
def tareas():
    if request.method == 'POST':
        tarea = Tarea(texto=request.form['nombre'])
    return render_template(
        'tareas.html',
        tareas=select(t for t in Tarea)
    )


@app.route('/eliminar/<int:posicion>')
@db_session
def eliminar(posicion):
    tarea = Tarea[posicion]
    tarea.delete()
    return redirect('/')


@app.route('/editar/<int:posicion>', methods=['GET', 'POST'])
@db_session
def editar(posicion):
    tarea = Tarea[posicion]
    if request.method == 'POST':
        tarea.texto = request.form['nombre']
        return redirect('/')

    return render_template(
        'editar.html',
        tarea=tarea
    )


@app.route('/tareas_json', methods=['GET', 'POST'])
@db_session
def tareas_json():
    tareas = select(t.texto for t in Tarea)
    return jsonify([
        {'texto': texto} for texto in tareas
    ])


app.run(debug=True, port=5000)
