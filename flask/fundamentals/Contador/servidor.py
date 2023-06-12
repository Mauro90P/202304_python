from flask import Flask, render_template

app = Flask(__name__)


contador = 1


@app.route('/')
def index():
    return render_template('index.html', contador=contador)


@app.route('/sumar')
def sumar():
    global contador
    contador += 1
    return str(contador)


@app.route('/reset')
def reset():
    global contador
    contador = 1
    return str(contador)


if __name__ == "__main__":
    app.run(debug=True)
