import function
import time
import random
import os.path
fromFile = input("\nMasukkan dari file txt? (y/n): ").lower()
while fromFile != 'y' and fromFile != 'n':
    fromFile = input("Masukkan dari file txt? (y/n): ").lower()
if fromFile == 'y':
    error = True
    while error:
        filename = input("Masukkan nama file txt: ")
        filename = "../test/" + filename 
        while not(os.path.isfile(filename)):
            print("\nFile tidak ditemukan.\n")
            filename = input("Masukkan nama file txt: ")
            filename = "../test/" + filename
        print()
        file = open(filename, 'r')
        while True:
            try:
                buffer_size = int(file.readline())
            except:
                print("Buffer size harus berupa integer\n")
                break
            try:
                matrix_size = file.readline().split()
                matrix_width = int(matrix_size[0])
                matrix_height = int(matrix_size[1])
            except:
                print("Ukuran matrix harus berupa integer\n")
                break
            try:
                matrix = []
                for i in range(matrix_height):
                    cell = file.readline().split()
                    isAlphaNum = all(element.isalnum() for element in cell)
                    isLen2 = all(len(element) == 2 for element in cell)
                    if isAlphaNum and isLen2:
                        matrix.append(cell)
                        if len(matrix[i]) != matrix_width:
                            print("Jumlah kolom matrix tidak sesuai.\n")
                            raise Exception()
                    else:
                        print("Cell matrix harus terdiri dari token dengan 2 karakter alphanumeric.\n")
                        raise Exception()
            except:
                break
            try:
                number_of_sequences = int(file.readline().strip('\n'))
            except:
                print("Jumlah sequences harus berupa integer.\n")
                break
            try:
                matrix_sequence = []
                for i in range(number_of_sequences):
                    seq = file.readline().split()
                    isAlphaNum = all(element.isalnum() for element in seq)
                    isLen2 = all(len(element) == 2 for element in seq)
                    if isAlphaNum and isLen2:
                        matrix_sequence.append(seq)
                    else:
                        print("Sequence harus terdiri dari token dengan 2 karakter alphanumeric.\n")
                        raise Exception()
                    try:
                        matrix_sequence[i].append(int(file.readline().strip('\n')))
                    except:
                        print("Reward harus berupa integer\n")
                        raise Exception()
            except:
                break
            else:
                error = False
                break
else:
    token_unik = int(input("Masukkan jumlah token unik: "))
    while token_unik <= 0:
        print("Jumlah token unik tidak boleh 0 atau negatif.")
        token_unik = int(input("Masukkan jumlah token unik: "))
   
    token = input("Masukkan token unik (alphanumeric): ").upper().split()
    isAlphaNum = all(element.isalnum() for element in token)
    isLen2 = all(len(element) == 2 for element in token)
    while len(set(token)) != token_unik or not(isAlphaNum) or not(isLen2):
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
    isUnique = False
    matrix_sequence = [[random.choice(token) for i in range(random.randint(2,ukuran_max_seq))] for j in range(jumlah_seq)]
    reroll = False
    while not(isUnique):
        for i in range(len(matrix_sequence)-1):
            if matrix_sequence[i] in matrix_sequence[i+1:]:
                matrix_sequence = [[random.choice(token) for bla in range(random.randint(2,ukuran_max_seq))] for blabla in range(jumlah_seq)]
                reroll = True
                break
        if not reroll:
            isUnique = True
        reroll = False
    for item in matrix_sequence:
        item.append(random.randint(1,100))
    function.print_matrix(matrix)
    function.print_matrix(matrix_sequence, False)
    print()         

start = time.time()
maxscore, buffer, coordinate = function.bruteForce(matrix, matrix_sequence, buffer_size)
print()
finish = time.time()
print(str((finish - start)*1000) + " ms")
print()

saveOrNo = input("Apakah ingin menyimpan solusi? (y/n): ")
while saveOrNo != 'y' and saveOrNo != 'n':
    saveOrNo = input("Apakah ingin menyimpan solusi? (y/n): ").lower()
if saveOrNo == 'y':
    while True:
        filename = input("Masukkan nama file: ")
        filename = "../test/" + filename
        print()
        isExistAndFile = os.path.isfile(filename)
        if isExistAndFile:
            print("File dengan nama tersebut sudah ada.")
            print("Apakah Anda ingin mengubah nama file atau rewrite?\n")
            timpa = input("r untuk rewrite dan u untuk ubah nama file: ").lower()
            print()
            while timpa != 'r' and timpa != 'u':
                timpa = input("r untuk rewrite dan u untuk ubah nama file: ").lower()
            if timpa == 'u':
                continue
            else:
                break
        else:
            break
   
    file = open(filename, "w")
    file.write(str(maxscore) + '\n')
    if maxscore == 0:
        file.write("Tidak memiliki kombinasi dengan score positif.\n")
    else:
        file.write(buffer + '\n')
        for tuple in coordinate:
            x,y = tuple
            file.write(str(x) + ", " + str(y) + '\n')
    file.write('\n')
    file.write(str((finish - start)*1000) + " ms")
    file.write('\n')