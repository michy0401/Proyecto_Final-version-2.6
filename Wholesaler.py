from Supplier import Supplier  #Importa la clase Supplier desde el modulo Supplier.

class Wholesaler(Supplier):
    def __init__(self, id_supplier, name, phone_number, email, address, shipping_conditions, certification, agent_name, agent_phone_number, agent_email):
        super().__init__(id_supplier, name, phone_number, email, address, shipping_conditions)  #Llama al constructor de la clase padre Supplier
        self.certification = certification  #Inicializa la certificacion del mayorista
        self.agent_name = agent_name  #Inicializa el nombre del agente del mayorista.
        self.agent_phone_number = agent_phone_number  #Inicializa el numero de telefono del agente del mayorista.
        self.agent_email = agent_email  #Inicializa el correo electronico del agente del mayorista


