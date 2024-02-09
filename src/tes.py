import os.path
import numpy as np
file = os.path.isfile("../test/file.txt")
print(os.getcwd())
print(file)

buffer = [[1,2,3,4], [1,2,4,5], [2,4,5,6], [2,4,5,6]]
for i in range(len(buffer)-1):
    print(buffer[i])
    print(buffer[i+1:])
    if buffer[i] in buffer[i+1:]:
        print("duplicate")
        break
token = input("Masukkan token unik (alphanumeric): ").upper().split()
print(token)