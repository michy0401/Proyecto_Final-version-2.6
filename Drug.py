from Product import Product  # Importa la clase Product desde el modulo Product.

class Drug(Product):
    def __init__(self, id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date, prescription_required):
        super().__init__(id_product, name_product, presentation_type, quantity, product_category, unit_cost, product_price, expiration_date)
        # Llama al constructor de la clase padre (Product) con los parametros proporcionados.

        self.prescription_required = prescription_required
        # Inicializa el atributo que indica si se requiere receta medica para este medicamento.

