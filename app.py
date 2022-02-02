from distutils.util import execute
from subprocess import REALTIME_PRIORITY_CLASS
from flask import Flask, request,render_template, redirect, url_for
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='solicitudes'
mysql.init_app(app)

@app.route('/')
def loggin():
    return render_template('Inicio.html')

@app.route('/dashboard')
def dash():
    return render_template('Dashboard.html')

@app.route('/registro')
def registro():
    return render_template('Registro.html')

@app.route("/error")
def errorConexion():
    return render_template('ErrorConexion.html')

@app.route('/', methods=['POST'])
def Autenticate():

    username = request.form['u']
    password = request.form['p']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM User WHERE username='" + username + "' and password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return render_template('ErrorConexion.html')
    else:
        return render_template('Dashboard.html')

@app.route('/autentication', methods=['POST'])
def autentication():
    _usuario=request.form['txtUsuario']
    _contraseña=request.form['txtContraseña']

    sql ="INSERT INTO `User` (`username`, `password`) VALUES (%s,%s);"
    
    datos=(_usuario,_contraseña)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)