from conexion import Registro_datos  #Importa la clase Registro_datos desde el modulo conexion

class User:

    def __init__(self, user, password):
        self.user = user  #Inicializa el nombre de usuario
        self.password = password  #Inicializa la contrasenya
        self.log_in_status = False  #Inicializa el estado de inicio de sesion como falso
        self.data_base = Registro_datos()  #Inicializa una instancia de la clase Registro_datos para la conexion a la base de datos
    
    def Verified_status(self):
        user_typed = self.data_base.busca_users(self.user)  #Busca el usuario en la base de datos
        if user_typed:
            password_typed = user_typed[0][2]  # Obtiene la contrasenya almacenada para el usuario encontrado
            if password_typed == self.password:
                self.log_in_status = True  #Establece el estado de inicio de sesion como verdadero
                print("Ha ingresado con exito")  # Imprime un mensaje de exito de inicio de sesion
                return user_typed[0]  #Devuelve los datos del usuario encontrado
            else:
                self.log_in_status = False  #Establece el estado de inicio de sesion como falso
                print("El usuario o contrasena ingresado es incorrecto")  #Imprime un mensaje de error si la contrasenya no coincide
        return None  # Devuelve None si el usuario no se encuentra en la base de datos.


