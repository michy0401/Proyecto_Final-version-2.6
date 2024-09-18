from Product import Product
from typing import List, Tuple
import mariadb


class Product_Management:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_product(self, product: Product):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO product (id_presentation_type, id_category_product, id_supplier, name_product,
                            quantity, unit_cost, product_price, expiration_date, id_brand_product,
                            id_flavor_product, required_prescription, recommended_age, instruction, guarantee)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (product.id_presentation_type, product.id_category_product, product.id_supplier, product.name_product,
                product.quantity, product.unit_cost, product.product_price, product.expiration_date,
                product.id_brand_product, product.id_flavor_product, product.required_prescription,
                product.recommended_age, product.instruction, product.guarantee)
        cursor.execute(query, values)
        conn.commit()
        product.id_product = cursor.lastrowid  # Obtiene el ID del último producto insertado
        cursor.close()
        print(f"{product.name_product} ha sido añadido con éxito con ID {product.id_product}")

    def search_all_products(self):
        try:
            with self.db_connection.get_connection().cursor() as cursor:
                query = """
                SELECT p.id_product, p.name_product, p.product_price, 
                       pt.presentation_type
                FROM product p
                JOIN presentation_type pt ON p.id_presentation_type = pt.id_presentation_type
                """
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            raise Exception(f"Error en la búsqueda de productos: {str(e)}")

    def search_product(self, search_term: str):
        try:
            with self.db_connection.get_connection().cursor() as cursor:
                if search_term.isdigit():  # Verifica si el término de búsqueda es un número
                    query = """
                    SELECT p.id_product, p.name_product, p.product_price, 
                           pt.presentation_type
                    FROM product p
                    JOIN presentation_type pt ON p.id_presentation_type = pt.id_presentation_type
                    WHERE p.id_product = %s
                    """
                    cursor.execute(query, (int(search_term),))
                else:
                    query = """
                    SELECT p.id_product, p.name_product, p.product_price, 
                           pt.presentation_type
                    FROM product p
                    JOIN presentation_type pt ON p.id_presentation_type = pt.id_presentation_type
                    WHERE p.name_product LIKE %s
                    """
                    cursor.execute(query, (f"%{search_term}%",))
                return cursor.fetchall()
        except Exception as e:
            raise Exception(f"Error en la búsqueda de productos: {str(e)}")

    def delete_product(self, id_product):
        try:
            conn = self.db_connection.get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM product WHERE id_product = %s"  # Asegúrate de usar el nombre correcto de la columna
            cursor.execute(query, (id_product,))
            conn.commit()
            cursor.close()
            print(f"Producto con ID {id_product} ha sido eliminado con éxito")
        except mariadb.Error as e:
            print(f"Error al eliminar el producto: {e}")



    def modify_product(self, product):
        cursor = self.db_connection.cursor()
        query = """UPDATE product SET id_presentation_type=%s, id_category_product=%s, id_supplier=%s, name_product=%s, quantity=%s, unit_cost=%s, product_price=%s, expiration_date=%s, id_brand_product=%s, id_flavor_product=%s, required_prescription=%s, recommended_age=%s, instruction=%s, guarantee=%s
                   WHERE id_product=%s"""
        values = (product.id_presentation_type, product.id_category_product, product.id_supplier, product.name_product, product.quantity, product.unit_cost, product.product_price, product.expiration_date, product.id_brand_product, product.id_flavor_product, product.required_prescription, product.recommended_age, product.instruction, product.guarantee, product.id_product)
        cursor.execute(query, values)
        self.db_connection.commit()

    def get_product_by_id(self, product_id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM product WHERE id_product = %s"
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        if result:
            product = Product(
                id_product=result[0],
                id_presentation_type=result[1],
                id_category_product=result[2],
                id_supplier=result[3],
                name_product=result[4],
                quantity=result[5],
                unit_cost=result[6],
                product_price=result[7],
                expiration_date=result[8],
                id_brand_product=result[9],
                id_flavor_product=result[10],
                required_prescription=result[11],
                recommended_age=result[12],
                instruction=result[13],
                guarantee=result[14]
            )
            return product
        return None

    def load_all_products(self):
        try:
            return self.search_all_products()
        except Exception as e:
            raise Exception(f"Error al cargar los productos: {str(e)}")

    def get_all_products(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM product")
        results = cursor.fetchall()
        products = [
            Product(
                id_product=row[0],
                id_presentation_type=row[1],
                id_category_product=row[2],
                id_supplier=row[3],
                name_product=row[4],
                quantity=row[5],
                unit_cost=row[6],
                product_price=row[7],
                expiration_date=row[8],
                id_brand_product=row[9],
                id_flavor_product=row[10],
                required_prescription=row[11],
                recommended_age=row[12],
                instruction=row[13],
                guarantee=row[14]
            )
            for row in results
        ]
        return products