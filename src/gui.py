from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import function
import time
import random
maxscore = ""
buffer = ""
coordinate = ""
start = ''
finish = ''
matrix = []
label_matrix = []
def openFile():
    global maxscore, buffer, coordinate, finish, start, matrix, label_matrix
    canvas.delete('all')
    canvas2.delete('all')
    filepath = filedialog.askopenfilename(initialdir="D:\\Github\\Tucil1_13522090\\test")
    file = open(filepath, 'r')
    while True:
        try:
            buffer_size = int(file.readline())
        except:
            messagebox.showerror(title='Something is wrong', message="Buffer size harus berupa integer\n")
            break
        try:
            matrix_size = file.readline().split()
            matrix_width = int(matrix_size[0])
            matrix_height = int(matrix_size[1])
        except:
            messagebox.showerror(title='Something is wrong', message="Ukuran matrix harus berupa integer\n")
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
                        messagebox.showerror(title='Something is wrong', message="Jumlah kolom matrix tidak sesuai.\n")
                        raise Exception()
                else:
                    messagebox.showerror(title='Something is wrong', message="Cell matrix harus terdiri dari token dengan 2 karakter alphanumeric.\n")
                    raise Exception()
        except:
            break
        try:
            number_of_sequences = int(file.readline().strip('\n'))
        except:
            messagebox.showerror(title='Something is wrong', message="Jumlah sequences harus berupa integer.\n")
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
                    messagebox.showerror(title='Something is wrong', message="Sequence harus terdiri dari token dengan 2 karakter alphanumeric.\n")
                    raise Exception()
                try:
                    matrix_sequence[i].append(int(file.readline().strip('\n')))
                except:
                    messagebox.showerror(title='Something is wrong', message="Reward harus berupa integer\n")
                    raise Exception()
        except:
            break
        else:
            break
    file.close()
    start = time.time()
    maxscore, buffer, coordinate = function.bruteForce(matrix, matrix_sequence, buffer_size)
    finish = time.time()
    maxscore2.set(maxscore)
    cell_size = 50
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            y1 = i*cell_size + 10
            x1 = j*cell_size + 10
            y2 = y1 + cell_size
            x2 = x1 + cell_size
            canvas.create_rectangle(x1,y1,x2,y2, outline='green', width=2)
            canvas.create_text(x1+25, y1+25, text=str(matrix[i][j]))
    if maxscore != 0:
        buffer2.set(buffer)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                y1 = i*cell_size + 10
                x1 = j*cell_size + 10
                y2 = y1 + cell_size
                x2 = x1 + cell_size
                if (j+1,i+1) in coordinate:
                    canvas.create_rectangle(x1,y1,x2,y2, outline='red', width=4)
        for i in range(len(coordinate)-1):
            x1 = (coordinate[i][0] - 1) * cell_size + 35
            y1 = (coordinate[i][1] - 1) * cell_size + 35
            x2 = (coordinate[i+1][0] - 1) * cell_size + 35
            y2 = (coordinate[i+1][1] - 1) * cell_size + 35
            canvas.create_line(x1, y1, x2, y2, fill='red', width=3)
    else:
        buffer2.set('No solution')
    time2.set(f"{finish-start:.2f} ms")
    
    
def saveFile():
    global maxscore, buffer, coordinate, finish, start
    file = filedialog.asksaveasfile(defaultextension='.txt')
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
    file.close()

