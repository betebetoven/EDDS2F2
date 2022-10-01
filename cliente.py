from time import process_time_ns
from traceback import print_tb
import requests##pip3 install request
import json
from tkinter.filedialog import askopenfilename

from matriz import matriz



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

           

if __name__ == '__main__':
    #carga_masiva(entrada())
    #login("betebetoven","jaja")
    #editN("beto")
    #editP("mama")
   # KS("yes")
    #login("colosho","colosho")
    m = matriz(11)
    print(m.ingresar(1,1,"kkita"))
    print(m.ingresar(0,1,"buque"))
    print(m.ingresar(0,0,"beso"))
    print(m.ingresar(0,3,"antesfinal"))
    print(m.ingresar(1,3,"antesfinal"))
    print(m.ingresar(2,3,"antesfinal"))
    print(m.ingresar(3,3,"final"))
    print(m.ingresar(10,1,"hoysi"))
    print(m.ingresar(1,0,"hoysi"))
    print(m.ingresar(10,0,"hoysi"))
    print(m.ingresar(10,0,"hoysi2"))
    print(m.ingresar(10,10,"final"))
    print(m.ingresar(0,10,"final"))
    print(m.ingresar(10,0,"final"))
   
    print(str(m.raiz.derecha.abajo))
    print(str(m.raiz.abajo.derecha))
    print(id(m.raiz.derecha.abajo)==id(m.raiz.abajo.derecha))
    print(str(m.raiz.derecha.derecha.abajo))
    print(str(m.raiz.abajo.abajo.derecha.derecha))
    print(id(m.raiz.derecha.derecha.abajo)==id(m.raiz.abajo.abajo.derecha.derecha))
    print(str(m.raiz.derecha.abajo.abajo))
    print(str(m.raiz.abajo.abajo.derecha))
    print(id(m.raiz.derecha.abajo.abajo)==id(m.raiz.abajo.abajo.derecha))
    print(str(m.raiz.derecha.derecha.derecha.derecha.abajo))
    print(str(m.raiz.abajo.abajo.abajo.abajo.derecha))
    print(id(m.raiz.derecha.derecha.derecha.derecha.abajo)==id(m.raiz.abajo.abajo.abajo.abajo.derecha))
    for n in m.ocupados:
        print(str(n))
    m.muestra()
    m.muestrac()
    m.eliminar(0,0)
    m.eliminar(10,10)
    m.eliminar(0,10)
    m.eliminar(10,0)
    m.eliminar(5,5)
    m.muestra()
    m.muestrac()

    for n in m.ocupados:
        print(str(n))





  
   
    
    


    
   