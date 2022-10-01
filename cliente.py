from time import process_time_ns
from traceback import print_tb
import requests##pip3 install request
import json
from tkinter.filedialog import askopenfilename
import random
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
    m = matriz(10)
    m.llenadoautom(random.randint(0,9),random.randint(0,9),"pt")
    m.llenadoautom(random.randint(0,9),random.randint(0,9),"pt")
    m.llenadoautom(random.randint(0,9),random.randint(0,9),"pt")
    m.llenadoautom(random.randint(0,9),random.randint(0,9),"pt")
    m.muestra()
    m.muestrac()
    for n in m.ocupados:
        print(str(n))






  
   
    
    


    
   