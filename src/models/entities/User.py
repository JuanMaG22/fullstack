from werkzeug.security import check_password_hash
from flask_login import UserMixin

#Es el reflejo que esta en la base de datos
class User(UserMixin):
##Sirve las entidades y la autenticacion
    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

#Este va a estar guardado despues de pasar por el hash
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)



