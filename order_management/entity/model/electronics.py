from entity.model.product import Product

class Electronics(Product):
    def __init__(self, product_id: int, product_name: str, description: str,
                 price: float, quantity_in_stock: int, brand: str, warranty_period: int):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, "Electronics")
        self.brand = brand
        self.warranty_period = warranty_period
