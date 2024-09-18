from Product import Product  #Importa la clase Product desde el modulo Product

class Medical_Device(Product):
    def __init__(self, id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date, instruction, guarantee):
        super().__init__(id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date)
        self.instruction = instruction #Inicializa las instrucciones del dispositivo medico
        self.guarantee = guarantee #Inicializa la garantia del dispositivo medico
