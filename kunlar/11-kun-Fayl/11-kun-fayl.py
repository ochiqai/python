# faylni ochib, uni ichidagi hamma narsa o'qib ekranga chiqarish
fayl_och = open(r"kundalik.txt", "r")
text = fayl_och.read()
print(text)
fayl_och.close()

# faylni ochib, uning faqat 1-qatorini chiqarish
fayl_och = open(r"kundalik.txt", "r")
text = fayl_och.readline()
print(text)
fayl_och.close()

# faylni ochib, uning hamma qatorlarini o'qib ekranga chiqarish
fayl_och = open(r"kundalik.txt", "r")
text = fayl_och.readlines()
print(text)
fayl_och.close()


# faylni ochib, for orqali tesktni o'qish
fayl_och = open(r"tun.txt", "r")
for qator in fayl_och:
    print(qator)
fayl_och.close()

# fayl ochib, unga yozish
fayl_och = open(r"tun.txt", "w")
fayl_och.write("Bu faylga yozish edi xolos.")
fayl_och.close()

# with orqali faylni ochib, uni ichidagi hamma narsa o'qib ekranga chiqarish
with open(r"kundalik.txt", "r") as fayl_och:
    text = fayl_och.read()
print(text)
fayl_och.close()