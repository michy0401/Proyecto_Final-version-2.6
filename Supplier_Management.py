from Supplier import Supplier  #Importa la clase Supplier desde el modulo Supplier
from typing import List, Optional  #Importa List y Optional desde typing

class Supplier_Management:
    def __init__(self):
        self.suppliers: List[Supplier] = []  #Inicializa una lista vacia de proveedores

    def add_supplier(self, supplier: Supplier):
        self.suppliers.append(supplier)  #Agrega un proveedor a la  lista
        print(f"{supplier.name} ha sido agregado con exito")  #Imprime un mensaje de exito al agregar proveedor

    def delete_supplier(self, id_supplier: int):
        for supplier in self.suppliers:
            if supplier.id_supplier == id_supplier:
                self.suppliers.remove(supplier)  #Elimina un proveedor de la lista.
                print(f"{supplier.name} ha sido eliminado con exito")  # Imprime un mensaje de exito al eliminar proveedor
                return
        print(f"Proveedor {id_supplier} no encontrado")  # Imprime un mensaje si el proveedor no se encuentra

    def modify_supplier(self, id_supplier: int, updated_supplier: Supplier):
        for i, supplier in enumerate(self.suppliers):
            if supplier.id_supplier == id_supplier:
                self.suppliers[i] = updated_supplier  #Modifica un proveedor en la lista
                print(f"{updated_supplier.name} ha sido actualizado con exito")  #Imprime un mensaje de exito al modificar.
                return
        print(f"Proveedor {id_supplier} no encontrado")  #Imprime un mensaje si el proveedor no se encuentra

    def search_supplier(self, name: str) -> Optional[Supplier]:
        for supplier in self.suppliers:
            if supplier.name == name:
                print(f"Proveedor: {supplier.name}")  #Imprime el nombre del proveedor encontrado
                return supplier  #Devuelve el proveedor encontrado
        print(f"Proveedor {name} no encontrado")  #Imprime un mensaje si el proveedor no se encuentra
        return None  #Devuelve None si el proveedor no es encontrado

