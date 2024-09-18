from Employee import Employee  #Importa la clase Employee desde el modulo Employee
from Product import Product  #Importa la clase Product desde el modulo Product
from Supplier import Supplier  # Importa la clase Supplier desde el modulo Supplier.
from Product_Management import Product_Management  #Importa la clase Product_Management desde el modulo Product_Management.
from Supplier_Management import Supplier_Management  # Importa la clase Supplier_Management desde el modulo Supplier_Management
from Employee_Management import Employee_Management  #Importa la clase Employee_Management desde el modulo Employee_Management

class Manager(Employee):

    def manage_product(self, id_product: int, product: Product, action: str, product_manager: Product_Management):
        if action == "Agregar":
            product_manager.add_product(product)  #Llama al metodo add_product de Product_Management para agregar un producto.
        elif action == "Delete":
            product_manager.delete_product(id_product)  # Llama al metodo delete_product de Product_Management para eliminar un producto
        elif action == "Modificar":
            product_manager.modify_product(id_product, product)  #Llama al metodo modify_product de Product_Management para modificar un producto.
        else:
            print("Accion no valida")  #Imprime un mensaje si la accion no es valida

    def manage_supplier(self, id_supplier: int, supplier: Supplier, action: str, supplier_manager: Supplier_Management):
        if action == "Agregar":
            supplier_manager.add_supplier(supplier)  #Llama al metodo add_supplier de Supplier_Management para agregar un proveedor
        elif action == "Delete":
            supplier_manager.delete_supplier(id_supplier)  #Llama al metodo delete_supplier de Supplier_Management para eliminar un proveedor.
        elif action == "Modificar":
            supplier_manager.modify_supplier(id_supplier, supplier)  #Llama al metodo modify_supplier de Supplier_Management para modificar un proveedor
        else:
            print("Accion no valida")  #Imprime un mensaje si la accion no es valida

    def manage_employee(self, id_employee: int, employee: Employee, action: str, employee_manager: Employee_Management):
        if action == "Agregar":
            employee_manager.add_employee(employee)  # Llama al metodo add_employee de Employee_Management para agregar un empleado
        elif action == "Delete":
            employee_manager.delete_employee(id_employee)  #Llama al metodo delete_employee de Employee_Management para eliminar un empleado.
        elif action == "Modificar":
            employee_manager.modify_employee(id_employee, employee)  #Llama al metodo modify_employee de Employee_Management para modificar un empleado
        else:
            print("Accion no valida")  # Imprime un mensaje si la accion no es valida.
