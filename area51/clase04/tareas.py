from flask import Flask, render_template, request, redirect

app = Flask(__name__)
lista_tareas = ['Cocinar']


@app.route('/', methods=['GET', 'POST'])
def tareas():
    if request.method == 'POST':
        lista_tareas.append(request.form['nombre'])
    return render_template(
        'tareas.html',
        tareas=enumerate(lista_tareas)
    )


@app.route('/eliminar/<int:posicion>')
def eliminar(posicion):
    del lista_tareas[posicion]
    return redirect('/')


@app.route('/editar/<int:posicion>', methods=['GET', 'POST'])
def editar(posicion):
    if request.method == 'POST':
        lista_tareas[posicion] = request.form['nombre']
        return redirect('/')

    return render_template(
        'editar.html',
        tarea=lista_tareas[posicion]
    )


app.run(debug=True)
