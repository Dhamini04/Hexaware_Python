from dao.order_processor import OrderProcessor
from entity.model.user import User
from entity.model.product import Product
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException

def main():
    service = OrderProcessor("db_config.properties")

    while True:
        print("\n===== ORDER MANAGEMENT MENU =====")
        print("1. Create User")
        print("2. Create Product")
        print("3. Place Order")
        print("4. Cancel Order")
        print("5. View All Products")
        print("6. View Orders by User")
        print("7. Exit")
        print("==================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (Admin/User): ")
            user = User(0, username, password, role)
            print("User created successfully." if service.create_user(user) else "Failed to create user.")

        elif choice == "2":
            admin_id = int(input("Enter Admin User ID: "))
            name = input("Product Name: ")
            desc = input("Description: ")
            price = float(input("Price: "))
            stock = int(input("Quantity in Stock: "))
            ptype = input("Type (Electronics/Clothing): ")

            if ptype == "Electronics":
                brand = input("Brand: ")
                warranty = int(input("Warranty Period (months): "))
                from entity.model.electronics import Electronics
                product = Electronics(0, name, desc, price, stock, brand, warranty)

            elif ptype == "Clothing":
                size = input("Size: ")
                color = input("Color: ")
                from entity.model.clothing import Clothing
                product = Clothing(0, name, desc, price, stock, size, color)

            else:
                print("Invalid type.")
                continue

            admin_user = User(admin_id, "", "", "Admin")
            try:
                result = service.create_product(admin_user, product)
                print("Product created successfully." if result else "Failed to create product.")
            except UserNotFoundException as e:
                print("Error:", e)

        elif choice == "3":
            user_id = int(input("Enter User ID: "))
            product_ids = input("Enter product IDs (comma separated): ").split(',')
            product_list = []
            for pid in product_ids:
                pid = int(pid.strip())
                qty = int(input(f"Quantity for Product ID {pid}: "))
                product = Product(pid, "", "", 0, qty, "")
                product_list.append(product)

            user = User(user_id, "", "", "")
            try:
                success = service.create_order(user, product_list)
                print("Order placed successfully." if success else "Failed to place order.")
            except UserNotFoundException as e:
                print("Error:", e)

        elif choice == "4":
            uid = int(input("Enter User ID: "))
            oid = int(input("Enter Order ID to cancel: "))
            try:
                if service.cancel_order(uid, oid):
                    print("Order cancelled successfully.")
                else:
                    print("Failed to cancel order.")
            except OrderNotFoundException as e:
                print("Error:", e)

        elif choice == "5":
            products = service.get_all_products()
            for p in products:
                print(p)

        elif choice == "6":
            user_id = int(input("Enter User ID: "))
            user = User(user_id, "", "", "")
            orders = service.get_order_by_user(user)
            for order in orders:
                print(order)

        elif choice == "7":
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
