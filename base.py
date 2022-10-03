

from tkinter import *

from PIL import ImageTk,Image

tablero_jugador_global = None



root = Tk()
root.title('Fase 2')
def ver():#VER SU TABLERO Y MIS DISPAROS
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
    
#ACA VA VER MI ABLERO Y SUS DISPAROS, ES LO MISMOS SOLO CAMBIA EL NOMBRE DE LA FOTO
def logo():
    global username
    global password
    global us
    global pas
    global inge
    top = Toplevel()
    f = Label(top,text="username").pack()
    username = StringVar(top)
    password = StringVar(top)
    us = Entry(top,textvariable=username).pack()
    d = Label(top,text="password").pack()
    pas = Entry(top,textvariable=password).pack()
    def ingr():
        print(f'usuario:{username.get()} y contraseña: {password.get()}')
    inge = Button(top,text="INGRESAR",command=ingr).pack()

def jugar():
    global username
    global password
    global us
    global pas
    global inge
    top = Toplevel()
    f = Label(top,text="tamaño del tablero(el tablero de la computadora se genera automaticamente)").pack()
    username = StringVar(top)
    password = StringVar(top)
    us = Entry(top,textvariable=username).pack()
    d = Label(top,text="ingresar en coordenada").pack()
    pas = Entry(top,textvariable=password).pack()
    def ingr():
        print(f'usuario:{username.get()} y contraseña: {password.get()}')
    inge = Button(top,text="INGRESAR",command=ingr).pack()


    



   
logi = Button(root,text="login",command=logo).pack()

btn = Button(root,text="ver su tablero y mis disparos",command=ver).pack()






mainloop()