import math
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def ildiz(x):
    return math.sqrt(x)


def vector_taq(a, b):
    # kosinus o'xshashlik https://en.wikipedia.org/wiki/Cosine_similarity
    # 1*1 + 2*2 + 2*2 + 1*2 + 1*1 + 1*1

    if len(a) == len(b):
        i = 0
        v = 0
        while i < len(a):
            v += (a[i] * b[i])
            i += 1

        # modul
        i = 0
        modul_a = 0
        modul_b = 0
        while i < len(a):
            modul_a += (a[i] * a[i])
            modul_b += (b[i] * b[i])
            i += 1

        modul_a = ildiz(modul_a)
        modul_b = ildiz(modul_b)
        maxraj = modul_a * modul_b
        yaqinlik = v / maxraj

        return yaqinlik
    else:
        print("Elementlar soni teng bo'lish kerak!")

# v1 = [1]
# v2 = [3]
# v3 = [1.5]

v1 = [1, 2, 3, 4, 5]
v2 = [1, 2, 3, 4, 5]
v3 = [1, 2, 3, 4, 6]
v4 = [100, 2, 3, 4, 5]


natija1 = vector_taq(v1, v2)
natija2 = vector_taq(v1, v3)
natija3 = vector_taq(v1, v4)

print(natija1)
print(natija2)
print(natija3)


# print(cosine_similarity(np.array(v1).reshape(1, -1), np.array(v2).reshape(1, -1)))

print("Tayyoridan foydalandik")

natija1 = cosine_similarity(np.array(v1).reshape(1, -1), np.array(v2).reshape(1, -1))[0][0]
natija2 = cosine_similarity(np.array(v1).reshape(1, -1), np.array(v3).reshape(1, -1))[0][0]
natija3 = cosine_similarity(np.array(v1).reshape(1, -1), np.array(v4).reshape(1, -1))[0][0]

print(natija1)
print(natija2)
print(natija3)
