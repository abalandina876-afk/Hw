import sqlite3

conn = sqlite3.connect("FruitBasket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FruitName TEXT,
    Color TEXT
)
""")

cursor.execute("INSERT INTO Fruits (FruitName, Color) VALUES ('Яблуко', 'Червоне')")
cursor.execute("INSERT INTO Fruits (FruitName, Color) VALUES ('Банан', 'Жовтий')")
cursor.execute("INSERT INTO Fruits (FruitName, Color) VALUES ('Апельсин', 'Помаранчевий')")

cursor.execute("UPDATE Fruits SET Color='Зелене' WHERE FruitName='Яблуко'")

cursor.execute("SELECT * FROM Fruits WHERE Color='Жовтий'")
yellow_fruits = cursor.fetchall()
print("Жовті фрукти:", yellow_fruits)

cursor.execute("SELECT * FROM Fruits")
all_fruits = cursor.fetchall()
print("Всі фрукти:", all_fruits)

conn.commit()
conn.close();