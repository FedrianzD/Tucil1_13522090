# import os.path
# import numpy as np
# import random
# file = os.path.isfile("../test/file.txt")
# print(os.getcwd())
# print(file)

# buffer = [[1,2,3,4], [1,2,4,5], [2,4,5,6], [2,4,5,6]]
# for i in range(len(buffer)-1):
#     print(buffer[i])
#     print(buffer[i+1:])
#     if buffer[i] in buffer[i+1:]:
#         print("duplicate")
#         break
# token = input("Masukkan token unik (alphanumeric): ").upper().split()
# print(token)

# a = 2.6
# print(int(a))

# isUnique = False
# matrix_sequence = [[1,2,3,4], [1,2,3,5], [1,2,3,5], [1,2,3,7]]
# reroll = False
# while not(isUnique):
#     for i in range(len(matrix_sequence)-1):
#         if matrix_sequence[i] in matrix_sequence[i+1:]:
#             matrix_sequence = [[random.choice(token) for bla in range(random.randint(2,5))] for blabla in range(3)]
#             reroll = True
#             break
#     if not reroll:
#         isUnique = True
#     reroll = False

# a = "AA BB CC LL DD EE"
# if "AA BB CC" in a:
#     print(True)
# if "DD EE" in a:
#     print(True)
A = 10000000
print((0.95 * A * 1) + (0.99 * 0.05 * A * 10) + (0.01 * 0.05 * A * 10000000))
B = (0.95 * A * 1) + (0.99 * 0.05 * A * 10) + (0.01 * 0.05 * A * 10000000)
print(B/A)