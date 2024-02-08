import function
import time
fromFile = input("Masukkan dari file txt? (y/n): ")
if fromFile == 'y':
    filename = input("Masukkan nama file txt: ")
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
    token = input("Masukkan token unik: ").split()
    ukuran_buffer = int(input("Masukkan ukuran buffer: "))
    ukuran_matrix = input("Masukkan ukuran matrix: ").split()
    jumlah_seq = int(input("Masukkan jumlah sequences: "))
    ukuran_max_seq = int(input("Masukkan ukuran maksimal sequences: "))
             
function.print_matrix(matrix)
function.print_matrix(matrix_sequence, False)
buffer = ["7A", "BD", "7A", "BD", "1C", "BD", "55"]
buffer2 = ["BD", "E9", "1C", "BD", "7A", "BD", "1C", "BD", "55"]
buffer3 = "BD E9 1C BD 7A BD 1C BD 55"
print(function.score(matrix_sequence, buffer3))
start = time.time()
function.bruteForce(matrix, matrix_sequence, 7)
finish = time.time()
print(finish - start)