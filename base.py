




from ast import Lambda, main
from glob import glob
import threading as th
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox
import requests##pip3 install request
import json
from tkinter.filedialog import askopenfilename
import random
import os
from matriz import matriz
from matriz import par
import time
from bloqueBC import bloque
from BlockChain import blockchain
from merkletree import MLKjunior
from Hastable import jacinto
from sha256 import shasha
from skin import skin
from adress import direccion_from
from tkinter import ttk


from PIL import ImageTk,Image

tablero_jugador_global = None
tablero_computadora_global = None
tablero_disparos_computadora_global = None
tablero_disparos_jugador_global = None
direccion = "one"
base_url = "http://3.88.228.81:8080/"


BLOCKCHAIN_GLOBAL = blockchain()
HASHTABLE_GLOBAL = jacinto()
ID_USUARIO_GLOBAL = 0
ADDRESS_USUARIO_GLOBAL = direccion_from()

FROM_GLOBAL = ""




def entrada():
    global direccion
    direccion = askopenfilename()
    f = open(direccion, "r")
    return f.read()
def carga_masiva(entrada):
    res = requests.post(f'{base_url}/Lista/{entrada}')
    data = res.text#convertimos la respuesta en dict
    
    f = open(f'arbolb.dot', "w")
    f.write(data)
    f.close()
    os.system(f'dot -Tpng arbolb.dot -o arbolb.png')


    ver5()
    print(data)
