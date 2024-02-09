import function
import time
import random
fromFile = input("Masukkan dari file txt? (y/n): ")
if fromFile == 'y':
    filename = input("Masukkan nama file txt: ")
    print()
    file = open(filename, 'r')
    buffer_size = int(file.readline())
    matrix_size = file.readline().split()
    matrix_width = int(matrix_size[0])
    matrix_height = int(matrix_size[1])
    matrix = []
    for i in range(matrix_height):
        matrix.append(file.readline().split())
    number_of_sequences = int(file.readline().strip('\n'))
    matrix_sequence = []
    for i in range(number_of_sequences):
        matrix_sequence.append(file.readline().split())
        matrix_sequence[i].append(file.readline().strip('\n'))
else:
    token_unik = int(input("Masukkan jumlah token unik: "))
    while token_unik <= 0:
        print("Jumlah token unik tidak boleh 0 atau negatif.")
        token_unik = int(input("Masukkan jumlah token unik: "))
   
    token = input("Masukkan token unik (alphanumeric): ").split()
    isAlphaNum = all(element.isalnum() for element in token)
    isLen2 = all(len(element) == 2 for element in token)
    while len(token) != token_unik or not(isAlphaNum) or not(isLen2):
        print("Token harus berupa alphanumeric dan berjumlah sama dengan jumlah token unik")
        token = input("Masukkan token unik: ").split()
        isAlphaNum = all(element.isalnum() for element in token)
        isLen2 = all(len(element) == 2 for element in token)

    buffer_size = int(input("Masukkan ukuran buffer: "))
    while buffer_size < 2:
        print("Ukuran buffer minimal adalah 2.")
        buffer_size = int(input("Masukkan ukuran buffer: "))
    ukuran_matrix = input("Masukkan ukuran matrix (col,row): ").split()
    while int(ukuran_matrix[0]) <= 0 or int(ukuran_matrix[1]) <= 0 or len(ukuran_matrix) != 2 or ((int(ukuran_matrix[0]) * int(ukuran_matrix[1])) < token_unik):
        print("Ukuran matrix tidak boleh 0 ataupun negatif dan ukuran matrix harus lebih besar dari jumlah token unik.")
        ukuran_matrix = input("Masukkan ukuran matrix (col,row): ").split()

    jumlah_seq = int(input("Masukkan jumlah sequences: "))
    while jumlah_seq <= 0:
        print("Jumlah sequence minimal 1.")
        jumlah_seq = int(input("Masukkan jumlah sequences: "))
    ukuran_max_seq = int(input("Masukkan ukuran maksimal sequences: "))
    while ukuran_max_seq < 2:
        print("Panjang minimal sequence adalah 2.")
        ukuran_max_seq = int(input("Masukkan ukuran maksimal sequences: "))

    matrix = [[0 for i in range(int(ukuran_matrix[0]))] for j in range(int(ukuran_matrix[1]))]
    minimumlength = min(ukuran_matrix[0], ukuran_matrix[1])
    for item in token:
        x = random.randint(0, len(matrix)-1)
        y = random.randint(0, len(matrix[0])-1)
        while matrix[x][y] != 0:
            x = random.randint(0, len(matrix)-1)
            y = random.randint(0, len(matrix[0])-1)
        matrix[x][y] = item
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                continue
            else:
                matrix[i][j] = random.choice(token)
    matrix_sequence = [[random.choice(token) for i in range(random.randint(2,ukuran_max_seq))] for j in range(jumlah_seq)]
    for item in matrix_sequence:
        item.append(random.randint(1,100))
             
function.print_matrix(matrix)
function.print_matrix(matrix_sequence, False)
# print(matrix_sequence)
buffer = ["7A", "BD", "7A", "BD", "1C", "BD", "55"]
buffer2 = ["BD", "E9", "1C", "BD", "7A", "BD", "1C", "BD", "55"]
buffer3 = "BD E9 1C BD 7A BD 1C BD 55"
# print(function.score(matrix_sequence, buffer3))
start = time.time()
function.bruteForce(matrix, matrix_sequence, buffer_size)
finish = time.time()
print(finish - start)