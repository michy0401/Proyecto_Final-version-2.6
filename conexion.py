import mariadb
import sys

class Registro_datos:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        try:
            self.conexion = mariadb.connect(
                host='localhost',
                database='Drogueria_inventario', 
                user='root',
                password='d040104a'
            )
        except mariadb.Error as e:
            print(f"Error conectando a la base de datos: {e}")
            sys.exit(1)

    def get_connection(self):
        if not hasattr(self, 'conexion') or self.conexion is None:
            self.create_connection()
        return self.conexion

    def busca_usuario(self, user, password):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            sql = "SELECT * FROM user WHERE user = %s AND password = %s"
            cur.execute(sql, (user, password))
            usuario = cur.fetchone()
            return usuario
        except mariadb.Error as e:
            print(f"Error al buscar usuario: {e}")
            return None
        finally:
            cur.close()

    def busca_empleado(self, id_user):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            sql = """
                SELECT 
                    e.name_employee AS 'Employee Name',
                    jt.job_title AS 'Job Title'
                FROM 
                    employee e
                JOIN 
                    job_title jt ON e.id_job_title = jt.id_job_title
                WHERE 
                    e.id_user = %s
            """
            cur.execute(sql, (id_user,))
            empleado = cur.fetchone()
            return empleado
        except mariadb.Error as e:
            print(f"Error al buscar empleado: {e}")
            return None
        finally:
            cur.close()

    def insert_data(self, query, values):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            print(f"Ejecutando: {query} con {values}")
            cursor.execute(query, values)
            conn.commit()
        except mariadb.Error as e:
            print(f"Error al insertar: {e}")
        finally:
            cursor.close()

    def execute_query(self, query, params=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            return results
        except mariadb.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        finally:
            cursor.close()
            
    def cursor(self):
        return self.conexion.cursor()
    
    def commit(self):
        self.conexion.commit()
        
    def cerrar_conexion(self):
        if hasattr(self, 'conexion') and self.conexion:
            self.conexion.close()