def login(usuario, contraseña):
    global ADDRESS_USUARIO_GLOBAL
    global ID_USUARIO_GLOBAL
    ADDRESS_USUARIO_GLOBAL.new()
    res = requests.post(f'{base_url}/Login/{usuario},{contraseña}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("LOGIN",data)
    aDict = json.loads(data)
    ID_USUARIO_GLOBAL = int(aDict["id"])
    messagebox.showerror("ala verga",f'el id es_{ID_USUARIO_GLOBAL}')
    
    print(data)
def editN(nombre):
    res = requests.post(f'{base_url}/editN/{nombre}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("CAMBIO DE NOMBRE",data)
    print(data)
def editP(nombre):
    res = requests.post(f'{base_url}/editP/{nombre}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("CAMBIO DE CONTRASEÑA",data)
    print(data)
def KS(nombre):#EL PARAMETRO DE ENTRADA LO DEJAMOS NADA MAS PARA CONFIRMACION
    res = requests.post(f'{base_url}/KS/{nombre}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("ELIMINACION",data)
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
def ver5():#VER MI TABLERO Y SUS DISPAROS
    global compu
    top = Toplevel()
    f = Label(top,text="ARBOL B").pack()
    compu = ImageTk.PhotoImage(Image.open('arbolb.png').resize((1200,700)))
    my_label = Label(top, image=compu).pack()
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
    global vt
    global g2
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
        global tablero_computadora_global
        global tablero_disparos_computadora_global
        global tablero_jugador_global
        global tablero_disparos_jugador_global
        tablero_computadora_global = matriz(int(dimension.get()))
        tablero_computadora_global.para_compu()
        tablero_disparos_computadora_global = matriz(int(dimension.get()))
        tablero_jugador_global = matriz(int(dimension.get()))
        tablero_jugador_global.para_compu()#ESTO SOLO ES PARA AUTOMATIAR, CAMBIAR LAS MIERDAS DESPUES
        tablero_disparos_jugador_global = matriz(int(dimension.get()))
        jesus = ""
        for n in tablero_jugador_global.inv:
            jesus+= "\n"+str(n["nombre"])+" :"
            for j in n["listacor"]:
                jesus+= "\n"+str(j)
        messagebox.showinfo("1: ", jesus)

    def ingr2():
        global tablero_computadora_global
        global tablero_disparos_computadora_global
        global tablero_jugador_global
        global tablero_disparos_jugador_global
        if tablero_jugador_global.llenadomanual(int(ddx.get()),int(ddy.get()),selected_month.get()):
            messagebox.showinfo("INGRESO","INGRESAD CORRECTAMENTE")
            print("SI LO PUDO INGRESAR MANUAL_______________________________________________")
        else:
            messagebox.showerror("ERROR","CASILLA OCUPADA O NO HAY ESPACIOS CERCA")
            print("NO LO PUDO INGRESAR MANUAL_______________________________________________")
        print(f' coordenadas: {ddx.get()},{ddy.get()}  barco:{selected_month.get()}')
    def ingr3():
        print(f'VAMO A JUGA')
    inge = Button(top,text="CREAR TABLERO",command=ingr).pack()
    ingee = Button(top,text="AGREGAR BARCO",command=ingr2).pack()
    ingeee = Button(top,text="JUGAR",command=jugar_si).pack()
    edit = Button(top,text="editar informacion",command=editar_informacion).pack()
    vt = Button(top,text="VER TIENDA",command=ver6).pack()
    g2 = Button(top,text="JUGAR DOS JUGADORES",command=jug2).pack()

def contains(x,y,parv):
    cont = 0
    for n in parv:
        if n.x == x and n.y == y:
            parv.pop(cont)
            return True
        cont = cont+1
    return False


def dispara(mo,mh,x,y):
    mh.grafo.agrega(x,y)
    if(mo.eliminar(x,y)):
        mh.ingresar(x,y,"golpe")
        
        messagebox.showinfo("DISPARO","LE DISTE")
        for n in mo.inv:
            if contains(x,y,n["listacor"]) :
                messagebox.showinfo("DISPARO",f'LE DISTE A UN {str(n["nombre"])}')
                if len(n["listacor"]) == 0:
                    messagebox.showinfo("HUNDISTE",f'HUNDISTE A UN {str(n["nombre"])}')
                    mo.inv.remove(n)
                    messagebox.showinfo("info",f'HUNDISTE A UN {str(mo.inv)}')



        print("LE DISTE------------------------")
    else:
        mh.ingresar(x,y,"missed")
        messagebox.showerror("DISPARO","FALLASTE")
        print("FALLASTE------------------------")
    


def jugar_si():
    global tablero_computadora_global
    global tablero_disparos_computadora_global
    global tablero_jugador_global
    global tablero_disparos_jugador_global
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
    global fire
    global ataque_de_racimo
    tablero_computadora_global.grapvzix("compu")
    tablero_disparos_jugador_global.grapvzix("disp_jug")
    tablero_jugador_global.grapvzix("mitablero")
    tablero_disparos_computadora_global.grapvzix("disp_compu")
    top = Toplevel()
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    dime = Label(top,text="DISPARA:").pack()
    dl = Label(top,text="x:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    dll = Label(top,text="y:").pack( )
    dy = Entry(top,textvariable=ddy).pack()
    def ingr():
        #dispara usuario
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,int(ddx.get()),int(ddy.get()))
        #dispara a computadora
        dispara(tablero_jugador_global,tablero_disparos_computadora_global,random.randint(0,9),random.randint(0,9))
        tablero_computadora_global.grapvzix("compu")
        tablero_disparos_jugador_global.grapvzix("disp_jug")
        tablero_jugador_global.grapvzix("mitablero")
        tablero_disparos_computadora_global.grapvzix("disp_compu")
        print(f' DISPARO: {ddx.get()},{ddy.get()}')
    def ingr3():
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,0,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,1,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,2,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,3,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,4,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,5,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,6,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,7,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,8,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,9,2)
        tablero_computadora_global.grapvzix("compu")
        tablero_disparos_jugador_global.grapvzix("disp_jug")
        tablero_jugador_global.grapvzix("mitablero")
        tablero_disparos_computadora_global.grapvzix("disp_compu")
        print(f'ataque de racismo')
    fire = Button(top,text="DISPARA",command=ingr).pack()
    ataque_de_racimo = Button(top,text="ATAQUE DE RACIMO",command=ingr3).pack()
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

def jug2():
    global tablero_computadora_global
    global tablero_disparos_computadora_global
    global tablero_jugador_global
    global tablero_disparos_jugador_global
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
    global fire
    global fire2
    global ataque_de_racimo
    tablero_computadora_global.grapvzix("compu")
    tablero_disparos_jugador_global.grapvzix("disp_jug")
    tablero_jugador_global.grapvzix("mitablero")
    tablero_disparos_computadora_global.grapvzix("disp_compu")
    top = Toplevel()
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    dime = Label(top,text="DISPARA:").pack()
    dl = Label(top,text="x:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    dll = Label(top,text="y:").pack( )
    dy = Entry(top,textvariable=ddy).pack()
    def ingr():
        #dispara jugador 1
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,int(ddx.get()),int(ddy.get()))
        #dispara a computadora
        #dispara(tablero_jugador_global,tablero_disparos_computadora_global,random.randint(0,9),random.randint(0,9))
        tablero_computadora_global.grapvzix("compu")
        tablero_disparos_jugador_global.grapvzix("disp_jug")
        tablero_jugador_global.grapvzix("mitablero")
        tablero_disparos_computadora_global.grapvzix("disp_compu")
        tablero_disparos_jugador_global.grafo.graphvix('grafo')
        print(f' DISPARO: {ddx.get()},{ddy.get()}')
    def ingr2():
        #dispara jugador 2
        #dispara(tablero_computadora_global,tablero_disparos_jugador_global,int(ddx.get()),int(ddy.get()))
        #dispara a computadora
        dispara(tablero_jugador_global,tablero_disparos_computadora_global,int(ddx.get()),int(ddy.get()))
        tablero_computadora_global.grapvzix("compu")
        tablero_disparos_jugador_global.grapvzix("disp_jug")
        tablero_jugador_global.grapvzix("mitablero")
        tablero_disparos_computadora_global.grapvzix("disp_compu")
        tablero_disparos_computadora_global.grafo.graphvix('grafo2')
        print(f' DISPARO: {ddx.get()},{ddy.get()}')

    
    fire = Button(top,text="DISPARA Jugador 1",command=ingr).pack()
    fire2 = Button(top,text="DISPARA Jugador 2",command=ingr2).pack()
    #ingee = Button(top,text="ver jugador 2 y disparos jugador 1",command=ver).pack()
    ingeee = Button(top,text="ver tablero jugador 1 y disparos jugador 1",command=ver2).pack()
    inge = Button(top,text="ver tablero jugador 2 y disparos jugador 2",command=ver3).pack()
    #ing = Button(top,text="ver tablero jugador 1 y disparos jugador 2",command=ver4).pack()

def justpas():
    pass

def carrito():
    global HASHTABLE_GLOBAL
    global varints_carrito
    global checkbutons_carrito
    global fr
    varints_carrito = []
    checkbutons_carrito= []
    
    top = Toplevel()
    top.geometry("500x400")
    mainframe = Frame(top)
    mainframe.pack(fill=BOTH,expand=1)
    my_canvas = Canvas(mainframe)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    my_scrollbar = ttk.Scrollbar(mainframe,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")





    #frame = VerticalScrolledFrame(top)
    #frame.pack()
    f = Label(second_frame,text="CARRITO").pack()
    fr = Label(second_frame,text=f'total: {HASHTABLE_GLOBAL.total()}').pack()
    cosas_array = HASHTABLE_GLOBAL.toArray()
    global ID_USUARIO_GLOBAL
    HASHTABLE_GLOBAL.prettytable_llenos(ID_USUARIO_GLOBAL)
    for n in HASHTABLE_GLOBAL.toArray():
        print(n)
    for n in cosas_array:
        new = IntVar()
        varints_carrito.append(new)
        checkbutons_carrito.append(Checkbutton(second_frame, text=f'{n.nombre}\n{n.precio}',variable=new, onvalue=1, offvalue=0, command=justpas))
    for n in checkbutons_carrito:
        n.pack()
    def eliminar_del_carrito():
        for n in range(len(varints_carrito)):
            if (varints_carrito[n].get() == 1):
                HASHTABLE_GLOBAL.eliminar(cosas_array[n].nombre)
                checkbutons_carrito[n].destroy()
                cosas_array.remove(cosas_array[n])
                varints_carrito.remove(varints_carrito[n])
                checkbutons_carrito.remove(checkbutons_carrito[n])
                HASHTABLE_GLOBAL.prettytable_llenos(ID_USUARIO_GLOBAL)
                messagebox.showwarning("NUEVO TOTAL",f'total: {HASHTABLE_GLOBAL.total()}\n TAMAÑO DE TABLA HASH: {HASHTABLE_GLOBAL.tamaño}\n TAMAÑO DEL CARRITO: {HASHTABLE_GLOBAL.ocupacion}\n PORCENTAJE DE OCUPACION: {HASHTABLE_GLOBAL.definir_porcentaje_ocupacion()}')
                #fr.config(text = f'total: {HASHTABLE_GLOBAL.total()}')
                return True
        messagebox.showwarning("NUEVO TOTAL",f'total: {HASHTABLE_GLOBAL.total()}\n TAMAÑO DE TABLA HASH: {HASHTABLE_GLOBAL.tamaño}\n TAMAÑO DEL CARRITO: {HASHTABLE_GLOBAL.ocupacion}\n PORCENTAJE DE OCUPACION: {HASHTABLE_GLOBAL.definir_porcentaje_ocupacion()}')
        HASHTABLE_GLOBAL.prettytable_llenos(ID_USUARIO_GLOBAL)

    malboro = Button(second_frame,text="eliminar del carrito",command=eliminar_del_carrito).pack()
    malbor = Button(second_frame,text="COMPRAR",command=justpas).pack()







def ver6():#VER MI TABLERO Y SUS DISPAROS
    global varints
    global checkbutons
    global skis
    global precios
    global HASHTABLE_GLOBAL
    global ID_USUARIO_GLOBAL
    
    hashtable_auxiliar = jacinto()
    top = Toplevel()
    top.geometry("500x400")
    mainframe = Frame(top)
    mainframe.pack(fill=BOTH,expand=1)
    my_canvas = Canvas(mainframe)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    my_scrollbar = ttk.Scrollbar(mainframe,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")







    f = Label(second_frame,text="TIENDA").pack()
    global direccion
    f = open(direccion, "r")
    stienda =  json.loads(f.read())["articulos"]
    total = 0
    f0 = Label(second_frame,text=f'EL TOTAL ES: {total}').pack()
    #HASHTABLE_GLOBAL = jacinto()
    varints = []
    checkbutons =[]
    skis = []
    precios = []
    def agregahash():

        pass
    def comprar():
        pass
    def vertotal():
        HASHTABLE_GLOBAL.reinicio()
        
        for n in range(len(varints)):
            if (varints[n].get() == 1):
                HASHTABLE_GLOBAL.agrega_inicial(ID_USUARIO_GLOBAL,skis[n])
        settotal()
        HASHTABLE_GLOBAL.prettytable_llenos(ID_USUARIO_GLOBAL)
        
        #HASHTABLE_GLOBAL = new_has
        
        
        

    def settotal():
        #global f0
        total = HASHTABLE_GLOBAL.total()
        #f0.config(text=f'EL TOTAL ES: {total}')
        messagebox.showinfo("TOTAL",f'SU TOTAL ES DE: {total} \n TAMAÑO DE TABLA HASH: {HASHTABLE_GLOBAL.tamaño}\n TAMAÑO DEL CARRITO: {HASHTABLE_GLOBAL.ocupacion}\n PORCENTAJE DE OCUPACION: {HASHTABLE_GLOBAL.definir_porcentaje_ocupacion()}')
    

    for c in stienda :
        
        print(c["id"])
        print(c["categoria"])
        print(c["precio"])
        print(c["nombre"])
        new = IntVar()
        varints.append(new)
        skis.append(skin(c["nombre"],int(c["precio"])))
        precios.append(int(c["precio"]))
        checkbutons.append(Checkbutton(second_frame, text=f'{c["id"]}\n{c["categoria"]}\n{c["precio"]}\n{c["nombre"]}',variable=new, onvalue=1, offvalue=0, command=agregahash))

    for n in checkbutons:
        n.pack()
    vtot = Button(second_frame,text="VER TOTAL",command=vertotal).pack()
    malboro = Button(second_frame,text="VER CARRITO",command=carrito).pack()
    #sb = Scrollbar(top)


    

    """for c in stienda :
        
        print(c["id"])
        f0 = Label(top,text=c["id"]).pack()
        print(c["categoria"])
        f2 = Label(top,text=c["categoria"]).pack()
        print(c["precio"])
        f3 = Label(top,text=c["precio"]).pack()
        print(c["nombre"])
        f00 = Label(top,text=c["nombre"]).pack()
        def agregaahashauxiliar():
         
            hashtable_auxiliar.agrega_inicial(2,skin(f00.cget("text"),f3.cget("text")))
        mnb = Button(top,text="COMPRAR",command=agregaahashauxiliar).pack()"""
    #sb = Scrollbar(top)
    #sb.config(command = top.yview )
    #sb.pack(side = LEFT, fill = RIGHT)


   
logi = Button(root,text="login",command=logo).pack()
cmm = Button(root,text="CARGA MASIVA",command=cm).pack()

#btn = Button(root,text="ver su tablero y mis disparos",command=ver).pack()
#COMIENZA TRABAJO DEL BLOCKCHAIN






def display(msg):  
    print(msg + ' ' + time.strftime('%H:%M:%S'))  
  
##Basic timer  
def run_once():  
    display('run_once:')  
    t=th.Timer(600,display,['Timeout:'])  
    t.start()#Here run is called  
run_once()  
##Runs immediately and once  
print('Waiting.....')  
  
##Lets make our timer run in intervals  
##Put it into a class  
class RepeatTimer(th.Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  
            print(' ')  
##We are now creating a thread timer and controling it  
timer = RepeatTimer(5,display,['Repeating'])  
timer.start() #recalling run  
print('Threading started')  
mainloop()
time.sleep(10)#It gets suspended for the given number of seconds  
print('Threading finishing')  
timer.cancel()




