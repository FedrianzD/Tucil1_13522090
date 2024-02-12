from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import function
import time
maxscore = ""
buffer = ""
coordinate = ""
start = ''
finish = ''
matrix = []
label_matrix = []
def openFile():
    global maxscore, buffer, coordinate, finish, start, matrix, label_matrix
    for label_row in label_matrix:
            for label in label_row:
                label.destroy()
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
    buffer2.set(buffer)
    time2.set(f"{finish-start:.2f} ms")
    for i in range(len(matrix)):
        label_row = []
        for j in range(len(matrix[0])):
            if (j+1, i+1) in coordinate:
                label = Label(frame3, text=matrix[i][j], borderwidth=1, relief="solid", width=10, height=4, bg='red')
            else:
                label = Label(frame3, text=matrix[i][j], borderwidth=1, relief="solid", width=10, height=4)
            label.grid(row=i, column=j)
            label_row.append(label)
        label_matrix.append(label_row)
    

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


    

window = Tk()
window.geometry("800x800")
window.config(bg="Black")
frame = Frame(window)
frame.config(bg="black")
frame2 = Frame(window)
frame2.config(bg="black")

frame3 = Frame(window)
frame3.config(bg='black')


fileButton = Button(frame, text="BROWSE", command=openFile, width=5, padx=10).grid(column=0, row= 0, pady=5, padx=10)
saveButton = Button(frame, text='Save', command=saveFile,width=5, padx=10).grid(column=0, row= 5, pady=5, padx=10)

maxscore2 = StringVar()
labelmaxscore = Label(frame2, text='Reward: ', fg="green", width=10).grid(column=0, row= 0, pady=5, padx=10)
label1 = Label(frame2, textvariable=maxscore2, width=10).grid(column=0, row= 3, pady=(5,50), padx=10)

buffer2 = StringVar()
labelbuffer = Label(frame2, text='Solution: ', fg="green", width=30).grid(column=5, row= 0, pady=5, padx=10)
label2 = Label(frame2, textvariable=buffer2, width=30).grid(column=5, row= 3, pady=(5,50), padx=10)

time2 = StringVar()
labeltime = Label(frame2, text='Time: ', fg="green", width=10).grid(column=10, row= 0, pady=5, padx=(10,20))
label3 = Label(frame2, textvariable=time2, width=10).grid(column=10, row= 3, pady=(5,50), padx=(10,20))



frame.grid(column=0, row=5, padx=20)
frame2.grid(column=3, row=0, pady=20)
frame3.grid(column=3, row=5, ipadx=5, ipady=5)


window.mainloop() 