# no me gusta
def counting(lista):
    aux = [0 for i in range(10)]
    resultado = [0 for i in range(len(lista))]

    for i in lista:
        aux[i] += 1

    for i in range(1,10):
        aux[i] += aux[i-1]

    for i in range(len(lista)):
        resultado[aux[lista[i]]-1] = lista[i]
        aux[lista[i]] -= 1

    return resultado


arreglo= [1,2,7,1,3,4,2]

print(counting(arreglo))
