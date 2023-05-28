from flask import Flask, render_template

app = Flask(__name__)

# POR DEFECTO AL TOMAR LA URL QUEDA CON 8X8


@app.route('/')
def tablero():
    return render_template('tablero.html', num_rows=8, num_cols=8)

# AL CAMBIAR EL DIGITO EN LA URL, NOS ASIGNA LA CANTIDA DE NUMERO DE CUADROS EN EL CUERPO


@app.route('/<x>')
def sized_checkboard(x):
    return render_template('tablero.html', num_rows=int(x), num_cols=int(x))

# Aca se cambia la cantidad de veces de cuadros en la pantalla


@app.route('/<x>/<y>')
def sized_checkboard_dos_varibles(x, y):
    return render_template('tablero.html', num_rows=int(x), num_cols=int(y))

# Aca se pasan la variables según numero de ingreso y la ruta de cambio de color, esto hace referencia al html donde se dan la logica de color


@app.route('/<x>/<y>/<c1>/<c2>')
def sized_checkboard_dos_varibles_color(x, y, c1, c2):
    return render_template('tablero.html', num_rows=int(x), num_cols=int(y), color_one=c1, color_two=c2)


if __name__ == "__main__":
    app.run(debug=True)
