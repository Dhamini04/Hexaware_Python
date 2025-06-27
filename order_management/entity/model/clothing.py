from entity.model.product import Product

class Clothing(Product):
    def __init__(self, product_id: int, product_name: str, description: str,
                 price: float, quantity_in_stock: int, size: str, color: str):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, "Clothing")
        self.size = size
        self.color = color
