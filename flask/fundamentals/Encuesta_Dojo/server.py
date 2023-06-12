from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/login')
def login():

    if 'usuario' in session:
        return redirect('/')
        

    return render_template('login.html')

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
        usuario = {
            'nombre': request.form['name'],
            'ubicacion': request.form['ubicacion'],
            'lenguaje': request.form['lenguaje'],
            'comentario': request.form['comentario']
        }
        session['usuario'] = usuario
        return redirect('resultado')
    
@app.route('/resultado')
def resultado():
    # Código para obtener los datos del usuario...
    usuario = session.get('usuario', None)
    if usuario is None:
         return redirect('/login')
    return render_template('inicio.html', usuario=usuario)

@app.route('/salir')
def salir():
    session.clear()
    flash('Haz vuelto al registro de la encuesta!', 'info')
    return redirect('/login')


if __name__=="__main__":
    app.run(debug=True, port='5001')   