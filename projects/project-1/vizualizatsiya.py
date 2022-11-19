import numpy as np
import matplotlib.pyplot as plt


usul_oddiy = np.load("natija/oddiy_natija.npz")
usul_oddiy = usul_oddiy["oddiy_usul"]

usul_ai = np.load("natija/ml_natija.npz")
usul_ai = usul_ai["ai_usul"]

print(usul_oddiy.shape)
print(usul_ai.shape)

print("IDX: oddiy:  AI")
for i in range(24):
    print(f"{i}: {usul_oddiy[i]}: {usul_ai[i]}")

# viz
plt.plot(usul_oddiy)
plt.plot(usul_ai)
plt.xlabel("Rasm")
plt.ylabel("Uxshashlik natijasi")
plt.legend(["Oddiy", "AI"])
plt.show()