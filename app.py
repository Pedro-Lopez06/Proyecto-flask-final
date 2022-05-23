from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#conexxion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyecto_py'
mysql = MySQL(app)

#settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente')
    datos = cur.fetchall()
    return render_template('agregar.html', clientes = datos)

@app.route('/agregar_clientes', methods=['POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        localidad = request.form['localidad']
        ip_wam = request.form['ip_wam']
        ip_lan = request.form['ip_lan']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO cliente (nombre, apellido, direccion, telefono, localidad, ip_wam, ip_lan) VALUES (%s, %s, %s, %s, %s, %s, %s)',
        (nombre, apellido, direccion, telefono, localidad, ip_wam, ip_lan))
        mysql.connection.commit()
        flash('Cliente Registrado')
        return redirect(url_for('Index'))

@app.route('/eliminar/<string:id>')
def borrar(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cliente WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Cliente Eliminado')
    return redirect(url_for('Index'))


@app.route('/actualizar/<id>')
def get_cliente(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente WHERE id = %s',[id])
    dato = cur.fetchall()
    print(dato[0])
    return render_template('editar_cliente.html', cliente = dato[0])

@app.route('/actualizar/<id>', methods = ['POST'])
def actu_cliente(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        localidad = request.form['localidad']
        ip_wam = request.form['ip_wam']
        ip_lan = request.form['ip_lan']
        cur = mysql.connection.cursor()
        cur.execute(""" 
        UPDATE cliente
        SET nombre = %s, 
        apellido = %s, 
        direccion = %s,
        telefono = %s,
        localidad = %s, 
        ip_wam = %s,
        ip_lan = %s
        WHERE id = %s 
        """,(nombre, apellido, direccion, telefono, localidad, ip_wam, ip_lan, id))
        mysql.connection.commit()
        flash('Cliente Actualizado')
        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=3000, debug= True)