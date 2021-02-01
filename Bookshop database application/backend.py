import sqlite3


def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()


def insert(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    # NULL je za id iz tabele book. Commit se koristi samo kada se desavaju promene u bazi
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()
    return rows


# Stavlja se prazan string zbog toga sto korisnik moze da pretrazuje po jednom parametru pa da za ostale vrati default
def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()


def update(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()



connect()
# insert("Nesto", "Jack London", 1909, 8742132)
# delete(4)
update(3,"Martinn Eden","Jack London", 1910, 75454)
print(view())
# print(search(title="Martin Eden"))
