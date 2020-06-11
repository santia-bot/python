#se declaran los valores en las listas
lista1 =[1,3,5]
lista2 =[4,3,6]
lista3 =[7,3,9]
lista4 =[     ]
#se agragan las listas en una sola variablen
mati = lista1,lista2,lista3,lista4
#se suman los valores de las filas y columnas
suma1 = sum(lista1)
print("el resultado de", lista1[0],",",lista1[1],",",lista1[2], "es:", suma1)
suma2 = sum(lista2)
print("el resultado de", lista2[0],",",lista2[1],",",lista2[2], "es:", suma2)
suma3 = sum(lista3)
print("el resultado de", lista3[0],",",lista3[1],",",lista3[2], "es:", suma3)
suma4 = lista1[0] + lista2[0] + lista3[0]
print("el resultado de", lista1[0],",",lista2[0],",",lista3[0], "es:", suma4)
suma5 = lista1[1] + lista2[1] + lista3[1]
print("el resultado de", lista1[1],",",lista2[1],",",lista3[1], "es:", suma5)
suma6 = lista1[2] + lista2[2] + lista3[2]
print("el resultado de", lista1[2],",",lista2[2],",",lista3[2], "es:", suma6)
#se agragan los resultados resultados de las sumas a la lista
lista1.append(suma1)
lista2.append(suma2)
lista3.append(suma3)
lista4.append(suma4)
lista4.append(suma5)
lista4.append(suma6)
lista4.append(" ")
#se hace el rocorrido de la matriz
for f in range(4):
    for c in range(4):
        print(mati[f][c],end =' ' )
    print()
#se incorpora (if,elif,else) para mostrar si es prima o n o lo es
if lista1[-1] == lista4[0]:
    print("es prima")
elif lista1[-1] == lista4[1]:
    print("es prima")
elif lista1[-1] == lista4[2]:
    print("es prima")
elif lista2[-1] == lista4[0]:
    print("es prima")
elif lista2[-1] == lista4[1]:
    print("es prima")
elif lista2[-1] == lista4[2]:
    print("es prima")
elif lista3[-1] == lista4[0]:
    print("es prima")
elif lista3[-1] == lista4[1]:
    print("es prima")
elif lista3[-1] == lista4[2]:
    print("es prima")
else:
    print("no es prima")
