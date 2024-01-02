from tkinter import * 
from tkinter.filedialog import *
from huffman import *

def quitGame(event):
    main_screen.destroy()

main_screen = Tk()
main_screen.title('ENCRYPTO')
main_screen.geometry('940x601') 

#Size of canvas
canvas = Canvas(main_screen,width=950,height=601)

#BG Images
home_IMG = PhotoImage(file="./images/Main.png")
comp_IMG= PhotoImage(file="./images/Compress.png")
decomp_IMG= PhotoImage(file="./images/Decompress.png")
bg_label=Label(main_screen, image=home_IMG) 
bg_label.place(x=0,y=0,relwidth=1,relheight=1) 
canvas.pack()  

def uploadCompFile():
    file = askopenfilename()
    f = open(file, 'r')
    data = f.read()
    freq_table, encoded_text = compress(data)

    o = asksaveasfilename(filetypes=[('text file', '*.txt')], defaultextension= '.txt')

     # Step 3: Open a new file in write-binary mode and write the frequency table and the encoded text to the file.
    with open(o, 'wb') as output_file:
        # Write the frequency table as a JSON-encoded string.
        import json
        freq_table_json = json.dumps(freq_table)
        output_file.write(freq_table_json.encode('utf-8'))

        # Write a newline character to separate the frequency table from the encoded text.
        output_file.write('\n'.encode('utf-8'))

        # Write the encoded text as binary data.
        output_file.write(bytes(encoded_text, 'utf-8'))

    # Step 4: Close the input and output files.
    f.close()
    output_file.close()
    #output_file.close()

def uploadDecompFile():
    file = askopenfilename()

    # Step 1: Open the compressed file in read-binary mode and read the frequency table and encoded text.
    with open(file, 'rb') as input_file:
        # Read the frequency table as a JSON-encoded string.
        freq_table_json = input_file.readline().decode('utf-8').strip()
        # Read the encoded text as binary data.
        encoded_text = input_file.read().decode('utf-8')

    # Step 2: Decode the frequency table from JSON format and convert it to a Python dictionary.
    import json
    freq_table = json.loads(freq_table_json)

    # Step 3: Decompress the encoded text using the `decompress` function.
    text = decompress(freq_table, encoded_text)

    # Step 4: Open a new file in write mode and write the original text to the file.

    o = asksaveasfilename(filetypes=[('text file', '*.txt')], defaultextension= '.txt')

    with open(o, 'w') as output_file:
        output_file.write(text)

    # Step 5: Close the input and output files.
    input_file.close()
    output_file.close()

def comp_WIN():
    bg_comp=Label(main_screen, image=comp_IMG) 
    bg_comp.place(x=0,y=0,relwidth=1,relheight=1)
    b1 = Button(main_screen,text='Compress',height=1,width = 10,fg='white',bg='red',font=('times new roman',22),command=comp_WIN,borderwidth=0)
    b1.place(x=14,y=58)

    b2 = Button(main_screen,text='Decompress',height=1,width = 10,fg='white',bg='red',font=('times new roman',22),command=decomp_WIN,borderwidth=0)
    b2.place(x=14,y=258)

    b3 = Button(main_screen,text='Upload',height=1,width = 8,fg='white',bg='red',font=('times new roman',16),command=uploadCompFile,borderwidth=0)
    b3.place(x=500,y=288)


def decomp_WIN():
    bg_decomp=Label(main_screen, image=decomp_IMG) 
    bg_decomp.place(x=0,y=0,relwidth=1,relheight=1)
    b1 = Button(main_screen,text='Compress',height=1,width = 10,fg='white',bg='red',font=('times new roman',22),command=comp_WIN,borderwidth=0)
    b1.place(x=14,y=58)

    b2 = Button(main_screen,text='Decompress',height=1,width = 10,fg='white',bg='red',font=('times new roman',22),command=decomp_WIN,borderwidth=0)
    b2.place(x=14,y=258)

    b3 = Button(main_screen,text='Upload',height=1,width = 8,fg='white',bg='red',font=('times new roman',16),command=uploadDecompFile,borderwidth=0)
    b3.place(x=500,y=288)


#Buttons
b1 = Button(main_screen,text='Compress',height=1,width = 10,fg='white',bg='red',font=('times new roman',22),command=comp_WIN,borderwidth=0)
b1.place(x=14,y=58)

b1 = Button(main_screen,text='Decompress',height=1,width = 10,fg='white',bg='red',font=('times new roman',22),command=decomp_WIN,borderwidth=0)
b1.place(x=14,y=258)

main_screen.mainloop()