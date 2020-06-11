tupla =("mexico", "colombia", "brasil", "peru", "chile", "ecuador")

lista = list(tupla)

pais =input(" \n cual es tu pais de origen: \n " )
si = pais in lista
if si == True:
    indice = lista.index(pais)
    print(" \n el pais", pais, " si se encuentra en la tupla en el index:", indice)

si == pais in lista
if si == False:
    print(" \n se esta agragando el pais... \n ")
    lista.append(pais)
    print(" \n el pais", pais, "ha sido agregado \n ")

for i in lista:
    print(i)

while True:
    remo = input(" \n que pais desea eliminar: \n ")
    si == remo in lista
    if si == True:
        print("eliminando...")
        lista.remove(remo)
        break 
    else:
        print("dato inavido o no se encuentra en la lista") 
        continue
   
tupla = tuple(lista)
print(tupla)
    


