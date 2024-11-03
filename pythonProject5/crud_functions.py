import sqlite3 as sql


connection = sql.connect('product_base.db')
cursor = connection.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INT NOT NULL
        );
''')
cursor.execute("DELETE FROM Products")
for i in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f'Продукт {i}', f'Описание {i}', i * 100))
    connection.commit()
def get_all_products():
    return cursor.execute("SELECT * FROM Products")


connection.commit()
