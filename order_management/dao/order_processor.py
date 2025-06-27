import mysql.connector
from datetime import date
from dao.i_order_management_repository import IOrderManagementRepository
from entity.model.user import User
from entity.model.product import Product
from entity.model.order import Order
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException
from util.db_conn_util import get_connection

class OrderProcessor(IOrderManagementRepository):

    def __init__(self, config_path):
        self.connection = get_connection(config_path)
        self.cursor = self.connection.cursor(dictionary=True)

    def create_user(self, user: User) -> bool:
        try:
            self.cursor.execute("INSERT INTO User (username, password, role) VALUES (%s, %s, %s)",
                                (user.username, user.password, user.role))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error creating user:", e)
            return False

    def create_product(self, user: User, product: Product) -> bool:
        try:
            # Check if user is admin
            self.cursor.execute("SELECT * FROM User WHERE userId = %s AND role = 'Admin'", (user.user_id,))
            if not self.cursor.fetchone():
                raise UserNotFoundException("Admin user not found.")

            self.cursor.execute("""INSERT INTO Product 
                (productName, description, price, quantityInStock, type, brand, warrantyPeriod, size, color)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (product.product_name, product.description, product.price, product.quantity_in_stock,
                 product.type, getattr(product, 'brand', None), getattr(product, 'warranty_period', None),
                 getattr(product, 'size', None), getattr(product, 'color', None)))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error creating product:", e)
            return False

    def create_order(self, user: User, product_list: list[Product]) -> bool:
        try:
            self.cursor.execute("SELECT * FROM User WHERE userId = %s", (user.user_id,))
            if not self.cursor.fetchone():
                raise UserNotFoundException("User not found.")

            today = date.today()
            self.cursor.execute("INSERT INTO Orders (userId, orderDate) VALUES (%s, %s)",
                                (user.user_id, today))
            order_id = self.cursor.lastrowid

            for product in product_list:
                self.cursor.execute("SELECT price FROM Product WHERE productId = %s", (product.product_id,))
                result = self.cursor.fetchone()
                if result:
                    total_price = result['price'] * product.quantity_in_stock
                    self.cursor.execute("""INSERT INTO OrderItems (orderId, productId, quantity, totalPrice)
                                           VALUES (%s, %s, %s, %s)""",
                                        (order_id, product.product_id, product.quantity_in_stock, total_price))

            self.connection.commit()
            return True
        except Exception as e:
            print("Error creating order:", e)
            self.connection.rollback()
            return False

    def cancel_order(self, user_id: int, order_id: int) -> bool:
        try:
            self.cursor.execute("SELECT * FROM Orders WHERE orderId = %s AND userId = %s",
                                (order_id, user_id))
            if not self.cursor.fetchone():
                raise OrderNotFoundException("Order not found for given user.")

            self.cursor.execute("DELETE FROM OrderItems WHERE orderId = %s", (order_id,))
            self.cursor.execute("DELETE FROM Orders WHERE orderId = %s", (order_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error cancelling order:", e)
            self.connection.rollback()
            return False

    def get_all_products(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM Product")
            return self.cursor.fetchall()
        except Exception as e:
            print("Error retrieving products:", e)
            return []

    def get_order_by_user(self, user: User) -> list:
        try:
            self.cursor.execute("SELECT * FROM Orders WHERE userId = %s", (user.user_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print("Error fetching user orders:", e)
            return []
