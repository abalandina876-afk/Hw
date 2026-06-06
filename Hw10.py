import sqlite3

conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    AnimalName TEXT,
    AnimalType TEXT
)
""")

animals = [
    ("Lion", "Mammal"),
    ("Crocodile", "Reptile"),
    ("Eagle", "Bird"),
    ("Sea Turtle", "Reptile"),
    ("Monkey", "Mammal")
]

cursor.executemany(
    'INSERT INTO Animals (AnimalName, AnimalType) VALUES (?, ?)',
    animals
)

cursor.execute(
    'UPDATE Animals SET AnimalName = "Falcon" WHERE AnimalName = "Eagle"'
)

cursor.execute(
    'SELECT * FROM Animals WHERE AnimalType = "Mammal"'
)
mammals = cursor.fetchall()
print("Mammals:", mammals)

cursor.execute('SELECT * FROM Animals')
all_animals = cursor.fetchall()
print("All animals:", all_animals)

conn.commit()
conn.close()