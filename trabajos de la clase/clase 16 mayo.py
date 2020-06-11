tupla =("mexico", "colombia", "brasil", "peru", "chile", "ecuador")

lista = list(tupla)

pais =input("cual es tu pais de origen: \n " )
si = pais in lista
if si == True:
    indice = lista.index(pais)
    print("el pais", pais, " si se encuentra en la tupla en el index:", indice)

si == pais in lista
if si == False:
    print("se esta agragando el pais...")
    lista.append(pais)
    print("el pais", pais, "ha sido agregado")

for i in lista:
    print(i)