from abc import ABC, abstractmethod
from entity.model.user import User
from entity.model.product import Product
from entity.model.order import Order

class IOrderManagementRepository(ABC):

    @abstractmethod
    def create_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def create_product(self, user: User, product: Product) -> bool:
        pass

    @abstractmethod
    def create_order(self, user: User, product_list: list[Product]) -> bool:
        pass

    @abstractmethod
    def cancel_order(self, user_id: int, order_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_products(self) -> list:
        pass

    @abstractmethod
    def get_order_by_user(self, user: User) -> list:
        pass
