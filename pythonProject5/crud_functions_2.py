import sqlite3 as sql


connection = sql.connect('product_base.db')
cursor = connection.cursor()
connection2 = sql.connect('users.db')
cursor2 = connection2.cursor()



cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INT NOT NULL
        );
''')

cursor2.execute('''
   CREATE TABLE IF NOT EXISTS Users(
   id INTEGER PRIMARY KEY,
   username TEXT NOT NULL,
   email TEXT NOT NULL,
   age TEXT NOT NULL,
   balance INTEGER
   )
   ''')
connection2.commit()




cursor.execute("DELETE FROM Products")
for i in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f'Продукт {i}', f'Описание {i}', i * 100))
    connection.commit()
def get_all_products():
    return cursor.execute("SELECT * FROM Products")

def add_user(username, email, age):
    cursor2.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (username, email, age, '1000'))
    connection2.commit()


def is_included(username):
    check = cursor2.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check.fetchone() is None:
        return True
    return False
connection.commit()
connection2.commit()