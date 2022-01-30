import sqlite3
from ishchi import Ishchi


# baza yaratish
conn = sqlite3.connect("ishchilar_baza")
cur = conn.cursor()

def jadval_yaratish():
    cur.execute('DROP TABLE IF EXISTS ishchilar')
    cur.execute("""CREATE TABLE ishchilar (
                id INTEGER PRIMARY KEY,
                ism TEXT,
                familiya TEXT,
                sharif TEXT,
                yosh INTEGER)
                """)
    conn.commit()

def ishchi_qushish(ishchi):
    cur.execute("INSERT INTO ishchilar (ism, familiya, sharif, yosh) VALUES (?, ?, ?, ?)",
                (ishchi.ism, ishchi.familiya, ishchi.sharif, ishchi.yosh))
    conn.commit()

def ishchilarni_ruyxati():
    cur.execute("SELECT * FROM ishchilar")
    for qator in cur:
        print(qator)

def malumot_uchirish(yosh):
    cur.execute("DELETE FROM ishchilar WHERE yosh=?", (yosh,))
    conn.commit()

def malumot_uzgartirish(eski, yangi):
    cur.execute("UPDATE ishchilar SET yosh=? WHERE yosh=?", (yangi, eski))
    conn.commit()



# malumot qo'shish
ishchi_1 = Ishchi("Tesha", "Boltayev", "Qilich o'gli", 5)
ishchi_2 = Ishchi("Umrzoq", "Xujayev", "Bogbon o'gli", 21)
ishchi_3 = Ishchi("Oltin", "Rahimov", "Ulugbek o'gli", 47)
ishchi_4 = Ishchi("Tesha", "Boltayev", "Qilich o'gli", 5)
ishchilar_list = [ishchi_1, ishchi_2, ishchi_3, ishchi_4]

jadval_yaratish()
print("Jadval yaratildi: ishchilar nomli")

for ishchi in ishchilar_list:
    ishchi_qushish(ishchi)
print("{} ta ishchi ishchilar jadvaliga qo'shildi".format(len(ishchilar_list)))

print("Ishchilar ro'yhati:")
ishchilarni_ruyxati()

print("Ishchilarni o'chirish agar ularning yoshi 5 ga teng bo'lsa")
malumot_uchirish(5)
ishchilarni_ruyxati()

print("Ishchilarni amulomotini yangilash, 47 yoshdagilarni 55 yoshga o'tkazish")
malumot_uzgartirish(47, 55)
ishchilarni_ruyxati()

conn.close()








































# conn = sqlite3.connect('kitob.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Kitobxon')
# cur.execute('CREATE TABLE Kitobxon (nomi TEXT, beti INTEGER)')
#
# # conn.close()
#
# conn = sqlite3.connect('kitob.sqlite')
# cur = conn.cursor()
#
# cur.execute("INSERT INTO Kitobxon (nomi, beti) VALUES (?, ?)", ("Mehrobdan Chayon", 300))
# cur.execute("INSERT INTO Kitobxon (nomi, beti) VALUES (?, ?)", ("O'tgan kunlar", 400))
# cur.execute("INSERT INTO Kitobxon (nomi, beti) VALUES (?, ?)", ("Ertaklar", 500))
# conn.commit()
#
# print("Kitoblar ro'yhati: ")
#
# cur.execute("SELECT nomi, beti FROM Kitobxon")
# for qator in cur:
#     print(qator)
#
# cur.execute("DELETE FROM Kitobxon WHERE beti > 0")
# conn.commit()
#
#
# print("Kitoblar ro'yhati: ")
# cur.execute("SELECT nomi, beti FROM Kitobxon")
# for qator in cur:
#     print(qator)
# conn.close()
#
#
#
