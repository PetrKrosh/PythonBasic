# Функция добавления всех нулей в конец
def moveZeros(arr):
    return [nonZero for nonZero in arr if nonZero != 0] + [Zero for Zero in arr if Zero == 0]

arr = [1, 2, 0, 4, 3, 0, 5, 0]
L = moveZeros(arr)
print(L)

L_new = [i for i in L if i != 0]
print(L_new)

# L = [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
# for i in L:
#     if i == 0:
#         L.append(L.pop(L.index(0)))
# print(L)
#
# L_new = [i for i in L if i != 0]
# print(L_new)