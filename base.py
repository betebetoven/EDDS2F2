
from tkinter import *

from PIL import ImageTk,Image
from django.forms import PasswordInput



root = Tk()
root.title('Fase 2')
def ver():
    global compu
    global disp_jug
    global uwu

    top = Toplevel()
    f = Label(top,text="TABLERO COMPUTADORA").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('compu.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)

    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_jug.png').resize((400,400)))
    my_label2 = Label(top, image=disp_jug).pack(side = LEFT, fill = Y)
    
    
   

btn = Button(root,text="ver foto",command=ver).pack()






mainloop()