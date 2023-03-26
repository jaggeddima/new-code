from tkinter import *

root = Tk()

root.geometry('200x200')
root['bg'] = '#8CD5D9'
root.title('Оценки')

def Proverka () :
    n1 = st.get()
    n2 = nd.get()
    n3 = rd.get()
    n4 = th.get()
    RE = R.get()
    
    if n1 == '2':
        t1 = 2.
    elif n1 == '3':
        t1 = 3.
    elif n1 == '4':
        t1 = 4.
    elif n1 == '5':
        t1 = 5.
        
    if n2 == '2':
        t2 = 2.
    elif n2 == '3':
        t2 = 3.
    elif n2 == '4':
        t2 = 4.
    elif n2 == '5':
        t2 = 5.
        
    if n3 == '2':
        t3 = 2.
    elif n3 == '3':
        t3 = 3.
    elif n3 == '4':
        t3 = 4.
    elif n3 == '5':
        t3 = 5.
        
    if n4 == '2':
        t4 = 2.
    elif n4 == '3':
        t4 = 3.
    elif n4 == '4':
        t4 = 4.
    elif n4 == '5':
        t4 = 5.
        
    if RE == '2':
        ER = 2.
    elif RE == '3':
        ER = 3.
    elif RE == '4':
        ER = 4.
    elif RE == '5':
        ER = 5.
        
    P = t1 + t2
    PP = P / 2
    S = t3 + t4
    SS = S / 2
    PS = PP + SS
    PPSS = PS / 2
    PSR = PPSS + ER
    PSRR = PSR / 2
    
    l['text'] = PSRR

st = StringVar()
nd = StringVar()
rd = StringVar()
th = StringVar()
R = StringVar()

EN1 = Entry(textvariable=st, bg='#DAE6B3')
EN2 = Entry(textvariable=nd, bg='#DAE6B3')
EN3 = Entry(textvariable=rd, bg='#DAE6B3')
EN4 = Entry(textvariable=th, bg='#DAE6B3')
REN = Entry(textvariable=R, bg='#541c3d')
EN1.pack()
EN2.pack()
EN3.pack()
EN4.pack()
REN.pack()

B = Button(text='Проверка  отметок', bg='#7740BF', command=Proverka)
B.place (relx=0.2, rely=0.5)

l = Label(text=0, bg='#7740BF')
l.place (relx=0.45, rely=0.65)

root.mainloop()