def submit():
    global maxscore, buffer, coordinate, finish, start, matrix, label_matrix
    canvas.delete('all')
    canvas2.delete('all')

    token_unik = entry1.get()
    token = entry2.get()
    buffer_size = entry3.get()
    kolom = entry4.get()
    baris = entry4b.get()
    jumlah_seq = entry5.get()
    ukuran_max_seq = entry6.get()

    try:
        token_unik = int(token_unik)
        buffer_size = int(buffer_size)
        kolom = int(kolom)
        baris = int(baris)
        jumlah_seq = int(jumlah_seq)
        ukuran_max_seq = int(ukuran_max_seq)
    except:
        messagebox.showerror(title='Something is wrong', message="Harus berupa integer.\n")
    if int(token_unik) < 2:
        messagebox.showerror(title='Something is wrong', message="Jumlah token harus lebih dari 1.\n")
    if int(token_unik) <= 0:
        messagebox.showerror(title='Something is wrong', message="Jumlah token unik tidak boleh 0 atau negatif.")
    token = token.split()
    isAlphaNum = all(element.isalnum() for element in token)
    isLen2 = all(len(element) == 2 for element in token)
    if len(set(token)) != token_unik or not(isAlphaNum) or not(isLen2):
        messagebox.showerror(title='Something is wrong', message="Token harus berupa alphanumeric dan berjumlah sama dengan jumlah token unik")
    if int(buffer_size) < 2:
        messagebox.showerror(title='Something is wrong', message="Ukuran buffer minimal adalah 2.")
    if int(kolom) <= 0 or int(baris) <= 0 or ((int(kolom) * int(baris)) < token_unik):
        messagebox.showerror(title='Something is wrong', message="Ukuran matrix tidak boleh 0 ataupun negatif dan ukuran matrix harus lebih besar dari jumlah token unik.")
    jumlah_seq = int(jumlah_seq)
    if jumlah_seq <= 0:
        messagebox.showerror(title='Something is wrong', message="Jumlah sequence minimal 1.")
    ukuran_max_seq = int(ukuran_max_seq)
    if ukuran_max_seq < 2:
        messagebox.showerror(title='Something is wrong', message="Panjang minimal sequence adalah 2.")
    matrix = [[0 for i in range(int(kolom))] for j in range(int(baris))]
    minimumlength = min(kolom, baris)
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
    start = time.time()
    maxscore, buffer, coordinate = function.bruteForce(matrix, matrix_sequence, buffer_size)
    finish = time.time()
    maxscore2.set(maxscore)
    buffer2.set(buffer)
    time2.set(f"{finish-start:.2f} ms")
    cell_size = 50
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            y1 = i*cell_size + 10
            x1 = j*cell_size + 10
            y2 = y1 + cell_size
            x2 = x1 + cell_size
            if (j+1,i+1) not in coordinate:
                canvas.create_rectangle(x1,y1,x2,y2, outline='green', width=2)
            canvas.create_text(x1+25, y1+25, text=str(matrix[i][j]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            y1 = i*cell_size + 10
            x1 = j*cell_size + 10
            y2 = y1 + cell_size
            x2 = x1 + cell_size
            if (j+1,i+1) in coordinate:
                canvas.create_rectangle(x1,y1,x2,y2, outline='red', width=4)
    for i in range(len(coordinate)-1):
        x1 = (coordinate[i][0] - 1) * cell_size + 35
        y1 = (coordinate[i][1] - 1) * cell_size + 35
        x2 = (coordinate[i+1][0] - 1) * cell_size + 35
        y2 = (coordinate[i+1][1] - 1) * cell_size + 35
        canvas.create_line(x1, y1, x2, y2, fill='red', width=3)
    cell_size2 = 20
    for i in range(len(matrix_sequence)):
        for j in range(len(matrix_sequence[i])):
            y1 = i*cell_size2 + 10
            x1 = j*cell_size2 + 10
            y2 = y1 + cell_size2
            x2 = x1 + cell_size2
            if j != len(matrix_sequence[i])-1:
                canvas2.create_rectangle(x1,y1,x2,y2, outline='green', width=2)
            canvas2.create_text(x1+10, y1+10, text=str(matrix_sequence[i][j]))
    for i in range(len(matrix_sequence)):
        for j in range(len(matrix_sequence[i])):
            y1 = i*cell_size2 + 10
            x1 = j*cell_size2 + 10
            y2 = y1 + cell_size2
            x2 = x1 + cell_size2
            if j == len(matrix_sequence[i])-1:
                canvas2.create_rectangle(x1,y1,x2,y2, outline='red', width=2)
            canvas2.create_text(x1+10, y1+10, text=str(matrix_sequence[i][j]))

window = Tk()
window.geometry("900x800")
window.title("Breach Protocol")
window.config(bg="Black")
frame = Frame(window)
frame.config(bg="white")
frame2 = Frame(window)
frame2.config(bg="black")

frame3 = Frame(window)
frame3.config(bg='black')

canvas = Canvas(frame3, width=400, height=400)
canvas.pack()
frame4 = Frame(window)
frame4.config(bg='black')

frame5 = Frame(window)
frame5.config(bg='white')

labelseq = Label(frame5, text="Sequence: ", width=20)
labelseq.pack(side=TOP)
canvas2 = Canvas(frame5, width=200, height=300)
canvas2.pack()

entry1 = Entry(frame4)
entry1.grid(row=0,column=1)
labelentry1 = Label(frame4, text='Jumlah token: ', width=25).grid(row=0,column=0, padx=5)
entry2 = Entry(frame4)
entry2.grid(row=1,column=1)
labelentry2 = Label(frame4, text='Token unik: ', width=25).grid(row=1,column=0, padx=5)
entry3 = Entry(frame4)
entry3.grid(row=2,column=1)
labelentry3 = Label(frame4, text='Ukuran buffer: ', width=25).grid(row=2,column=0, padx=5)
entry4 = Entry(frame4)
entry4.grid(row=3,column=1)
labelentry4a = Label(frame4, text='Panjang kolom: ', width=25).grid(row=3,column=0, padx=5)
entry4b = Entry(frame4)
entry4b.grid(row=4,column=1)
labelentry4b = Label(frame4, text='Panjang baris: ', width=25).grid(row=4,column=0, padx=5)
entry5 = Entry(frame4)
entry5.grid(row=5,column=1)
labelentry5 = Label(frame4, text='Jumlah sequence: ', width=25).grid(row=5,column=0, padx=5)
entry6 = Entry(frame4)
entry6.grid(row=6,column=1)
labelentry6 = Label(frame4, text='Panjang maksimal sequence: ', width=25).grid(row=6,column=0, padx=5)

fileButton = Button(frame, text="BROWSE", command=openFile, width=5, padx=10).grid(column=0, row= 0, pady=5, padx=10)
saveButton = Button(frame, text='Save', command=saveFile,width=5, padx=10).grid(column=0, row= 5, pady=5, padx=10)
saveButton = Button(frame4, text='Submit', command=submit,width=5, padx=10).grid(column=0, row= 7, pady=5, padx=10)

maxscore2 = StringVar()
labelmaxscore = Label(frame2, text='Reward: ', fg="green", width=10).grid(column=0, row= 0, pady=5, padx=10)
label1 = Label(frame2, textvariable=maxscore2, width=10).grid(column=0, row= 3, pady=(5,5), padx=10)

buffer2 = StringVar()
labelbuffer = Label(frame2, text='Solution: ', fg="green", width=30).grid(column=5, row= 0, pady=5, padx=10)
label2 = Label(frame2, textvariable=buffer2, width=30).grid(column=5, row= 3, pady=(5,5), padx=10)

time2 = StringVar()
labeltime = Label(frame2, text='Time: ', fg="green", width=10).grid(column=10, row= 0, pady=5, padx=(10,20))
label3 = Label(frame2, textvariable=time2, width=10).grid(column=10, row= 3, pady=(5,5), padx=(10,20))



frame.grid(column=0, row=2, padx=20)
frame2.grid(column=0, row=0, pady=20)
frame3.grid(column=0, row=1, ipadx=5, ipady=5)
frame4.grid(column=1, row=0, pady=20, padx=20)
frame5.grid(column=1, row=1)


window.mainloop() 