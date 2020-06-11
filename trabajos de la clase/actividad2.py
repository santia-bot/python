lista = []
num = 10
i = 0
while i < num:
    numero = lista.append(int(input("ingrese un numero: \n ")))
    i = i + 1

lista.sort()
print("el numero menor es:", lista[0], "y", "el mayor numero es;", lista[-1])   
print(lista)

while True:
    sub = lista[print("rango que desea imprimir del",lista[0]):int(input("al:"))]
   
    si = sub in lista
    if si == True:
        print("\n sublista:", sub)
        break
    else:
        print("fuera de rango")
"""
while True:
    rango = int(input("ingrese el rango de tu lista que deseas imprimir {0} al: ")
    if rango < lista[9]:
        for x in lista:
            if x <= lista:
                rango,append(x)
        break
    else:
        print("no esta en lista"
"""
tupla =tuple(lista)
print(tupla)