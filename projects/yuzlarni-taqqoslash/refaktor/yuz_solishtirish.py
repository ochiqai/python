from yuzbib import (
    vector_taq,
    aniqlash,
    model_yuklash,
    chizish,
    embedding_olish,
    piksel_olish,
    rasm_olish
)



# 1. rasm olish
rasm_joyi = "rasmlar/uz_prez.jpg"
rasm = rasm_olish(rasm_joyi)

# 2. aniqlagich
aniqlagich_model = model_yuklash(turi="aniqlagich")
kordinatalar = aniqlash(
    model=aniqlagich_model,
    rasm=rasm
)
rasm_chizilgan = chizish(
    rasm=rasm,
    kordinatalar=kordinatalar
)


# 3.1 piksellar orqali solishtirish
piksellar = piksel_olish(
    rasm=rasm,
    kordinatalar=kordinatalar
)


ASLIDA = [
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Boshqa odam",
    "Boshqa odam",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Shavkat Mirziyoyev",
    "Boshqa odam",
    "Shavkat Mirziyoyev",
    "Boshqa odam",
    "Shavkat Mirziyoyev",
    "Boshqa odam",
    "Boshqa odam",
    "Boshqa odam"
]

# test: 0 rasm, 1-18: bazadagi
test = piksellar[0][0]
for idx in range(1, len(piksellar)):
    baza = piksellar[idx][0]
    yaqinlik = vector_taq(test, baza)
    print(yaqinlik)
    if yaqinlik > 0.91:
        print("Model bashorati: {}".format("Shavkat Mirziyoyev"))
        print("Aslida         : {}".format(ASLIDA[idx]))
    else:
        print("Model bashorati: {}".format("Boshqa odam"))
        print("Aslida         : {}".format(ASLIDA[idx]))


# 3.2 embedding orqali solishtirish
embedding_model = model_yuklash(turi="embedding")
embeddinglar = embedding_olish(
    model=embedding_model,
    rasm=rasm,
    kordinatalar=kordinatalar
)

# test: 0 rasm, 1-18: bazadagi
test = embeddinglar[0][0]
for idx in range(1, len(embeddinglar)):
    baza = embeddinglar[idx][0]
    yaqinlik = vector_taq(test, baza)
    print(yaqinlik)
    if yaqinlik > 0.1:
        print("Model bashorati: {}".format("Shavkat Mirziyoyev"))
        print("Aslida         : {}".format(ASLIDA[idx]))
    else:
        print("Model bashorati: {}".format("Boshqa odam"))
        print("Aslida         : {}".format(ASLIDA[idx]))
