from .entities.User import User

class ModelUser():
##metodo para recibir variable de conexion y el usuario para la autenticacion
##Los datos de la base de datos, va con user.py
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                ##Comprabar password
                #print(user.password)
                #quit()
                user = User(row[0], row[1], row[2] == user.password, row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

##mostrar los datos del usuario ya logeado
@classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)