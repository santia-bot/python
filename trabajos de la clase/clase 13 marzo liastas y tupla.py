print("clase de lista")
"""
nombre
telefono
correo
sintaxis: lista = []
sintanxis: tupla = ()
    #sub = lista2[:: -2] /brincos al reves
#sub = lista2[:: -1] #alreves
#sub = lista2[1::3] #brincos
#sub = lista2[::2]# 2 en 2 /buscar mas
)
#lista[:-1] #se imprimer el ultimo
"""
"""
lista = ["guadalupe", 32, "55523456", "diazsantix@gmail.com", False ]
#print(lista)
#slicing // buscar
lista2 = ["python", "java", "C++", "PHP", "MySQL", "C#"]

#print("llamar un elemento:", lista2[0])
#print("numeros de elementos en lista", len(lista2))

#sub = lista2[1::3]
"""
"""
print("\n sublista:", sub,)
lista2.append("POO")    # agrega un nuevo elemento al final
lista2.insert(1,"LINUX") #Agrega un nuevo elemento en el indice indicado
#lista2.remove("PHP")   #se quita un elemento
#lista2.sort()          #esto ordena de forma ascendente
#lista2.sort(reverse = True)     #se ordena de forma descendente
for i in lista2: #obtener los elementos de las listas
    print(i)
for i in range(len(lista2)):
    print(lista2[i])
print(",".join(lista2)) #imprime directo y sin corchetes
print(lista2)
"""


lista3 =[]
num = int(input("cuantos numeros desea ingresar:"))
x = 0
suma = 0
while x < num:
    lista3.append(int(input("ingrese un numero:")))
    x+=1
    print(lista3)
for i in lista3:
    suma += i
print(suma)

tupla = tuple(lista3)
lista4 = list(tupla)

print(tupla)
print(lista4)