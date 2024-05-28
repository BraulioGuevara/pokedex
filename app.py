from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'templates')
#options = ['Ninguno','Acero','Agua','Bicho','Dragon','Electrico','Fantasma','Fuego','Hada','Hielo','Lucha','Normal','Planta','Psiquico','Roca','Siniestro','Tierra','Veneno','Volador']

def get_types():
    cursor = db.database.cursor()
    cursor.execute("SELECT nombre_tipo FROM tipos")
    myresult = cursor.fetchall()
    cursor.close()
    
    lista = []

    for i in range(len(myresult)):
        placeholder = str(myresult[i])
        placeholder = placeholder.strip("'(),")
        lista.append(placeholder)


    return lista

def buscar_tipo(options,tipo):
    for i in range(len(options)):
        if tipo == options[i] :
            iden = i
            break
    return iden

app = Flask(__name__, template_folder = template_dir)

 

#Rutas de la aplicación
@app.route('/')
def home():
    options = get_types()
    cursor = db.database.cursor()
    cursor.execute("SELECT p.id, p.nombre, p.peso, p.altura,p.descripcion, t1.nombre_tipo AS tipo_1, t2.nombre_tipo AS tipo_2 FROM pokemon p LEFT JOIN tipos t1 ON p.id_tipo1 = t1.id LEFT JOIN tipos t2 ON p.id_tipo2 = t2.id;")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()

    

    return render_template('index.html', data=insertObject, options=options)

#Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    options = get_types()
    id_ = int(request.form['id'])
    nombre = request.form['nombre']
    peso = request.form['peso']
    altura = request.form['altura']
    desc = request.form['descripcion']
    tipo1 = buscar_tipo(options,request.form.get('tipo_1'))
    tipo2 = buscar_tipo(options,request.form.get('tipo_2'))

    if id_ and nombre and peso and altura and desc and tipo1 and tipo2:
        cursor = db.database.cursor()
        sql = "INSERT INTO pokemon (id,nombre, peso, altura,descripcion,id_tipo1,id_tipo2) VALUES (%s, %s, %s,%s, %s, %s, %s)"
        data = (id_,nombre, peso, altura,desc,tipo1,tipo2)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))





@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM pokemon WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    options = get_types()
    nombre = request.form['nombre']
    peso = request.form['peso']
    altura = request.form['altura']
    desc = request.form['descripcion']
    tipo1 = buscar_tipo(options,request.form.get('tipo_1'))
    tipo2 = buscar_tipo(options,request.form.get('tipo_2'))

    if nombre and peso and altura and desc and tipo1 and tipo2:
        cursor = db.database.cursor()
        sql = "UPDATE pokemon SET nombre = %s, peso = %s, altura = %s, descripcion = %s, id_tipo1 = %s , id_tipo2 = %s WHERE id = %s"
        data = (nombre, peso, altura,desc,tipo1,tipo2, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)