import numpy as np
import matplotlib.pyplot as plt



rasm = plt.imread("rasmlar/yuz_rasm_0.jpg")
# plt.imshow(rasm[0:25, 0:25, :])
# plt.imshow(rasm[:, 0:25, :])

# plt.show()
# print(rasm)
# print(rasm.shape)
# print(rasm.dtype)

# rasmlarni listga joylash
# rasm_01 = plt.imread("rasmlar/yuz_rasm_0.jpg")
# rasm_02 = plt.imread("rasmlar/yuz_rasm_1.jpg")
#
# rasmlar = [rasm_01, rasm_02]
#
# for rasm in rasmlar:
#     plt.imshow(rasm)
#     plt.show()

# # rasmlarni qushish
# rasm_01 = plt.imread("rasmlar/yuz_rasm_0.jpg")
# rasm_02 = plt.imread("rasmlar/yuz_rasm_1.jpg")
#
# rasm_qushish = rasm_01 - rasm_02
# print(rasm_qushish)
# print(rasm_qushish.min())
# print(rasm_qushish.max())
# plt.imshow(rasm_qushish // 2)
# plt.show()


#
dollar_kursi = np.linspace(5000, 11000, 50)


# plt.plot(dollar_kursi, [x for x in range(20)])
# plt.show()
# print(dollar_kursi)

kurs = []
for x in range(50):
    kurs.append(np.random.choice(dollar_kursi.astype(np.int32)))
# plt.plot([x for x in range(50)], dollar_kursi)
# plt.show()

dollar_kursi_xar_xil = []
for x in dollar_kursi:
    yangi_kurs = x + np.random.choice([0, 5, 50, 500, 2050])
    dollar_kursi_xar_xil.append(yangi_kurs)
# plt.plot([x for x in range(50)], dollar_kursi_xar_xil)
# plt.show()



x = np.linspace(-50, 50, 100)
# y = 5*x + 1
y = np.sin(x)*x + x
plt.plot(x, y)
plt.text(10, 10, "kurs")
plt.legend("Kurs")
plt.xlabel("x qiymatlar")
plt.ylabel("y qiymatlar")
plt.title("Kurs o'zgarishi")
plt.show()









