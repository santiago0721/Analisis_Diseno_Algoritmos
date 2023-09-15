import pandas as pd
import json
import requests
from pandas import json_normalize


link = "https://www.datos.gov.co/resource/av5s-m74z.json"
datos = requests.get(link)
data = json.loads(datos.text)
data = json_normalize(data)
#print(data)

prueba = data.to_numpy().tolist()


def Merge(lista_izq,lista_der):
    lista_resultados= []

    while(len(lista_izq)>0 and len(lista_der)>0):
        if lista_izq[0] < lista_der[0]:
            lista_resultados.append(lista_izq[0])
            lista_izq = lista_izq[1:]
        else:
            lista_resultados.append(lista_der[0])
            lista_der = lista_der[1:]
    if len(lista_der) > 0:
        lista_resultados += lista_der
    else:
        lista_resultados += lista_izq

    return lista_resultados


def MergeSort(lista):
    #caso base
    base = len(lista)
    if base <= 1:
        return lista
    lista_izquierda= lista[:len(lista)//2]
    lista_derecha =  lista[len(lista)//2:]


    lista_izquierda = MergeSort(lista_izquierda)
    lista_derecha = MergeSort(lista_derecha)

    return(Merge(lista_izquierda,lista_derecha))


arreglo= [1,2,7,1,-1,43,0]
print(MergeSort(prueba))
