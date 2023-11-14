# main.py
from flask import Flask, render_template
from holamundo import obtener_mensaje

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Obtener el DataFrame desde holamundo.py
    df = obtener_mensaje()

    # Renderizar el DataFrame en HTML y devolverlo como respuesta
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
