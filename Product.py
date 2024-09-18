class Product:
    def __init__(self, id_product=None, id_presentation_type=None, id_category_product=None, id_supplier=None,
                 name_product=None, quantity=None, unit_cost=None, product_price=None,
                 expiration_date=None, id_brand_product=None, id_flavor_product=None,
                 required_prescription=None, recommended_age=None, instruction=None, guarantee=None):
        self.id_product = id_product
        self.id_presentation_type = id_presentation_type
        self.id_category_product = id_category_product
        self.id_supplier = id_supplier
        self.name_product = name_product
        self.quantity = quantity
        self.unit_cost = unit_cost
        self.product_price = product_price
        self.expiration_date = expiration_date
        self.id_brand_product = id_brand_product
        self.id_flavor_product = id_flavor_product
        self.required_prescription = required_prescription
        self.recommended_age = recommended_age
        self.instruction = instruction
        self.guarantee = guarantee
