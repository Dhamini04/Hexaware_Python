# Hexaware_Python
# Order Management System

A command-line Order Management System built in Python with MySQL backend for Hexaware's python coding challenge.

##  Submitted by
- **Name:** Dhamini Machireddy  
- **Trainer:** Karthika Thangaraj  
- **Organization:** Hexavarsity – Hexaware

##  Objective
To design and implement a CLI-based Order Management System using OOP principles, MySQL for backend storage, and Python for business logic and user interaction. This system enables creating users, adding products, placing orders, and tracking them efficiently.

##  Features
- Create User (Admin/User)
- Create Product (Electronics or Clothing)
- Place an Order (Multiple Products)
- Cancel an Order
- View All Products
- View Orders by User
- Error Handling with Custom Exceptions
- DB connection via external configuration file

##  Project Structure

```
OrderManagement/
├── dao/
│   ├── order_processor.py
│   └── i_order_management_repository.py
├── entity/
│   └── model/
│       ├── product.py
│       ├── electronics.py
│       ├── clothing.py
│       ├── user.py
│       ├── order.py
│       └── order_item.py
├── exception/
│   ├── user_not_found_exception.py
│   └── order_not_found_exception.py
├── util/
│   ├── db_conn_util.py
│   └── db_property_util.py
├── main/
│   └── main_module.py
├── db_config.properties
├── requirements.txt
```

##  Technologies Used
- Python 3.11
- MySQL 8.x
- mysql-connector-python
- Visual Studio Code

## How to Run

1. Clone or download this repository  
2. Make sure MySQL server is running  
3. Update `db_config.properties` with your MySQL credentials
4. Run the main module:

```bash
python -m main.main_module
```

##  Notes
- Admin users must be created first to add products  
- Products are classified as Electronics or Clothing using OOP inheritance  
- All data persists in MySQL using foreign key relationships  
- CLI interface enables simple testing and navigation

##  Outcome
A fully functional Order Management CLI system demonstrating OOP, SQL integration, exception handling, and modular coding practices — as required by the Hexaware final project challenge.
