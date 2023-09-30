from tkinter import *

window = Tk()

window.geometry('200x200')
window['bg'] = '#8CD5D9'
window.title('Перевод на азбука морзе')

def perevot ():
    ganvo = ['.-','-...','-.-.','-..','.','..-.','--.','....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    
    leterr = leter.get()
    lenn = len(leterr)
    gavno_ru = []
    
    for i in range(lenn):
        a = leterr[i].lower()
        ordleterr = ord(a)
        gavno_ru.append(ganvo[ordleterr - 97])
        
    labes['text'] = ''.join([i for i in gavno_ru])    
leter = StringVar()

enter = Entry(textvariable=leter, bg='#DAE6B3')
enter.place(relx=0.2, rely=0.2)

button = Button(bg='#DAE6B3', text='Перевод', command=perevot)
button.place(relx=0.35, rely=0.4)

labes = Label(bg='#DAE6B3', text='...---...')
labes.place(relx=0.4, rely=0.65)

window.mainloop()
