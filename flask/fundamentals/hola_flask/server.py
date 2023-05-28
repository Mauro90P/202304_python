# Importa Flask para permitirnos crear nuestra aplicación
from flask import Flask, render_template

# Crea una nueva instancia de la clase Flask llamada "app"
app = Flask(__name__)


# El decorador "@" asocia esta ruta con la función inmediatamente siguiente

# TAREA 1

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta
# sentencias import, tal vez algunas otras rutas

# Con esta ruta podemos ingresar cualquier nombre y se mostrara en la pantalla


@app.route('/hola/<name>')
def hola(name):
    return "Hola, " + name

# TAREA 2


@app.route('/dojo')
def dojo():
    return "¡Dojo!"

# TAREA 3


@app.route('/say/flask')
def flask():
    return "¡Hola,Flask!"


@app.route('/say/Michael')
def Michael():
    return "¡Hola,Michael!"


@app.route('/say/jhon')
def jhon():
    return "¡Hola,Jhon"


# @app.route('/gatos')
# def gatos():
#     return render_template('index.html')

# TAREA 4

# EN ESTA TAREA AL CAMBIAR EL VALOR DEL DIGITO NUMERICO Y NOMBRE REPETIRA EL NOMBRE LAS VECES QUE EL INDIQUE EL VALOR NUMERICO


@app.route('/<int:largo>/<string:name>')
def rang(largo, name):
    respuesta = ''
    for num in range(largo):
        respuesta += name
    return respuesta


@app.route('/hello/<string:renata>/<int:num>')
def hello(renata, num):
    return render_template('index.html', renata=renata, num=num)


# # app.run(debug=True) debería ser la última sentencia
if __name__ == "__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
