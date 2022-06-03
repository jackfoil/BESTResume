#this is the main code (that I created)
from createwatermark import *
from merg import *

#this is to make the front end
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 




if __name__ == "__main__":
    ### Creation of the frame  
    ws = Tk()
    ws.title('BESTResume')
    ws.geometry('500x100')

    sendoff = []
    hidden = True
    web = ""


    ####cretest the texts 
    adhar = Label(ws, text='Upload your resume: ')
    adhar.grid(row=0, column=0, padx=10)

    adhar2 = Label(ws, text='What website would you like to scan: ')
    adhar2.grid(row=1, column=0, padx=10)

    adhar3 = Label(ws, text='Hide the text: ')
    adhar3.grid(row=2, column=0, padx=10)

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

        global filepath

        filepath=file_path.name

    ##gets the text from the box
    def getTextInput():
        result=T.get("1.0", "end")
        return result


    ##Makes the swith turn off or on
    def convert():
        if(b2['text']== "OFF"):
            b2["text"]="ON"

        elif (b2['text']== "ON"):
            b2["text"]="OFF"


    ####this will develope the watermarked resume 
    def start():        
        web = getTextInput()

        if(b2['text']== "OFF"):
            hidden = False
        else:
            hidden = True

        sendoff.append(filepath)
        sendoff.append(web.strip())
        sendoff.append(hidden)
        print(sendoff)

        createwatermark(sendoff[1], 2, 200, sendoff[2])
        print("watermark is done")
        merging(sendoff[0], 'watermark.pdf')
        print("Resume is done")
        #"https://www.onetonline.org/link/summary/25-1021.00"


    ##creates the buttons and textbox  
    dlbtn = Button(ws, text ='Choose File', command = lambda:open_file()) 
    dlbtn.grid(row=0, column=1)

    T = Text(height = 1, width = 30)
    T.grid(row = 1, column=1)

    b2 = Button(text="ON", command=convert)
    b2.grid(row=2,column=1)

    b3 = Button(text="Submit", command=start)
    b3.grid(row=3,column=1)

    ws.mainloop()

    










