import mysql.connector
from util.db_property_util import get_property_string

def get_connection(file_path: str):
    props = get_property_string(file_path)
    conn = mysql.connector.connect(
        host=props["host"],
        port=props["port"],
        user=props["username"],
        password=props["password"],
        database=props["dbname"]
    )
    return conn

