# RA: 21800179

from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from bd import *
import webbrowser

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'encurtar'

@app.route('/')
def principal():
    return render_template('home.html')

@app.route('/incluir_usuario', methods=['GET','POST'])
def incluindo():
    if request.method == 'POST':
        nnome = request.form.get('nnome')
        nsenha = request.form.get('nsenha')

        conn = mysql.connect()
        cursor = conn.cursor()

        incluindo_usuario(cursor, conn, nnome, nsenha)

        cursor.close()
        conn.close()

        return render_template('urlencurtada.html')
    else:
        return render_template('home.html', erro='Metodo errado!')

@app.route('/reduzir')
def reduzindo():
    return render_template('encurtado.html')

@app.route('/aba_original')
def abrir_original():
    webbrowser.open('https://g1.globo.com/mundo/noticia/2019/05/24/theresa-may-anuncia-sua-renuncia-ao-cargo.ghtml')

if __name__ == '__main__':
    app.run(debug=True)