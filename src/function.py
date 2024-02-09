import numpy as np
import copy
def print_matrix(matrix, default=True):
    if default: # scorenya disamping
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != len(matrix[i])-1:
                    print(matrix[i][j], end=" ")
                else:
                    print(matrix[i][j])
        print()
    else: # scorenya di newline
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j < len(matrix[i])-2:
                    print(matrix[i][j], end=" ")
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
def FinalList(final_coordinate, final_buffer, maxscore, sequences):
    if len(final_buffer) == 0:
        return final_buffer, final_coordinate 
    if all(buffer == final_buffer[0] for buffer in final_buffer):
        return final_buffer[0], final_coordinate[0]
    else:
        buffer = min(final_buffer, key=len)
        coordinate = np.where(np.array(final_buffer) == buffer)
        return buffer, final_coordinate[coordinate[0][0]]
        # realFinalBuffer = []
        # for buffer in final_buffer:
        #     tempBuffer = []
        #     for j in range(len(buffer)-2):
        #         if score(sequences, buffer[-j]) != maxscore:
        #             realFinalBuffer.append(buffer)
        #             break
        #         else:
        #             tempBuffer = buffer[-j]
        #     realFinalBuffer.append(tempBuffer)
        # buffer = min(realFinalBuffer, key=len)
        # idxBuffer = np.where(realFinalBuffer == buffer)
        # realFinalCoordinate = final_coordinate[idxBuffer[0]]
        # return buffer,realFinalCoordinate

def bruteForce(matrix, sequences, buffer_size):
    maxscore = 0
    buffer_coordinate = []
    final_coordinate = []
    final_buffer = []
    # buffer_size = buffer_size*2
    # xmovement = [1 for i in range((buffer_size-1)%2)]
    # ymovement = [1 for i in range(buffer_size - ((buffer_size-1)%2))]
    # movement = [1 for i in range(buffer_size-1)]
    # movement = [1,4,1,1]
    ymax = len(matrix) - 1
    xmax = len(matrix[0]) - 1
    for i in range(len(matrix[0])):
        movement = [1 for i in range(buffer_size-1)]
        is_horizontal = False
        string = matrix[0][i]
        y = 0
        x = i
        buffer_coordinate.append((x+1,y+1))
        while not(validateMax(movement, ymax, xmax)): # ngitung semua kemungkinan
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
                        elif curr_score >= maxscore:
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
            if xmax == 0 or ymax == 0:
                break
            increment_array(movement, xmax, ymax)
    buffer, coordinate = FinalList(final_coordinate, final_buffer, maxscore, sequences)
    print(maxscore)
    if maxscore > 0:
        print(buffer)
        for tuple in coordinate:
            x,y = tuple
            print(str(x) + ", " + str(y))
    else:
        print("Tidak ada solusi yang menghasilkan nilai positif")
    return maxscore, buffer, coordinate
    
    

            
            

            

        

