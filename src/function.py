import numpy as np
import copy
import random
import os.path
def printYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def printRed(skk): print("\033[91m {}\033[00m".format(skk))

def print_matrix(matrix, default=True):
    if default: # scorenya disamping
        print("Matrix:")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != len(matrix[i])-1:
                    print(matrix[i][j], end=" ")
                else:
                    print(matrix[i][j])
        print()
    else: # scorenya di newline
        for i in range(len(matrix)):
            print("Sequence " + str(i+1) + ": ", end="")
            for j in range(len(matrix[i])):
                if j < len(matrix[i])-2:
                    print(matrix[i][j], end=" ")
                else:
                    if j == len(matrix[i])-1:
                        print("Reward: " + str(matrix[i][j]))
                    else:
                        print(matrix[i][j])

def score(sequence, buffer):
    # strbuffer = " ".join(buffer) # kalo buffernya dalam bentuk array
    strbuffer = buffer
    score = 0
    strsequence = []
    for i in range(len(sequence)):
        strsequence.append(" ".join(sequence[i][:-1]))
    for i in range(len(strsequence)):
        if strsequence[i] in strbuffer:
            score += int(sequence[i][-1])
    return score

def increment_array(arr, xlimit, ylimit):
    for i in range(len(arr) - 1, -1, -1):
        if (i+1) % 2 == 1: # ganjil berati yang terakhir adalah vertikal
            arr[i] = ((arr[i]) % ylimit) + 1
        else:
            arr[i] = ((arr[i]) % xlimit) + 1
        if arr[i] != 1:
            break
    return arr  

def validateMax(arr, ylimit, xlimit):
    isMax = True
    for i in range(len(arr)):
        if (i+1) % 2 == 1:
            if arr[i] != ylimit:
                isMax = False
        else:
            if arr[i] != xlimit:
                isMax = False
    return isMax

def FinalList(final_coordinate, final_buffer):
    if len(final_buffer) == 0:
        return final_buffer, final_coordinate 
    if all(buffer == final_buffer[0] for buffer in final_buffer):
        return final_buffer[0], final_coordinate[0]
    else:
        buffer = min(final_buffer, key=len)
        coordinate = np.where(np.array(final_buffer) == buffer)
        return buffer, final_coordinate[coordinate[0][0]]

def bruteForce(matrix, sequences, buffer_size):
    maxscore = 0
    final_coordinate = []
    final_buffer = []
    ymax = len(matrix) - 1
    xmax = len(matrix[0]) - 1
    for i in range(len(matrix[0])):
        buffer_coordinate = []  
        doitonce = False
        movement = [1 for ite in range(buffer_size-1)]
        is_horizontal = False
        string = matrix[0][i]
        y = 0
        x = i
        buffer_coordinate.append((x+1,y+1))
        while not(validateMax(movement, ymax, xmax)) or not doitonce: # ngitung semua kemungkinan
            for j in range(len(movement)): # melakukan pergerakan sesuai dengan kemungkinan movement saat ini
                if is_horizontal:  
                    x = (x + movement[j]) % len(matrix[0])
                    if (x+1,y+1) in buffer_coordinate: # kalo movement yang dipakai terdapat 2 cell matrix yang dilewati 
                        break # maka langsung keluar loop dan mencari kemungkinan movement yang lain
                    else:
                        string += " " + matrix[y][x]
                        buffer_coordinate.append((x+1,y+1))
                        is_horizontal = False
                        curr_score = score(sequences, string) # hitung score saat ini
                        if curr_score > maxscore:
                            final_coordinate = []
                            final_buffer = []
                            maxscore = score(sequences, string)
                            final_buffer.append(copy.deepcopy(string))
                            final_coordinate.append(copy.deepcopy(buffer_coordinate))
                        elif curr_score >= maxscore: # bisa dioptimasi dengan menghapus bagian ini mungkin? Gak jadi karena yang optimal bisa dibelakangan
                            maxscore = score(sequences, string)
                            final_buffer.append(copy.deepcopy(string))
                            final_coordinate.append(copy.deepcopy(buffer_coordinate))
                else:
                    y = (y + movement[j]) % len(matrix)
                    if (x+1,y+1) in buffer_coordinate:
                        break
                    else:
                        string += " " + matrix[y][x]
                        buffer_coordinate.append((x+1,y+1))
                        is_horizontal = True
                        curr_score = score(sequences, string) # hitung score saat ini
                        if curr_score > maxscore:
                            final_coordinate = []
                            final_buffer = []
                            maxscore = score(sequences, string)
                            final_buffer.append(copy.deepcopy(string))
                            final_coordinate.append(copy.deepcopy(buffer_coordinate))
                        elif curr_score >= maxscore:
                            maxscore = score(sequences, string)
                            final_buffer.append(copy.deepcopy(string))
                            final_coordinate.append(copy.deepcopy(buffer_coordinate))
            curr_score = score(sequences, string)
            if curr_score > maxscore:
                final_coordinate = []
                final_buffer = []
                maxscore = score(sequences, string)
                final_buffer.append(copy.deepcopy(string))
                final_coordinate.append(copy.deepcopy(buffer_coordinate))
            elif curr_score >= maxscore:
                maxscore = score(sequences, string)
                final_buffer.append(copy.deepcopy(string))
                final_coordinate.append(copy.deepcopy(buffer_coordinate))
            y = 0
            x = i
            is_horizontal = False
            string = matrix[0][i] 
            buffer_coordinate = []
            buffer_coordinate.append((x+1,y+1)) 
            doitonce = True
            if xmax == 0 or ymax == 0:
                break
            increment_array(movement, xmax, ymax)
    buffer, coordinate = FinalList(final_coordinate, final_buffer)
    print(maxscore)
    if maxscore > 0:
        print(buffer)
        for tuple in coordinate:
            x,y = tuple
            print(str(x) + ", " + str(y))
    else:
        print("Tidak ada solusi yang menghasilkan nilai positif")
    return maxscore, buffer, coordinate
    
