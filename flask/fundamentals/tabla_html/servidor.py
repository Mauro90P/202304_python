from flask import Flask, render_template

app = Flask(__name__)


@app.route('/principal')
def principal():
    return render_template('index.html')


@app.route('/contacto')
def contacto():

    list_usuarios = [
        {
            "nombre": "Mauricio",
            "apellido": "Pardo",
            "id": 1,
        },
        {
            "nombre": "Juan",
            "apellido": "Lopez",
            "id": 2,
        },
        {
            "nombre": "Bernardo",
            "apellido": "Jerez",
            "id": 3,
        }

    ]
    return render_template('contacto.html', usuarios=list_usuarios)


if __name__ == "__main__":
    app.run(debug=True)
