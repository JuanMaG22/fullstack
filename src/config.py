class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'
    #Nos ayuda para el envio de mensajes, llave privada para el inicio de sesion
    #Usuario no valido

    #Indicar los parametros para la conexion de la base de datos

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'juanmanuelg22'
    MYSQL_PASSWORD = '3117740513s'
    MYSQL_DB = 'flask_login'

config={
    'development':DevelopmentConfig
}