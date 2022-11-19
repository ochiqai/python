import numpy as np

#
# # 1, 2, 3, o'lchamli matritsalar (array)
#
# vector_list = [1, 2, 3]
# print(vector_list, type(vector_list))
#
# vector_np = np.array([1, 2, 3])
# print(vector_np, type(vector_np))
#
# print(vector_np.shape)
# print(vector_np.argmax())
#
#
# # elementlarini olish
# print(vector_np[2])
#
# # 2 o'lchamli array
# vector_2d = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(vector_2d)
# print(vector_2d.shape) # >> [n, m] n-qator, m-ustun
#
# vector_2d_mix = np.array([
#     [1, 2, 3],
#     [4, 5]
# ])
#
# print(vector_2d_mix)
#
# vector_np_nollar = np.zeros((5, 5))
# print(vector_np_nollar)
# vector_np_nollar = np.zeros((5, 5)).astype(np.int32)
# print(vector_np_nollar)
#
# vector_np_bir = np.eye(5)
# print(vector_np_bir)
#
# vector_np_birlar = np.ones((5, 5))
# print(vector_np_birlar)
#
#
# vector_2d_mix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
#
# M = np.array([[11]])
# print(M)
# print(M.shape)
#
# A = np.array([])
# print(A.shape)

A = np.array([[], [], [], []])
print(A.shape)
A = np.array([[1], [-10], [9], [10.1]])
print(A.shape)
A = np.array([[0], [0], [0], [0]])
print(A.shape)

A = np.array([[2], [1], [2], [3]])
print(A.shape)

print(A.sum())

A = np.array([[2], [1], [2], [3]], dtype=np.int32)
print(A.dtype)

