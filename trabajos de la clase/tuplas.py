"""
tuplas
"""
"""
tupla = ("guadalupe", "antonio", "pilio", 32, "30076375609")
print("llamar un elemento:", tupla[0])
print("numeros de elementos",len(tupla))
subt = [:]
print( "\n subtupla:",subt )
#print(tupla[-2])
#tupla.append("juan") no se puede agregar
for i in lista2: #obtener los elementos de las listas
    print(i)
for i in range(len(lista2)):
    print(lista2[i])
print(",".join(lista2))
"""
"""
tupla = ("juan", "pedro", "alonzo", "ramiro", "su madre", "pilio")
print(tupla)
tupla = list(tupla)
tupla.append("carla")
print(tupla)
tupla = tuple(tupla)
print(tupla)
"""
"""
lista1 = []
num = int(input("ingrese un numero:"))
x = 0
mul = 0
while x < num:
    lista1.append(int(input("ingrese un numero")))
    x += 1
print(lista1)
mul1 = int(input("ingrese un numero para multiplicar:"))

for i in lista1:
    print(i * mul1)
tupla = tuple(lista1)
print(tupla)
"""
tupla =("juan", "antonio")
print(tupla)
lista = list(tupla)
lista.append("carla")
print(lista)

tupla =tuple(lista)
print(tupla)
si ="juan" in lista
if si ==True:
    print("juan esta dentro de la lista")