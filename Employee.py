from User import User  #Importa la clase User desde el modulo User.
from Product import Product  #Importa la clase Product desde el modulo Product.
from Supplier import Supplier  # Importa la clase Supplier desde el modulo Supplier.
from Product_Management import Product_Management  #Importa la clase Product_Management desde el modulo Product_Management.
from Supplier_Management import Supplier_Management  # Importa la clase Supplier_Management desde el modulo Supplier_Management.
from typing import Optional  #Importa Optional desde typing.

class Employee(User):

    def __init__(self, user, password, id_employee, name_employee, address, email, job_title):
        super().__init__(user, password)  # Llama al constructor de la clase padre (User)
        self.id_employee = id_employee  #Inicializa el ID del empleado
        self.name_employee = name_employee  # Inicializa el nombre del empleado
        self.address = address  #Inicializa la direccion del empleado
        self.email = email  # Inicializa el correo del empleado
        self.job_title = job_title  #Inicializa el cargo del empleado

    def search_product(self, name: str, product_manager: Product_Management) -> Optional[Product]:
        product = product_manager.search_product(name)  # Llama al metodo search_product de Product_Management para buscar un producto por nombre.
        if product:
            print(f"Producto: {product.name_product}")  #Imprime el nombre del producto si se encuentra
        else:
            print(f"Producto {name} no encontrado")  #Imprime un mensaje si el producto no es encontrado.
        return product  # Devuelve el producto encontrado o None si no se encuentra

    def add_product(self, product: Product, product_manager: Product_Management):
        product_manager.add_product(product)  # Llama al metodo add_product de Product_Management para añadir un producto
        print(f"Producto {product.name_product} fue añadido por {self.name_employee}")  # Imprime un mensaje indicando que el producto fue añadido por el empleado.

    def search_supplier(self, name: str, supplier_manager: Supplier_Management) -> Optional[Supplier]:
        supplier = supplier_manager.search_supplier(name)  #Llama al metodo search_supplier de Supplier_Management para buscar un proveedor por nombre.
        if supplier:
            print(f"Proveedor {supplier.name}")  #Imprime el nombre del proveedor si se encuentra
        else:
            print(f"Proveedor {name} no encontrado")  # Imprime un mensaje si el proveedor no es encontrado
        return supplier  # Devuelve el proveedor encontrado o None si no se encontro

