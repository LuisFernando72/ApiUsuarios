from capa_acceso_datos.db import conexion
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class usuario():
    def __init__(self):
        pass
    
    def seleccionarUsuarios(self):
        result = []
        cursor = conexion.cursor()
        resultados = cursor.execute("select * from usuarios;")
        for row in resultados.fetchall():
            item_dict = {}
            item_dict["id"] = str(row[0])
            item_dict["nombres"] = row[1]
            item_dict["apellidos"] = row[2]
            item_dict["password"] = row[3]
            item_dict["fecha"] = row[4]
            result.append(item_dict)
        cursor.close()
        return result
    
    def buscarUsuario(self, id_usuario):
        cursor = conexion.cursor()
        resultados = cursor.execute(
        "select * from usuarios where id_usuario=" + id_usuario)
        usar = resultados.fetchmany(1)
     
        for row in usar:
            item_dict = {}
            item_dict["id"] = str(row[0])
            item_dict["nombres"] = str(row[1])
            item_dict["apellidos"] = str(row[2])
            item_dict["password"] = str(row[3])
            item_dict["fecha"] = str(row[4])
            
        return item_dict
    
    
    
    def insertarUsuario(self, nombres, apellidos, password, fecha_insert):
        cursorInsert = conexion.cursor()
        fecha = datetime.date.today()
        fechahoy = str(fecha.year) + "-" + str(fecha.month)+"-" + str(fecha.day)
        contra = generate_password_hash(password, "pbkdf2:sha256:10", 10)

        consulta = "insert into usuarios(nombres,apellidos, password, fecha_creacion) values(?,?,?,?)"
        cursorInsert.execute(
        consulta, nombres, apellidos, contra, fechahoy)

        cursorInsert.commit()
        return 1
        
    def actualizarUsuario(self,nombres, apellidos, password, id_usuario):
        pass_enc = generate_password_hash(
        password, "pbkdf2:sha256:10", 10)  
        cursor = conexion.cursor()
        consulta = "update usuarios set nombres = ?,apellidos=?, password = ? where id_usuario = ?; "
        resultado = cursor.execute(
        consulta, nombres, apellidos, pass_enc,id_usuario)

        resultados = cursor.execute(
        "select * from usuarios where id_usuario=" + id_usuario)
        usar = resultados.fetchmany(1)
        for row in usar:
            item_dict = {}
            item_dict["id"] = str(row[0])
            item_dict["nombres"] = str(row[1])
            item_dict["apellidos"] = str(row[2])
            item_dict["password"] = str(row[3])
            item_dict["fecha"] = str(row[4])
        return item_dict
    
    def eliminarUsuario(self, id_usuario):
        cursor = conexion.cursor()
        resultado = cursor.execute(
        "delete from usuarios where id_usuario=" + id_usuario)
        cursor.commit()
        return 1