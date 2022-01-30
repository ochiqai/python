import sqlite3


conn = sqlite3.connect('kitob.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Kitobxon')
cur.execute('CREATE TABLE Kitobxon (nomi TEXT, beti INTEGER)')

# conn.close()

conn = sqlite3.connect('kitob.sqlite')
cur = conn.cursor()

cur.execute("INSERT INTO Kitobxon (nomi, beti) VALUES (?, ?)", ("Mehrobdan Chayon", 300))
cur.execute("INSERT INTO Kitobxon (nomi, beti) VALUES (?, ?)", ("O'tgan kunlar", 400))
cur.execute("INSERT INTO Kitobxon (nomi, beti) VALUES (?, ?)", ("Ertaklar", 500))
conn.commit()

print("Kitoblar ro'yhati: ")

cur.execute("SELECT nomi, beti FROM Kitobxon")
for qator in cur:
    print(qator)

cur.execute("DELETE FROM Kitobxon WHERE beti > 0")
conn.commit()


print("Kitoblar ro'yhati: ")
cur.execute("SELECT nomi, beti FROM Kitobxon")
for qator in cur:
    print(qator)
conn.close()



