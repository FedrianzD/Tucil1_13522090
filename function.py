import numpy as np
import copy
def print_matrix(matrix, default=True):
    if default:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != len(matrix[i])-1:
                    print(matrix[i][j], end=" ")
                else:
                    print(matrix[i][j])
        print()
    else:
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
def distance(list):
    for i in list:
        for j in range(len(i)):
            x = 0
def bruteForce(matrix, sequence, buffer_size):
    maxscore = 0
    buffer_coordinate = []
    final_coordinate = []
    # buffer_size = buffer_size*2
    # xmovement = [1 for i in range((buffer_size-1)%2)]
    # ymovement = [1 for i in range(buffer_size - ((buffer_size-1)%2))]
    movement = [1 for i in range(buffer_size-1)]
    ymax = len(matrix) - 1
    xmax = len(matrix[0]) - 1
    # ymax = 3
    # xmax = 7
    for i in range(len(matrix[0])):
        is_horizontal = False
        string = matrix[0][i]
        y = 0
        x = i
        buffer_coordinate.append((x,y))
        while not(validateMax(movement, ymax, xmax)):
            for j in range(len(movement)):
                if is_horizontal:  
                    x = (x + movement[j]) % len(matrix[0])
                    # while (y,x) in buffer_coordinate:
                    #     x = (x + 1) % len(matrix[0])
                    string += " " + matrix[y][x]
                    buffer_coordinate.append((x,y))
                    # print("y:", y, "x:", x)
                    is_horizontal = False
                else:
                    y = (y + movement[j]) % len(matrix)
                    # while (y,x) in buffer_coordinate:
                    #     y = (y + 1) % len(matrix)
                    string += " " + matrix[y][x]
                    buffer_coordinate.append((x,y))
                    # print("y:", y, "x:", x)
                    is_horizontal = True
            
            
            # print(string)
            # if string == "X1 X2 X3 X4 X5 X6 X7":
            #     maxscore = 100
            print(movement)
            curr_score = score(sequence, string)
            if curr_score > maxscore:
                final_coordinate = []
                maxscore = score(sequence, string)
                final_coordinate.append(copy.deepcopy(buffer_coordinate))
            elif curr_score >= maxscore:
                maxscore = score(sequence, string)
                final_coordinate.append(copy.deepcopy(buffer_coordinate))
            y = 0
            x = i
            is_horizontal = False
            string = matrix[0][i] 
            buffer_coordinate = []
            buffer_coordinate.append((x,y)) 
            increment_array(movement, xmax, ymax)
    print(maxscore)
    print(final_coordinate)
    # print(min(buffer_coordinate, key=sum))
            
            

            

        

