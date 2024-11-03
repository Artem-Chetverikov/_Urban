import sqlite3


def initiate_db():
    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL,
    pictures TEXT NOT NULL
    )
    ''')
    connection.close()


def get_all_products():
    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    users = cursor.fetchall()
    connection.close()
    return users


def insert_all_products():
    prod = [['Product1', 'описание 1', 100, 'pictures/Product1_300x300.jpg'],
            ['Product2', 'описание 2', 200, 'pictures/Product2_300x300.jpg'],
            ['Product3', 'описание 3', 300, 'pictures/Product3_300x300.jpg'],
            ['Product4', 'описание 4', 400, 'pictures/Product4_300x300.jpg']]

    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()

    for prod_i in prod:
        cursor.execute("INSERT INTO Products (title, description, price, pictures) VALUES (?, ?, ?, ?)",
                       (f'{prod_i[0]}', f'{prod_i[1]}', f'{prod_i[2]}', f'{prod_i[3]}')
                       )
    connection.commit()
    connection.close()


def delete_all_products():
    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()
    cursor.execute("DELETE * FROM Products")
    connection.commit()
    connection.close()

# initiate_db()
# insert_all_products()
# delete_all_products()

