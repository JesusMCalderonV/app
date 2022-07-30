from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/parque_tayrona')
def parque():
    return render_template('parque_tayrona.html')

@app.route('/santa_marta')
def san():
    return render_template('santa_marta.html')

@app.route('/minca')
def min():
    return render_template('/')

@app.route('/ciudad_perdida')
def ciu():
    return render_template('ciudad_perdida.html')

@app.route('/palomino')
def palo():
    return render_template('palomino')

@app.route('/tours')
def tour():
    return render_template('tours.html')

if __name__ == "__main__":
    app.run(debug=True)