#this is to make the front end
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time

filepath = ""
hidden = True



#######functions of each button
#uploads the file 
def open_file():
    file_path = askopenfile(mode='r', filetypes=[
        ('All files', '*.*'),
        ('Image Files', '*jpeg'),
        ('text files', '*.txt')],
    )

    if file_path is not None:
        pass 

    filepath= file_path.name


##takes the string in the textbox 
web = ""
def taketext():
    web = T.text


##Makes the swith turn off or on
def convert(b2):
    if(b2['text']== "OFF"):
        b2["text"]="ON"
        hidden = True
        print("hidden is true")

    elif (b2['text']== "ON"):
        b2["text"]="OFF"
        hidden = False
        print("hidden is false")




###runs the front end off the app
def runtheapp():
    ### Creation of the frame  
    ws = Tk()
    ws.title('BESTResume')
    ws.geometry('500x100') 

    ####cretest the texts 
    adhar = Label(ws, text='Upload your resume: ')
    adhar.grid(row=0, column=0, padx=10)

    adhar2 = Label(ws, text='What website would you like to scan: ')
    adhar2.grid(row=1, column=0, padx=10)

    adhar3 = Label(ws, text='Hide the text: ')
    adhar3.grid(row=2, column=0, padx=10)

    ##creates the buttons and textbox  
    dlbtn = Button(ws, text ='Choose File', command = lambda:open_file()) 
    dlbtn.grid(row=0, column=1)

    #T = Text(height = 1, width = 30, command = taketext())
    #T.grid(row = 1, column=1)

    b2 = Button(text="ON", command=convert(b2))
    b2.grid(row=2,column=1)


    ws.mainloop()
    return hidden, filepath



if __name__ == "__main__":
    values = runtheapp()
    print(values)

