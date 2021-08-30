
ism1 = 'Nuriddin'
ism2 = "Ulug'bek"

print(ism1[0])
print(ism2[4])

# ism1[1.5] >> mumkin emas


# uzunligi
print(len(ism2))

# oxirgi belgini olish
print(ism2[len(ism2) - 1])

# oxiridan kelish
print(ism2[-1])
print(ism1[-1])

print("********************************\n")
for belgi in ism1:
    print(belgi)

print("********************************\n")
indeks = 0
while indeks < len(ism1):
    belgi = ism1[indeks]
    indeks = indeks + 1
    print(belgi)


print("********************************\n")
dan = 3
gacha = 6
slays = ism1[dan:gacha]  # [0,3)
print(slays)
slays = ism1[:3]  # [0,3)
print(slays)

slays = ism1[3:len(ism1)]  # [3, oxirgacha)
print(slays)

slays = ism1[3:]
print(slays)

print("********************************\n")
slays = ism2[3:3]
print(slays)


print("**immutable ***********\n")

ism1 = 'sardor'
# ism1[0] = 'H'
# print(ism1)

yangi_ism = 'S' + ism1[1:]
print(yangi_ism)




print("**qidirish ***********\n")

yozuv = "Yangi Toshkent Qibray tumanida bunyod etiladi"





idx = 0
for belgi in yozuv:
    if belgi == 'n':
        print('Izlanayotgan harf topildi, Uraaaa.', idx)
        continue
    idx = idx + 1


def qidir(yozuv, harf):
    idx = 0
    for belgi in yozuv:
        if belgi == harf:
            print('Izlanayotgan harf topildi, Uraaaa.', idx)
            return idx
        idx = idx + 1

    return -1

print(qidir(yozuv, '.'))


# har juft joyda berilgan belgini qidir
print("******************************\n")
yozuv = "Yangi Toshkent Qibray tumanida bunyod etiladi"
idx = 0
while idx < len(yozuv):
    belgi = yozuv[idx]
    if belgi == 'n':
        print('Izlanayotgan harf topildi, Uraaaa.', idx)
        break
    idx = idx + 2


print("******************************\n")
yozuv = "Yangi Toshkent Qibray tumanida bunyod etiladi"

uzunlik = 0
sana = 0
for belgi in yozuv:
    uzunlik = uzunlik + 1
    if belgi == 'n':
        sana = sana + 1
print(uzunlik)
print(sana)

print("-----------------------------------------\n\n\n")
print("String metodlari")
ism = "sardor"
katta_ism = ism.upper()
print(katta_ism)

ism = "OCHIQ"
kichik_ism = ism.lower()
print(kichik_ism)

idx = ism.find('Q')
print(idx)

ism = 'tashkent shahri'
idx = ism.find('a', 5)
print(idx)

# in
ism = 'tashkent shahri'
bor = 't' in ism

print(bor)

if ism == 'samarqand shahri':
    print('Bir xil')
else:
    print('Xar xil')




print(ism.replace('tashkent', 'samarqand'))

print("👋")

# \n - yangi qator
# \t -

yozuv = "salom"
print(yozuv)
yozuv = "salom\t".strip()
print(yozuv)
yozuv = "salom\n"
print(yozuv)

def harqanday_kichikharf(s):
    for eshak in s:
        if eshak.isupper():
            return False

    return True

yozuv = "salom"
result = harqanday_kichikharf(yozuv)
print(result)








