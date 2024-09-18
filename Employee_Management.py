from Employee import Employee  #Importa la clase Employee desde el modulo Employee.
from typing import List, Optional  #Importa List y Optional

class Employee_Management:
    def __init__(self):
        self.employees: List[Employee] = []  #Inicializa una lista vacia de empleados.

    def add_employee(self, employee: Employee):
        self.employees.append(employee)  #Agrega un empleado a la lista.
        print(f"{employee.name_employee} ha sido añadido con exito")  # Imprime un mensaje de exito al agregar al empleado

    def delete_employee(self, id_employee: int):
        for employee in self.employees:
            if employee.id_employee == id_employee:
                self.employees.remove(employee)  #Elimina un empleado de la lista.
                print(f"{employee.name_employee} ha sido eliminado con exito")  # Imprime un mensaje de exito al eliminar al empleado
                return
        print(f"Empleado {id_employee} no encontrado")  #Imprime un mensaje si el empleado no es encontrado.

    def modify_employee(self, id_employee: int, updated_employee: Employee):
        for i, employee in enumerate(self.employees):
            if employee.id_employee == id_employee:
                self.employees[i] = updated_employee  #Modifica un empleado en la lista.
                print(f"Empleado {updated_employee.name_employee} ha sido modificado con exito")  # Imprime un mensaje de exito al modificar al empleado.
                return
        print(f"Empleado {id_employee} no encontrado")  # Imprime un mensaje si el empleado no es encontrado.

    def search_employee(self, name: str) -> Optional[Employee]:
        for employee in self.employees:
            if employee.name_employee == name:
                print(f"Empleado {employee.name_employee}")  # Imprime el nombre del empleado encontrado.
                return employee  #Devuelve el empleado encontrado.
        print(f"Empleado {name} no encontrado")  # Imprime un mensaje si el empleado no se encuentra.
        return None  #Devuelve None si el empleado no se encuentra.
