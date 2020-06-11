"""
diseña una funcion que dada una lista de numeros enteros, devuelva el numero de series de hay en ella.
llamamos serie a todo tramo con valores identicos.
"""
def series(lista):
    serie =set(lista)
    print(serie)
    print(len(lista))

def prome(lista):
    for i in lista:
        suma+= i
    promedio = suma/len(lista)
    return promedio
#main
lista =[1,1,8,8,8,8,0,0,2,10,10]
series(lista)
prome(lista)
promedio = pro(lista)
print(promedio)