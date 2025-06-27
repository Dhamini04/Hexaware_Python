class OrderItem:
    def __init__(self, order_item_id: int, order_id: int, product_id: int, quantity: int, total_price: float):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
