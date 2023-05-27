# Importa Flask para permitirnos crear nuestra aplicación
from flask import Flask
# Crea una nueva instancia de la clase Flask llamada "app"
app = Flask(__name__)

# El decorador "@" asocia esta ruta con la función inmediatamente siguiente


@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'           # Devuelve la cadena '¡Hola Mundo!' como respuesta


if __name__ == "__main__":        # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente
    # Ejecuta la aplicación en modo de depuración
    app.run(debug=True)

""" @app.reoute('/hello/<string:banana>/<int:num>')
def hello(banana, num):
    return f"Hello{banana * num}"
@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id



@app.route('/hola/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def hola(name):
    print(name)
    return "Hola, " + name

 """