def run():
    fromFile = input("\nMasukkan dari file txt? (y/n): ").lower()
    while fromFile != 'y' and fromFile != 'n':
        fromFile = input("Masukkan dari file txt? (y/n): ").lower()
    if fromFile == 'y':
        foldertest = input("File pada folder test? (y/n): ")
        while foldertest != 'y' and foldertest != 'n':
            foldertest = input("File pada folder test? (y/n): ")
        error = True
        while error:
            if foldertest == 'y':
                filename = input("Masukkan nama file txt: ")
                filename = "../test/" + filename 
                while not(os.path.isfile(filename)):
                    print("\nFile tidak ditemukan.\n")
                    filename = input("Masukkan nama file txt: ")
                    filename = "../test/" + filename
                file = open(filename, 'r')
            else:
                path = input("Masukkan absolute path dari file txt: ")
                while not(os.path.isfile(path)):
                    print("\nFile tidak ditemukan.\n")
                    path = input("Masukkan absolute path dari file txt: ")
                file = open(path, 'r')
            print()
            
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
        return buffer_size, matrix, matrix_sequence
    else:
        
        while True:
            while True:
                try:
                    token_unik = int(input("\nMasukkan jumlah token unik: "))
                    if token_unik < 2:
                        raise Exception()
                except:
                    print("Harus berupa angka dan minimal 2.")
                else:
                    break
            while token_unik <= 0:
                print("Jumlah token unik tidak boleh 0 atau negatif.")
                token_unik = int(input("Masukkan jumlah token unik: "))
        
            token = input("Masukkan token unik (alphanumeric): ").split()
            isAlphaNum = all(element.isalnum() for element in token)
            isLen2 = all(len(element) == 2 for element in token)
            while len(set(token)) != token_unik or not(isAlphaNum) or not(isLen2):
                print("Token harus berupa alphanumeric dan berjumlah sama dengan jumlah token unik")
                token = input("Masukkan token unik: ").split()
                isAlphaNum = all(element.isalnum() for element in token)
                isLen2 = all(len(element) == 2 for element in token)
            while True:
                try:
                    buffer_size = int(input("Masukkan ukuran buffer: "))
                except:
                    print("Harus beruapa angka.")
                else:
                    break
            while buffer_size < 2:
                print("Ukuran buffer minimal adalah 2.")
                buffer_size = int(input("Masukkan ukuran buffer: "))
            ukuran_matrix = input("Masukkan ukuran matrix (col,row): ").split()
            while len(ukuran_matrix) != 2 :
                print("Harus memasukkan kolom dan baris.")
                ukuran_matrix = input("Masukkan ukuran matrix (col,row): ").split()
            while int(ukuran_matrix[0]) <= 0 or int(ukuran_matrix[1]) <= 0 or ((int(ukuran_matrix[0]) * int(ukuran_matrix[1])) < token_unik):
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
            print()
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
            count = 0
            while not(isUnique):
                for i in range(len(matrix_sequence)-1):
                    if matrix_sequence[i] in matrix_sequence[i+1:]:
                        matrix_sequence = [[random.choice(token) for bla in range(random.randint(2,ukuran_max_seq))] for blabla in range(jumlah_seq)]
                        reroll = True
                        count += 1
                        break
                if not reroll:
                    isUnique = True
                reroll = False
                if count >= 500:
                    print("Jumlah token unik tidak cukup untuk membuat sequence yang unik.")
                    break
            if count < 500:
                break 
        for item in matrix_sequence:
            item.append(random.randint(1,100))
        print_matrix(matrix)
        print_matrix(matrix_sequence, False)
        print() 
        return buffer_size, matrix, matrix_sequence
    
def saving(maxscore, buffer, coordinate, finish, start):
    saveOrNo = input("Apakah ingin menyimpan solusi? (y/n): ")
    while saveOrNo != 'y' and saveOrNo != 'n':
        saveOrNo = input("Apakah ingin menyimpan solusi? (y/n): ").lower()
    if saveOrNo == 'y':
        while True:
            filename = input("Masukkan nama file (termasuk .txt): ")
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

            
            

            

        

