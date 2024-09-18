from Product import Product  #Importa la clase Product desde el modulo Product

class Supplement(Product):
    def __init__(self, id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date, flavor):
        super().__init__(id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date)
        self.flavor = flavor  #Inicializa el sabor del suplemento

