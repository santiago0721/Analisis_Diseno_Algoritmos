def quick(lista):
    #caso base
    base=len(lista)
    if len(lista) <= 1:
        return lista
    
    pivote = lista.pop()
    lista1= []
    lista2 = []

    for i in lista:
        if i <= pivote:
            lista1.append(i)
        else:
            lista2.append(i)
    
    lista1 = quick(lista1)
    lista2 = quick(lista2)
    return lista1 + [pivote] + lista2


arreglo= [1,2,7,1,-1,43,0]

print(quick(arreglo))
