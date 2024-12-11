from db_connect.connection import get_db_connection

def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, surname FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users
