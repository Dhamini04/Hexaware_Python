class Product:
    def __init__(self, product_id: int, product_name: str, description: str,
                 price: float, quantity_in_stock: int, type: str):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.type = type  # "Electronics" or "Clothing"
