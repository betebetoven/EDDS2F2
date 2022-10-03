



from tkinter import *
from tkinter.ttk import Combobox
import requests##pip3 install request
import json
from tkinter.filedialog import askopenfilename
import random
from matriz import matriz

from PIL import ImageTk,Image

tablero_jugador_global = None
tablero_computadora_global = None
tablero_disparos_computadora_global = None
tablero_disparos_jugador_global = None

base_url = "http://3.88.228.81:8080/"
def entrada():
    f = open(askopenfilename(), "r")
    return f.read()
def carga_masiva(entrada):
    res = requests.post(f'{base_url}/Lista/{entrada}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def login(usuario, contraseña):
    res = requests.post(f'{base_url}/Login/{usuario},{contraseña}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def editN(nombre):
    res = requests.post(f'{base_url}/editN/{nombre}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def editP(nombre):
    res = requests.post(f'{base_url}/editP/{nombre}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def KS(nombre):#EL PARAMETRO DE ENTRADA LO DEJAMOS NADA MAS PARA CONFIRMACION
    res = requests.post(f'{base_url}/KS/{nombre}')
    data = res.text#convertimos la respuesta en dict
    print(data)

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
def ver2():#VER MI TABLERO Y MIS DISPAROS
    global compu
    global disp_jug
    global uwu
    top = Toplevel()
    f = Label(top,text="TABLERO JUGADOR").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('mitablero.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)
    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_jug.png').resize((400,400)))
    my_label2 = Label(top, image=disp_jug).pack(side = LEFT, fill = Y)
def ver3():#VER SU TABLERO Y SUS DISPAROS
    global compu
    global disp_jug
    global uwu
    top = Toplevel()
    f = Label(top,text="TABLERO COMPUTADORA").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('compu.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)
    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_compu.png').resize((400,400)))
    my_label2 = Label(top, image=disp_jug).pack(side = LEFT, fill = Y)
def ver4():#VER MI TABLERO Y SUS DISPAROS
    global compu
    global disp_jug
    global uwu
    top = Toplevel()
    f = Label(top,text="TABLERO JUGADOR").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('mitablero.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)
    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_compu.png').resize((400,400)))
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
        login(username.get(),password.get())
        print(f'usuario:{username.get()} y contraseña: {password.get()}')
        jugar()
    inge = Button(top,text="INGRESAR",command=ingr).pack()

def jugar():
    global dimension
    global dx
    global dy
    global ddx
    global ddy
    global barco
    global d
    global pas
    global inge
    global ingee
    global ingeee
    global cbb
    global selected_month
    global edit
    top = Toplevel()
    dimension = StringVar(top)
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    barco = StringVar(top)
    selected_month = StringVar(top)
    dime = Label(top,text="DIMENSION DE TABLERO:").pack()
    d = Entry(top,textvariable=dimension).pack()
    dl = Label(top,text="x:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    dll = Label(top,text="y:").pack( )
    dy = Entry(top,textvariable=ddy).pack()
    dlll = Label(top,text="barco:").pack( )
    cbb = Combobox(top,textvariable=selected_month)
    cbb['values']= ['pt','sub','dt','b']
    cbb['state']='readonly'
    cbb.pack()
    def ingr():
        print(f'dimension:{dimension.get()} ')
    def ingr2():
        print(f' coordenadas: {ddx.get()},{ddy.get()}  barco:{selected_month.get()}')
    def ingr3():
        print(f'VAMO A JUGA')
    inge = Button(top,text="CREAR TABLERO",command=ingr).pack()
    ingee = Button(top,text="AGREGAR BARCO",command=ingr2).pack()
    ingeee = Button(top,text="JUGAR",command=jugar_si).pack()
    edit = Button(top,text="editar informacion",command=editar_informacion).pack()
def jugar_si():
    
    global dx
    global dy
    global ddx
    global ddy
    
    
    global pas
    global inge
    global ingee
    global ingeee
    global cbb
    global ing
    
    top = Toplevel()
    
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    
    
    dime = Label(top,text="DISPARA:").pack()
    dl = Label(top,text="x:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    dll = Label(top,text="y:").pack( )
    dy = Entry(top,textvariable=ddy).pack()
    def ingr():
        print(f' DISPARO: {ddx.get()},{ddy.get()}  barco:{selected_month.get()}')
    def ingr2():
        print(f' coordenadas: {ddx.get()},{ddy.get()}  barco:{selected_month.get()}')
    def ingr3():
        print(f'VMUSTRA MI TABLERO Y MIS DISPAROS')
    
    ingee = Button(top,text="ver __SU__ tablero y MIS disparos",command=ver).pack()
    ingeee = Button(top,text="ver __MI__ tablero y MIS disparos",command=ver2).pack()
    inge = Button(top,text="ver __SU__ tablero y SUS disparos",command=ver3).pack()
    ing = Button(top,text="ver __MI__ tablero y SUS disparos",command=ver4).pack()

def editar_informacion():
    global dimension
    global dx
    global ddx
    global d
    global inge
    global ingee
    global ingeee
    top = Toplevel()
    dimension = StringVar(top)
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    barco = StringVar(top)
    selected_month = StringVar(top)
    dime = Label(top,text="cambiar nombre:").pack()
    d = Entry(top,textvariable=dimension).pack()
    dl = Label(top,text="cambiar contraseña:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    def ingr():
        editN(dimension.get())
        print(f'cambio de nomre:{dimension.get()} ')
    def ingr2():
        editP(ddx.get())
        print(f' cambio de contraseña: {ddx.get()}')
    def ingr3():
        KS("si")
        print(f'elimino cuenta, regresar a login')
    inge = Button(top,text="editar nombre",command=ingr).pack()
    ingee = Button(top,text="editar contraseña",command=ingr2).pack()
    ingeee = Button(top,text="eliminar cuenta",command=ingr3).pack()
    
def cm():
    carga_masiva(entrada())


   
logi = Button(root,text="login",command=logo).pack()
cmm = Button(root,text="CARGA MASIVA",command=cm).pack()

#btn = Button(root,text="ver su tablero y mis disparos",command=ver).pack()






mainloop()