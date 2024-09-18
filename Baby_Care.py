from Product import Product # Importa la clase Product desde el modulo Product.

class Baby_Care(Product):
    def __init__(self, id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date, recommended_age, brand, hypoallergenic):
        super().__init__(id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date)
        # Llama al constructor de la clase padre (Product)

        self.recommended_age = recommended_age  #Inicializa la edad recomendada
        self.brand = brand                      #Inicializa la marca del producto
        self.hypoallergenic = hypoallergenic    #Inicializa si el producto es hipoalergenico.
