from flask import Flask

app = Flask(__name__)


@app.route('/play/<color>/<int:num>')
def play(color, num):
    if num < 1:
        return 'El número debe ser mayor que cero'

    html = ''
    for i in range(num):
        html += f'<div style="background-color:{color}; width:300px; height:300px; margin:20px; display:inline-block;"></div>'

    return html

# Mostrar 3 cuadros azules cuando este solo play


@app.route('/play')
def game(num=None):
    if num is None:
        num = 3
    colors = ["blue"]
    boxes = ""
    for i in range(num):
        color = colors[i % len(colors)]
        boxes += f'<div style="background-color:{color}; width:300px; height:300px; margin:20px; display:inline-block;"></div>'
    return boxes


if __name__ == "__main__":
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
